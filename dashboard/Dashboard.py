import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul Web
st.set_page_config(page_title="Dashboard Bike Sharing")

# Load data 
df = pd.read_csv("semua_data.csv")

# Judul Dashboard
st.title("Dashboard Analisis Data Bike Sharing")

# Sidebar filter bulan
month_list = df['mnth_x'].unique()  
month = st.sidebar.selectbox("Pilih Bulan", month_list)

# Filter data berdasarkan bulan
month_data = df[df['mnth_x'] == month]

# Chart jumlah pendaftaran 
st.header("Jumlah Pendaftaran Bike Sharing")
fig1 = plt.figure(figsize=(10,4))
plt.plot(month_data['dteday_x'], month_data['registered_x'])  
st.pyplot(fig1)

# Chart kelembapan udara
st.header("Kelembapan Udara Bulanan") 
fig2 = plt.figure(figsize=(10,4))
plt.plot(month_data['dteday_x'], month_data['hum_y']) 
st.pyplot(fig2)

# Tabel data mentahnya
st.dataframe(month_data)