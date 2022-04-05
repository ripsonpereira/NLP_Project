import streamlit as st

import pickle

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

from zipfile import ZipFile

import json

st.header('''
NLP mini project
''')

text = st.text_input('Enter your sentence in the Kannada Language')

file_name = "dictionary.zip"
with ZipFile(file_name, 'r') as zip1:
  zip1.extractall()

with open('dictionary.json', 'r') as fp:
  data = json.load(fp)

clf = pickle.load(open('model.pkl', 'rb'))

def prediction(input):
    longest = 2875
    lst5 = input.split(' ')
    lst6 = []
    for each in lst5:
        lst6.append(data[each])
    if len(lst6)<longest:
        lst6 = lst6 + ([0]*(longest-len(lst6)))
    lst6 = np.asarray(lst6, dtype=np.float64)
    lst7 = lst6.reshape(1, -1)
    a = clf.predict(lst7)
    print(a)
    if a==1:
      st.write('Positive Sentiment')
    elif a==0:
      st.write('Negative Sentiment')
      
if st.button(label="Submit"):
  try:
    prediction(input)
  except:
    pass
else:
  pass
    
