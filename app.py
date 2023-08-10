import streamlit as st
import plotly.express as px
import numpy as np 
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from kedro.config import ConfigLoader
from kedro.framework.project import settings
import logging.config
from kedro.framework.context import KedroContext
import requests
from PIL import Image


from kedro.io import DataCatalog
import yaml

from kedro.extras.datasets.pickle import PickleDataSet

from kedro.extras.datasets.pandas import (
    CSVDataSet,
    SQLTableDataSet,
    SQLQueryDataSet,
    ParquetDataSet,
)

config = {
    "train_data": {
        "type": "pandas.CSVDataSet",
        "filepath": "C:/Users/emmau/Downloads/stock-price-prediction/stock-price-prediction/data/01_raw/train.csv"
    },
    "reg_model": {
        "type": "pickle.PickleDataSet",
        "filepath": "C:/Users/emmau/Downloads/stock-price-prediction/stock-price-prediction/data/06_models/reg_model.pickle",
        "backend": "pickle"
    },
    "predictions": {
        "type": "pandas.CSVDataSet",
        "filepath": "C:/Users/emmau/Downloads/stock-price-prediction/stock-price-prediction/data/07_model_output/predictions.csv"
    },
}

#retieving keys and secret
conf_path = "conf/"
conf_loader = ConfigLoader(conf_path)
conf_catalog = conf_loader.get("**/catalog.yml")

catalog = DataCatalog.from_config(config, conf_catalog)


#cache function that loads in data
#@st.cache(allow_output_mutation = True)
def load_data(data_name):
    data = catalog.load(data_name)
    #can add extra stuff here
    return data


data_load_state = st.text('Loading data from data directory...')
data = load_data("train_data")
#catalog.save("boats", df)

data_load_state.text("")

#load in regression model
regressor = catalog.load("reg_model")


def main():

    st.title('Stock Price Prediction App')
    st.sidebar.header('User Inputs')
    ticker_symbol = st.sidebar.text_input('Enter Ticker Symbol', '9983')
    #date = st.sidebar.date_input('Select Date', pd.Timestamp.now())
    image1_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/UNIQLO_logo.svg/306px-UNIQLO_logo.svg.png?20110923051949'
    # Display the Uniqlo logo in the sidebar
    st.sidebar.image(image1_url, use_column_width=True)

    
    st.write('Enter the stock data:')
    open_price = st.number_input('Open Price')
    high_price = st.number_input('High Price')
    low_price = st.number_input('Low Price')
    year = st.number_input('Year')
    month =  st.number_input('Month')

    

    if st.button('Predict'):
        input_data = pd.DataFrame({
            'Open': [open_price],
            'Year': [year],
            'High': [high_price],
            'Month': [month],
            'Low': [low_price]
        })
        
        prediction = regressor.predict((input_data))[0]
        # Display prediction using components
        st.subheader('Prediction')
        prediction_text = f'Predicted Close Price: **¥{prediction:.2f}**'
        st.markdown(prediction_text, unsafe_allow_html=True)
        
        







if __name__ == '__main__':
    main()
