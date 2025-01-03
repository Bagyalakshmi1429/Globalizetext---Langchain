# Globalize text - A application for those who lacks in communication, they can use this app and they can reframe their mail etc.
# Langchain, Open source llm's, Streamlit

import streamlit as st 
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from PIL import Image
import os

api_key = "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"

st.set_page_config(page_title="Globalize Email",page_icon="💬") # Setting up some initial things
st.header("Globalize Text",divider='rainbow')

# Styling

# bg = """
# <style>
#     [data-testid="stApp"]{
#         background-color: #eae1d0;
#     }
#     [data-testid="stHeader"]{
#          background-color: #eae1d0;
#     }
# </style>
# """

# st.markdown(bg,unsafe_allow_html=True)

col1, col2 = st.columns(2) # Creating 2 cols

with col1: # Col1 can perform the below
    st.markdown("Struggling to find the right words for your emails? Whether you need to sound professional or keep it casual, our app is here to help! Using advanced language models, we transform your text into polished, well-phrased emails. Simply input your message, choose the tone—formal or informal—and let our app do the rest. Perfect for anyone looking to improve their communication skills effortlessly.")
    
with col2: # Col2 can perform the below
    # st.image(width=340,image="communicate.png")
    
    # Specifying the image path
    
    image_path = "communicate.png"
    
    try:
        image = Image.open(image_path)
        st.image(image, width=340)
    except Exception as e:
        st.error(f"Error loading image: {e}")

st.markdown("## Enter Your Email To Convert") 

col3, col4 = st.columns(2)

# Tone and Dialect
with col3: 
    tone = st.selectbox('Which tone would you like to have in email', ('Formal','Informal'))
with col4:
    dialect = st.selectbox('Which english dialect you like',('British','American'))

def getdata(): # For getting the user input
    inp = st.text_area(label="Field",placeholder="Type Your Email")
    return inp

email = getdata()
st.write(email) # Reflecting the response

st.markdown("## Your Converted Email") 

if tone == "Formal" and dialect == "American": # Specifying the conditions
    prompts = ChatPromptTemplate.from_messages([
        ("system","You are an email expert, turn the poor communication into formal tone, use american dialect"),
        ("user","Question:{question}")
    ])
elif tone == "Formal" and dialect == "British":
       prompts = ChatPromptTemplate.from_messages([
        ("system","You are an email expert, turn the poor communication into formal tone, use british dialect"),
        ("user","Question:{question}")
    ])
    
if tone == "Informal" and dialect == "American":
    prompts = ChatPromptTemplate.from_messages([
        ("system","You are an email expert, turn the poor communication into informal tone, use american dialect"),
        ("user","Question:{question}")
    ])
    
elif tone == "Informal" and dialect == "British":
    prompts = ChatPromptTemplate.from_messages([
        ("system","You are an email expert, turn the poor communication into informal tone, use british dialect"),
        ("user","Question:{question}")
    ])

groqllm = ChatGroq(model='llama3-8b-8192',temperature=0, api_key=api_key) # Instancing groq
output = StrOutputParser() # Parsing
chain = prompts|groqllm|output # Chain

if email:
    st.write(chain.invoke({'question': email})) # Invoking the chain
