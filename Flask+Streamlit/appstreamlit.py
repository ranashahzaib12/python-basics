#Only RUN in terminal by this "   streamlit run appstreamlit.py     "
# Then click on "Allow Access" OUTput will show in a browser

#Enter control+C to stop the terminal
import streamlit as st
import pandas as pd
import numpy as np

#Title of the application
st.title("Hello Streanlit")
#Displaying simple text
st.write("THis is a simple text")

#Creating a Data Frame

df = pd.DataFrame({  
    'one' :[1,2,3,4],
    'two' :[10,20,30,40]
})

#Displaying the Data Frame
st.write ("Hey this is a Data Frame")
st.write(df)


#Creating a line chart 
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)


