import pickle
import streamlit as st
import numpy as np
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
en_voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
engine.setProperty(en_voice_id,1)
rate=engine.getProperty('rate')
engine.setProperty(rate,0.02)
st.set_page_config(page_title='Sample Machine Learning',layout='wide')
st.title("Predictive Sales Analytics based upon past 7 Days")
import warnings
warnings.filterwarnings('ignore')
from io import BytesIO
import pickle
import requests
mLink = 'https://github.com/Ajaybabuds/Predictive/blob/1ba3af6bcb3e367656e2a73589a4b5ea7136f6c4/Pred_Analytics.pkl?raw=true'
mfile = BytesIO(requests.get(mLink).content)
nt = pickle.load(mfile)
st.write("Select Date")
s=st.date_input('Date to Predict')
st.write("Enter Previous Week Sales")
col1,col2,col3,col4=st.beta_columns(4)
col5,col6,col7=st.beta_columns(3)
with col1:
    d1=st.number_input('Previous Day1')
with col2:
    d2=st.number_input('Previous Day2')
with col3:
    d3=st.number_input('Previous Day3')
with col4:
    d4=st.number_input('Previous Day4')
with col5:
    d5=st.number_input('Previous Day5')
with col6:
    d6=st.number_input('Previous Day6')
with col7:
    d7=st.number_input('Previous Day7')
holiday=st.select_slider("Is it Holiday or not",options=[0,1])
if st.button("Display result"):
    st.write("Predictive Result is:")
    result=nt.predict([[d1,d2,d3,d4,d5,d6,d7,holiday,s.isocalendar()[2],s.month]])
    res=np.round(result,2)
    engine.say("Predictive Sales for the Date")
    engine.say(s)
    engine.say(res)
    engine.runAndWait()
    st.write(np.round(result[0],2))
