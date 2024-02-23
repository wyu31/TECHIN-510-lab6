# TECHIN-510-lab6
This repository features a resume advisor leveraging LLMs, including OpenAI and chatbots. Users can input a job description and upload their CV for AI-driven suggestions on tailoring their resume to better match the specific job requirements. 

The Web App can be visited at:
https://wyu31resumemodification.azurewebsites.net/

## How to Run
1. Run the commands below in the terminal for initial settings
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env
```
2. Change the ```.env``` file to match your environment
3. Run the commands below in the terminal to trigger the Web App
```bash
streamlit run app.py
```

## What's Included
```app.py```: The main python script file for the resume modification Web App  
```requrements.txt```: List necessary libraries and dependencies required for the App, ensuring to install it  
```.env.sample```: A template showcasing the structure and format of environment variables necessary for configuring the application

## Lessons Learned
- Utilizing Session State, variables can be retained and shared between these reruns within the same user session. This is particularly useful in multi-page apps or when needing to maintain user input or processes across interactions.
- With the customised prompts, the OpenAI model can be modifed for a specif use.
- The PDFReader tool is designed to parse and extract data from PDF files, streamlining the process of gathering and processing information from documents.
- VectorStoreIndex The VectorStoreIndex works by indexing data in a way that makes searching and accessing information faster and more intuitive, further improving efficiency in handling and retrieving data.

## Questions
- Why do some interactions work flawlessly on terminal-triggered web pages hosted locally, yet when accessed through the deployed website, certain functionalities encounter errors?
-  I attempted to replace the dialog box, which collects user input, with a "Start Analysis" button aimed at prompting the intelligent assistant to edit the resume. However, this change resulted in the assistant producing blank responses. What steps should I take to effectively implement a button-driven approach while ensuring the AI assistant delivers meaningful feedback?
- After updating a resume in accordance with a job description, what method can be employed to start another round of edits on the resume based on a new JD without needing to leave the webpage?
- I've noticed that the suggestions for revising resume don't seem closely related with the JD. What steps can I take to improve the relevance of the resume revision suggestions to better match the JD?
- Is it possible for the AI assistant to actively edit specific sections of resume, rather than just providing broad and general recommendations?