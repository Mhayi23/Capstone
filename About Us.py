import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from pytz import country_names

sns.set()

data=pd.read_csv("CAPSTONEDATA.csv")
st.write("Gross Sales by Country")
st.line_chart(data,x="COUNTRY",y="GROSSSALES")

st.divider()
fig2, ax2 = plt.subplots()
plt.hist(data["COUNTRY"],bins=6, color="green",edgecolor="black")
ax2.set_xlabel("COUNTRY")
ax2.set_ylabel("NETSALES")
st.pyplot(fig2)

st.divider()
countries = ['FRANCE', 'GERMANY', 'POLAND', 'CANADA', 'SPAIN']
net_sales = [500000, 300000, 450000, 200000, 150000]  # Net sales in USD
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
#plt.pie(net_sales, labels=country_names, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Net Sales Distribution by Country')
plt.show()
