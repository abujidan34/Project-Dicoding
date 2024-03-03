import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

Databike = pd.read_csv("Databike.csv")

st.header('Dashboard Data Persewaan Sepeda:sparkles:')

st.subheader('Total persewaan sepeda per jam')
fig, ax = plt.subplots(figsize=(16, 8))

sewa_jam = Databike.groupby('hr')['cnt_hour'].sum()

plt.bar(sewa_jam.index, sewa_jam.values, color='#1f77b4')
plt.title('Total persewaan sepeda per jam')
plt.xlabel('Jam')
plt.ylabel('Total Penyewaan')
st.pyplot(fig)

st.subheader('Total persewaan sepeda berdasarkan musim')
fig, ax = plt.subplots(figsize=(16, 8))

bike_day_season = Databike.groupby(by=['season_labels']).cnt_day.sum().reset_index().sort_values('cnt_day')
sns.barplot(x=bike_day_season['cnt_day'], y=bike_day_season['season_labels'], hue=bike_day_season['season_labels'], palette='rocket')
plt.xlabel("Musim")
plt.ylabel("Total Penyewa")
plt.title("Total persewaan sepeda berdasarkan musim", loc="center", fontsize=25)
st.pyplot(fig)

st.subheader('Hubungan jumlah sepeda yang disewa dengan kenaikan temperatur suhu di setiap musimnya')
fig, ax = plt.subplots(figsize=(16, 8))

sns.scatterplot(data=Databike, x="cnt_day", y="temp_day", hue="season_labels", style="season_labels") 
st.pyplot(fig)
