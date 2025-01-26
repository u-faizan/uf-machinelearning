import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This is an app builds a Machine Learning Model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

  st.write('**X**')
  x = df.drop('species',axis=1)
  x

  st.write('**Y**')
  y = df.species
  y

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

with st.sidebar:
  st.header('Input Feactures')
  # "species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  
  island = st.selectbox(
    "On which island was the penguin found?",
    ('Biscoe', 'Dream', 'Torgersen'),
  )

  gender = st.selectbox(
    "What is the gender of the penguin?",
    ('male','female'),
  )
  
  bill_length_mm = st.slider("What is the length of the penguin's bill in millimeters?", 32.10, 59.6, 43.9)
  bill_depth_mm = st.slider("What is the depth of the penguin's bill in millimeters?", 13.10, 21.50, 17.20)
  flipper_length_mm = st.slider("What is the length of the penguin's flipper in millimeters?", 172.0, 231.0, 201.0)
  body_mass_g = st.slider("What is the body mass of the penguin in grams?", 2700, 6300, 4207)
  



