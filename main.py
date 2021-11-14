import streamlit as st
from datetime import date

import investpy
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd



st.title('Crypto Currency Forecast App')

df=pd.read_csv('Updateddataset.csv')

crypto_stock=df['tag']

selected_stock = st.selectbox('Select dataset for prediction', crypto_stock)

dt1 = "01/01/2012"
dt2 = date.today().strftime("%d/%m/%Y")



n_years = st.slider('Years of prediction:', 1, 5)
period = n_years * 365

data_load_state = st.text('Loading data...')
data = investpy.get_crypto_historical_data(crypto=selected_stock, from_date=dt1,to_date= dt2)
data.reset_index(inplace=True)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data)



fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
st.plotly_chart(fig)

df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader('Forecast data')
st.write(forecast)

st.write(f'Forecast plot for {n_years} years')

fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)
