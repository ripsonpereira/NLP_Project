import streamlit as st

import pickle

import pandas as pd
import numpy as np


from zipfile import ZipFile

import json

st.header('''
NLP mini project
''')

text = st.text_input('Enter your sentence in the Kannada Language')
st.write('bjsh')

file_name = "dictionary.zip"
with ZipFile(file_name, 'r') as zip1:
  zip1.extractall()

with open('dictionary.json', 'r') as fp:
  data = json.load(fp)

clf = pickle.load(open('model.pkl', 'rb'))

file1 = open('stopwords.txt', 'r',encoding="utf-8")
Lines = file1.readlines()
 

# Strips the newline character
stopwords=[]
for line in Lines:
    stopwords.append(str(line.strip()))
    


def prediction(input,stopwords=stopwords):
    longest = 340
    lst = input.split(' ')
   
    lst5=[i for i in lst if i not in stopwords ]

    lst6 = lst5
#     for each in lst5:
#         lst6.append(data[each])
        # print(data[each])
    # print(lst6)

    if len(lst6)<longest:
        lst8 = lst6 + ([0]*(longest-len(lst6)))
    # print(lst8)
    lst9 = np.asarray(lst8, dtype=np.float64)
    lst7 = lst9.reshape(1, -1)
    a = clf.predict(lst7)
    
    
    if a[0]==1:
        return "Positive"
    else:
        return "Negative"
       
    
if st.button(label="Submit"):
#   st.write("positive")
#   try:
    
    p=prediction(text)
    st.write(p)
    
#   except:
#     pass
# else:
#   pass
