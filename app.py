from tempfile import NamedTemporaryFile
import os

import streamlit as st
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.readers.file import PDFReader
from streamlit_js_eval import streamlit_js_eval
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Resume Feedback Bot",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

if "messages" not in st.session_state.keys():  # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Please enter a job description and upload a resume to get feedback!"}
    ]

job_description_text = st.text_area("Paste Job Description Here", height=300)
uploaded_file = st.file_uploader("Upload Resume")
if job_description_text and uploaded_file:
    bytes_data = uploaded_file.read()
    with NamedTemporaryFile(delete=False) as tmp:  # open a named temporary file
        tmp.write(bytes_data)  # write data from the uploaded file into it
        with st.spinner(
            text="Loading and indexing the Streamlit docs – hang tight! This should take 1-2 minutes."
        ):
            reader = PDFReader()
            docs = reader.load_data(tmp.name)
            llm = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY"),
                base_url=os.getenv("OPENAI_API_BASE"),
                model="gpt-3.5-turbo-0125",
                temperature=0.0,
                system_prompt=f'''
                You are an experienced recruitment expert.
                A job seeker has submitted a resume for a position with the following job description:
                "{job_description_text}"
                Based on the resume submitted, provide detailed feedback and modifications to make it more relevant to the job description.
                '''
            )
            index = VectorStoreIndex.from_documents(docs)
    os.remove(tmp.name)  # remove temp file

    if "chat_engine" not in st.session_state.keys():  # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(
            chat_mode="condense_question", verbose=False, llm=llm
        )

is_magic = st.button("🪄 Magic_Rewrite Resume")
if is_magic:
    prompt ='''
    Please modify the resume based on the job description.
    Please point out which specifc part can be converted into a more related description.
    '''
    response = st.session_state.chat_engine.stream_chat(prompt)
    st.write_stream(response.response_gen)

is_clear = st.button("🧹 Clear_Reload Page")
if is_clear:
    streamlit_js_eval(js_expressions="parent.window.location.reload()")