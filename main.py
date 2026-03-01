import streamlit as st
import requests

st.title("Tweet Sentiment Analysis")

text=st.text_area("Enter your tweet")
if st.button("Predict"):
    response=requests.post("http://localhost:8000/predict",json={"text":text})
    if response.status_code==200:
        result=response.json()
        # st.write(f"Sentiment: {result['Prediction']}")
        st.markdown(
            f"<h1 style='text-align: center; color: green;'>Sentiment: {result['Prediction']}</h1>",
            unsafe_allow_html=True
        )
    else:
        st.write("Error in prediction")