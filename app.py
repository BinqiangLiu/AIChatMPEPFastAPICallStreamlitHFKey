import requests
import streamlit as st
import timeit
import datetime

#import os
#from dotenv import load_dotenv
#load_dotenv()

#HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
#hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

st.set_page_config(page_title="Open AI USPTO MPEP Chat Assistant - Open Source Version", layout="wide")
st.subheader("Welcome to Open AI USPTO MPEP Chat Assistant: Life Enhancing with AI!")
st.write("Important notice: This Open AI USPTO MPEP Chat Assistant is offered for information and study purpose only and by no means for any other use. Check it out to see whether it could help you on your understanding of the USPTO MPEP. Any user should never interact with the AI Assistant in any way that is against any related promulgated regulations. The user is the only entity responsible for interactions taken between the user and the AI Chat Assistant.")

css_file = "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)  

pdf_file_name=""

with st.sidebar:
    #HUGGINGFACEHUB_API_TOKEN = st.text_input("Enter your AI Assistant Authenticateion Key here:")
    HUGGINGFACEHUB_API_TOKEN = st.text_input("Enter your AI Assistant Authenticateion Key here:", type="password")
    file_name_choice = st.selectbox("Select the part of MPEP to AI Chat", ("mpep-0000-table-of-contents","mpep-0005-change-summary","mpep-0010-title-page","mpep-0015-foreword","mpep-0020-introduction","mpep-0100","mpep-0200","mpep-0300","mpep-0400","mpep-0500","mpep-0600","mpep-0700","mpep-0800","mpep-0900","mpep-1000","mpep-1100","mpep-1200","mpep-1300","mpep-1400","mpep-1500","mpep-1600","mpep-1700","mpep-1800","mpep-1900","mpep-2000","mpep-2100","mpep-2200","mpep-2300","mpep-2400","mpep-2500","mpep-2600","mpep-2700","mpep-2800","mpep-2900","mpep-9005-appx-i","mpep-9010-appx-ii","mpep-9015-appx-l","mpep-9020-appx-r","mpep-9025-appx-t","mpep-9030-appx-ai","mpep-9035-appx-p","mpep-9090-subject-matter-index","mpep-9095-Form-Paragraph-Chapter"))
    if file_name_choice == "mpep-0000-table-of-contents":
        pdf_file_name = "mpep-0000-table-of-contents.pdf"
    elif file_name_choice == "mpep-0005-change-summary":
        pdf_file_name ="mpep-0005-change-summary.pdf"
    elif file_name_choice == "mpep-0010-title-page":
        pdf_file_name ="mpep-0010-title-page.pdf"
    elif file_name_choice == "mpep-0015-foreword":
        pdf_file_name ="mpep-0015-foreword.pdf"
    elif file_name_choice == "mpep-0020-introduction":
        pdf_file_name ="mpep-0020-introduction.pdf"
    elif file_name_choice == "mpep-0100":
        pdf_file_name ="mpep-0100.pdf"
    elif file_name_choice == "mpep-0200":
        pdf_file_name ="mpep-0200.pdf"
    elif file_name_choice == "mpep-0300":
        pdf_file_name ="mpep-0300.pdf"
    elif file_name_choice == "mpep-0400":
        pdf_file_name ="mpep-0400.pdf"
    elif file_name_choice == "mpep-0500":
        pdf_file_name ="mpep-0500.pdf"
    elif file_name_choice == "mpep-0600":
        pdf_file_name ="mpep-0600.pdf"
    elif file_name_choice == "mpep-0700":
        pdf_file_name ="mpep-0700.pdf"
    elif file_name_choice == "mpep-0800":
        pdf_file_name ="mpep-0800.pdf"
    elif file_name_choice == "mpep-0900":
        pdf_file_name ="mpep-0900.pdf"
    elif file_name_choice == "mpep-1000":
        pdf_file_name ="mpep-1000.pdf"
    elif file_name_choice == "mpep-1100":
        pdf_file_name ="mpep-1100.pdf"
    elif file_name_choice == "mpep-1200":
        pdf_file_name ="mpep-1200.pdf"
    elif file_name_choice == "mpep-1300":
        pdf_file_name ="mpep-1300.pdf"
    elif file_name_choice == "mpep-1400":
        pdf_file_name ="mpep-1400.pdf"
    elif file_name_choice == "mpep-1500":
        pdf_file_name ="mpep-1500.pdf"
    elif file_name_choice == "mpep-1600":
        pdf_file_name ="mpep-1600.pdf"
    elif file_name_choice == "mpep-1700":
        pdf_file_name ="mpep-1700.pdf"
    elif file_name_choice == "mpep-1800":
        pdf_file_name ="mpep-1800.pdf"
    elif file_name_choice == "mpep-1900":
        pdf_file_name ="mpep-1900.pdf"
    elif file_name_choice == "mpep-2000":
        pdf_file_name ="mpep-2000.pdf"
    elif file_name_choice == "mpep-2100":
        pdf_file_name ="mpep-2100.pdf"
    elif file_name_choice == "mpep-2200":
        pdf_file_name ="mpep-2200.pdf"
    elif file_name_choice == "mpep-2300":
        pdf_file_name ="mpep-2300.pdf"
    elif file_name_choice == "mpep-2400":
        pdf_file_name ="mpep-2400.pdf"
    elif file_name_choice == "mpep-2500":
        pdf_file_name ="mpep-2500.pdf"
    elif file_name_choice == "mpep-2600":
        pdf_file_name ="mpep-2600.pdf"
    elif file_name_choice == "mpep-2700":
        pdf_file_name ="mpep-2700.pdf"
    elif file_name_choice == "mpep-2800":
        pdf_file_name ="mpep-2800.pdf"
    elif file_name_choice == "mpep-2900":
        pdf_file_name ="mpep-2900.pdf"
    elif file_name_choice == "mpep-9005-appx-i":
        pdf_file_name ="mpep-9005-appx-i.pdf"
    elif file_name_choice == "mpep-9010-appx-ii":
        pdf_file_name ="mpep-9010-appx-ii.pdf"
    elif file_name_choice == "mpep-9015-appx-l":
        pdf_file_name ="mpep-9015-appx-l.pdf"
    elif file_name_choice == "mpep-9020-appx-r":
        pdf_file_name ="mpep-9020-appx-r.pdf"
    elif file_name_choice == "mpep-9025-appx-t":
        pdf_file_name ="mpep-9025-appx-t.pdf"
    elif file_name_choice == "mpep-9030-appx-ai":
        pdf_file_name ="mpep-9030-appx-ai.pdf"
    elif file_name_choice == "mpep-9035-appx-p":
        pdf_file_name ="mpep-9035-appx-p.pdf"
    elif file_name_choice == "mpep-9090-subject-matter-index":
        pdf_file_name ="mpep-9090-subject-matter-index.pdf"
    elif file_name_choice == "mpep-9095-Form-Paragraph-Chapter":
        pdf_file_name ="mpep-9095-Form-Paragraph-Chapter.pdf"    
    current_datetime = datetime.datetime.now()
    print("Content selected: "+pdf_file_name)
    print(f'Content selected: {pdf_file_name} @ {current_datetime}') 

def call_chatbot_api(pdf_file_name, user_question):
    #url = 'https://binqiangliu-fastapi-in-docker.hf.space/api/chat'
    #url = 'https://binqiangliu-officialusinositechatv1api.hf.space/api/chat'
    #url = 'https://binqiangliu-aichatmpep-fastapi.hf.space/query'
    #url = 'https://binqiangliu-aichatmpep-fastapi-v1.hf.space/query'
    url = 'https://binqiangliu-aichatmpep-fastapi-privatetest.hf.space/query'
    #url = 'https://ishare-aichatmpep-fastapi.hf.space/query'    
    
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"
    #保险起见，建议始终采用f''的形式以及配合使用{}
    }
    
    #headers = {
    #'Authorization': f'Bearer {hf_token}',  # 使用Bearer令牌类型
    #'Content-Type': 'application/json',  # 根据API的要求设置合适的Content-Type
    #}
    
    json_data_for_api = {
        'pdf_file_name': pdf_file_name,
        'user_question': user_question
    }
    
    #response = requests.post(url, json=json_data_for_api) 
    #如果被调用的API不需要headers验证(例如不是private)，则不需要加headers参数，否则画蛇添足！
    response = requests.post(url, headers=headers, json=json_data_for_api) 
    #必须要有headers=..., json=...这种形式
    
    result = response.json()
    return result['response']

user_query = st.text_input("Enter your query here:")
if st.button('Get AI Resposne'):
    if user_query !="" and not user_query.strip().isspace() and not user_query == "" and not user_query.strip() == "" and not user_query.isspace():
        with st.spinner("AI Thinking...Please wait a while to Cheers!"):  
            print("Ready to Call API - Chapter selected: "+pdf_file_name)
            print("User question: "+user_query)             
            start_1 = timeit.default_timer() # Start timer
            print(f"API调用开始：{start_1}")                     
            response = call_chatbot_api(pdf_file_name, user_query)
            end_1 = timeit.default_timer() # Start timer
            print(f"API调用结束：{end_1}")
            print(f"API调用耗时：{end_1 - start_1}")     
            st.write("USino AI Response:")
            st.write(response)
            print(response)  # 打印Chatbot的响应
