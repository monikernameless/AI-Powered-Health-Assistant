import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input or "symptoms" in user_input:
        return "Please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input,max_length = 500,num_return_sequences=2)
        return response[0]['generated_text']            

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User : ",user_input)
            with st.spinner("Processing your query, Please wait ...."):
                response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant : ",response)
            print(response)
        else:
            st.write("Please enter a message to get a response.")

main()  



#   Local URL: http://localhost:8502
#   Network URL: http://10.182.27.58:8502
# if __name__=="__main__":
# main()