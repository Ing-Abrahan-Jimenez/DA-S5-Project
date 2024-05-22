import streamlit as st
import pandas as pd
import plotly_express as px
data_vehicles = pd.read_csv(
    r"D:\Cursos\Data analyst Triple ten\Proyectos triple ten\Sprint 5\vehicles_us.csv")

st.title('Enterprise cars stock')
st.header('Vehicels in stock analyse')
st.write('Check out wich kind of car you can buy in the store, in the next graphs you will see a big view of all our ptoducts.')
st.subheader('Prices')
st.write('Click on the next button to know all our prices.')
price_hst_butt = st.button('Take a look to our prices!')
if price_hst_butt:
    st.write('These are our different prices!')
    price_hst = px.histogram(data_vehicles, x="price")
    st.plotly_chart(price_hst, use_container_width=True)

st.header("this web page is not complete...")
