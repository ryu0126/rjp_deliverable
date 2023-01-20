import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
from scipy import integrate
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Meiryo'
import streamlit as st
from PIL import Image

anaban = pd.read_csv('data_csv/anaban.csv')
bton = pd.read_csv('data_csv/bton.csv')
hauru = pd.read_csv('data_csv/hauru.csv')
lovesong = pd.read_csv('data_csv/lovesong.csv')
mani = pd.read_csv('data_csv/ma-ni-.csv')
violet = pd.read_csv('data_csv/violet.csv')

st.title('映画を観た感情の起伏')

img = Image.open('スプラトゥーン3.jpg')
if st.checkbox('check'):
    st.image(img,caption='スプラトゥーン',use_column_width=True)

left_column,right_column = st.beta_columns(2)
left_column.image(img,caption='スプラトゥーン',use_column_width=True)
right_column.image(img,caption='スプラトゥーン',use_column_width=True)