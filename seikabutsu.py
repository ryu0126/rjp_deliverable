import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
from scipy import integrate
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Meiryo'

anaban = pd.read_csv('data_csv/anaban.csv')
bton = pd.read_csv('data_csv/bton.csv')
hauru = pd.read_csv('data_csv/hauru.csv')
lovesong = pd.read_csv('data_csv/lovesong.csv')
mani = pd.read_csv('data_csv/ma-ni-.csv')
violet = pd.read_csv('data_csv/violet.csv')

st.title('映画を観た感情の起伏')

