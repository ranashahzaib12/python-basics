#Only RUN in terminal by this "   streamlit run widgetStreamlit.py    "
# Then click on "Allow Access" OUTput will show in a browser

#Enter control+C to stop the terminal

import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")
#Taking input from user and saving it into 'name' variable and displaying it

age = st.slider("select your age:" , 0,100,25) #Between 100 and 0 but minimum is 25
st.write(f"Your age is {age}")
options = ['py' , 'java' , 'c' , 'C++' , "r"]
choice = st.selectbox("Choose your favourite language :", options)
st.write(f"Your choice is:{choice}")



if name:
    st.write(f"Hello {name}")
