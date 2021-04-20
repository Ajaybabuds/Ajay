#!/usr/bin/env python
# coding: utf-8

# In[66]:


import streamlit as st
st.title("TYRE PURCHASES OF A CLIENT")
st.header("Total Sales by Different Categories")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\ajay\\Downloads\\Sales Data.csv")
df=df.drop_duplicates(subset=['Internal ID'])
sts=df.groupby(['Status']).sum().drop(['Internal ID','Item Rate','Quantity'],axis=1).round(2)
df['Date']=pd.to_datetime(df['Date'])
df['Month']=df['Date'].apply(lambda x:x.strftime('%B'))
df['Year']=df['Date'].dt.year
yr=df.groupby(['Year']).sum().drop(['Internal ID','Item Rate','Quantity'],axis=1)
mnth=df.groupby(['Month']).sum().drop(['Internal ID','Item Rate','Quantity','Year'],axis=1)
ax=yr.plot.barh(colormap='gist_rainbow')
number=st.number_input("Insert a number")
st.write(number)
color=st.select_slider('Select a Sales by',options=['Status','Year','Month']) 
if 'Status' in color:
        st.table(sts)
        st.bar_chart(sts)
elif 'Year' in color:
        st.write("Sales by Year:",yr)
        st.bar_chart(yr,height=5,width=8)
elif 'Month' in color:
        st.write("Sales by Month:",mnth)
        st.bar_chart(mnth)


# In[64]:





# In[ ]:




