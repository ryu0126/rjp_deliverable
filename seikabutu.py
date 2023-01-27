import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from scipy import stats
from scipy import integrate
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Meiryo'


st.title('映画を観た感情の起伏')

st.write('display image')
img = Image.open('C:/Users/koyama/OneDrive/rjp/rjp_streamlit/data/onepiece01_luffy.jpg')
st.image(img,caption='a',use_column_width=True)

link = '[GitHub](http://github.com)'
st.markdown(link, unsafe_allow_html=True)

left_column,right_column = st.columns(2)

st.write('display image')
imgi = Image.open('C:/Users/koyama/OneDrive/rjp/rjp_streamlit/data/onepiece01_luffy.jpg')
left_column.image(imgi,caption='a',use_column_width=True)
    
imgz = Image.open("C:/Users/koyama/OneDrive/rjp/rjp_streamlit/data/onepiece02_zoro_bandana.jpg")
right_column.image(imgz,caption='z',use_column_width=True)

img = Image.open("C:/Users/koyama/OneDrive/rjp/rjp_streamlit/data/onepiece05_sanji.jpg")
st.image(img,caption='s',use_column_width=True)
    
img = Image.open("C:/Users/koyama/OneDrive/rjp/rjp_streamlit/data/onepiece04_usopp_sogeking.jpg")
st.image(img,caption='u',use_column_width=True)