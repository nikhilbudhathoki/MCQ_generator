import streamlit as st
import langchain
from langchain_groq import ChatGroq#: Connects to the Groq API to utilize the LPU-accelerated Gemma model.
from langchain_core.prompts import ChatPromptTemplate#Helps create a structured template for interacting with the LLM
from langchain.text_splitter import RecursiveCharacterTextSplitter#Splits large context or documents into smaller chunks for processing.
from langchain.chains.combine_documents import create_stuff_documents_chain# combine multiple smaller chunks of documents or text into a coherent and meaningful output.
from langchain.chains import create_retrieval_chain#d to extract relevant information from a PDF (or other document formats) and pass it to the LLM.
from langchain_community.vectorstores import FAISS#vector store db
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings#vector embedding
from dotenv import load_dotenv
import tempfile
import os
from langchain.schema import Document
import time
load_dotenv()
groq_api_key=os.getenv("groq_api_key")
os.environ['GOOGLE_API_KEY']=os.getenv("GOOGLE_API_KEY")
st.title("GEMMA MODEL CHATBOT")
st.write("Please Select according to given details\n: If the class is more and topic is complicated it may take some time .\n\n Please refresh the page and try again . \nThank you! ")
llm=ChatGroq(groq_api_key=groq_api_key,model_name="gemma2-9b-it")
prompt_mcq = ChatPromptTemplate.from_template(
    """Generate {num_questions} multiple-choice questions for grade {grade} on the subject {subject}, subtopic {subtopic}.
    Each question should have 4 options (A, B, C, D) with the correct answer. The questions should be clear and relevant to the topic.
    """)


grade=st.selectbox("Select your grade",[1,2,3,4,5,6,7,8,9,10])
subject=st.selectbox("Select your subject",["Mathematics","Science","English","Nepali","Grammar","Social","Computer","Health"])
subtopic=st.text_input("Enter your sub topic")
num_questions = st.number_input("Number of Questions", min_value=1, max_value=10, value=5)

def generate_mcq(grade, subject, subtopic, num_questions):
    try:
        prompt = prompt_mcq.format_messages(
            num_questions=num_questions,
            grade=grade,
            subject=subject,
            subtopic=subtopic
        )
        response = llm(prompt)
        if response:
            return response.content  # Adjust based on response structure
        else:
            return "Failed to generate MCQs."
    except Exception as e:
        return f"Error generating MCQs: {e}"

if st.button("Generate MCQs"):
    if subtopic:
        progress_bar=st.progress(0)
        try:
            for i in range(0,101):
                progress_bar.progress(i)
                
                time.sleep(0.05)
        
            mcq_text = generate_mcq(grade, subject, subtopic, num_questions)
            st.write(mcq_text)
        except Exception as E:
            st.error(f"Error generating mcqs {E}")
    else:
        st.error("Please enter a subtopic.")