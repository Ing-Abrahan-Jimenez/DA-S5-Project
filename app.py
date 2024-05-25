import os
import streamlit as st
import pandas as pd
import plotly_express as px

current_route = os.path.dirname(__file__)
file_path = os.path.join(current_route, 'vehicles_us.csv')

data_vehicles = pd.read_csv(file_path)

st.title('Enterprise cars stock')
st.header('Vehicels in stock analyse')
st.write('Check out wich car fits to your wallet, in the next graphs you will see a big view of all our ptoducts.')
st.subheader('Prices')
st.write('Click on the next button to know all our prices.')
price_hst_butt = st.button('Take a look to our prices!')
if price_hst_butt:
    st.write('These are our different prices!')
    st.write(
        'Each point is a different price for the model that you are interesed in.')
    price_hst = px.scatter(data_vehicles, y="price", x="model")
    st.plotly_chart(price_hst, use_container_width=True)
st.subheader('Odometer x Price')
st.write('The next button will show you something speciall...')
od_pr_butt = st.button("See what I'm talking about")
if od_pr_butt:
    od_pr = px.scatter(data_vehicles, x='odometer', y='price')
    st.plotly_chart(od_pr, use_container_widht=True)
    st.write('Most of our cars has low milles in the odometer :sunglasses:')
st.subheader('Car conditions')
st.write('Are you loking for the best? Take a look to the car conditions & their prices!')
good = st.checkbox('Good')
good_cond = data_vehicles[data_vehicles['condition'] == 'good']
like_new = st.checkbox('Like new')
l_n_cond = data_vehicles[data_vehicles['condition'] == 'like new']
excellent = st.checkbox('Excelent')
ex_cond = data_vehicles[data_vehicles['condition'] == 'excellent']
new = st.checkbox('New')
new_cond = data_vehicles[data_vehicles['condition'] == 'new']
fair = st.checkbox('Fair')
fair_cond = data_vehicles[data_vehicles['condition'] == 'cond']
salvage = st.checkbox('Salvage')
sal_cond = data_vehicles[data_vehicles['condition'] == 'salvage']
if good:
    cond_hist = px.histogram(good_cond, x='odometer', y='price')
    st.plotly_chart(cond_hist, use_container_width=True)
elif like_new:
    cond_hist = px.histogram(l_n_cond, x='odometer', y='price')
    st.plotly_chart(cond_hist, use_container_width=True)
elif excellent:
    cond_hist = px.histogram(ex_cond, x='odometer', y='price')
    st.plotly_chart(cond_hist, use_container_width=True)
elif new:
    cond_hist = px.histogram(new_cond, x='odometer', y='price')
    st.plotly_chart(cond_hist, use_container_width=True)
elif fair:
    cond_hist = px.histogram(fair_cond, x='odometer', y='price')
    st.plotly_chart(cond_hist, use_container_width=True)
elif salvage:
    cond_hist = px.histogram(sal_cond, x='odometer', y='price')
    st.plotly_chart(cond_hist, use_container_width=True)
st.header("This web page is not complete...")
