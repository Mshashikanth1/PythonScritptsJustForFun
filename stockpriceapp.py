import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

# Simple Stock Price App


show are the stock **closing price** and ***volume *** of Google!
"""
)

searchsymbol='GOOGL'

#get the data of google using yfinance
searchdata=yf.Ticker(searchsymbol)

#get the historical prices for this ticker
searchdf=searchdata.history(period='1d',start='2010-5-31',end='2020-5-31')

#open high low close volume dividends stock splits
st.write("""
## Close

""")
st.line_chart(searchdf.Close)
st.write("""
## Volume
""")
st.line_chart(searchdf.Volume)

st.write("""
## High
""")
st.line_chart(searchdf.High)
