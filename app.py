import streamlit as st
import pandas as pd
import pickle
import numpy as np

# App title
st.title('Sales From AD')
st.write('Prediciton APP.')

# Model
model = pickle.load(open('model_lr.pkl', 'rb'))

# User input
tv_budget = st.number_input('TV Budjet ($ in Millions)', min_value=0, max_value=500, value=100)
radio_budget = st.number_input('Radio Budjet ($ in Millions)', min_value=0, max_value=500, value=50)
newspaper_budget = st.number_input('Newspaper Budjet ($ in Millions)', min_value=0, max_value=500, value=30)

# Conversion into DataFrame
user_data = pd.DataFrame({
    'TV': [tv_budget],
    'Radio': [radio_budget],
    'Newspaper': [newspaper_budget]
})

# Predict the sales
if st.button('Predict  The Sales'):
    prediction = model.predict(user_data)
    st.write(f'The Number of Predicited sales:  $ {prediction[0]:.2f} Million')