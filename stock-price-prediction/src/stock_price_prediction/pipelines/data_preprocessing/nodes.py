"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.5
"""
# Libraries for data loading, data manipulation and data visualisation
from typing import List, Dict
import pandas as pd      
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def feature_engineering(df) -> pd.DataFrame:
    df['Date'] = pd.to_datetime(df['Date'])
    df.insert(3,'Month',df.Date.dt.month)
    df.insert(2,'Year',df.Date.dt.year)
    df.insert(4,'Day',df.Date.dt.day)
    df['quarter'] = df['Date'].dt.quarter
    # Calculate the difference between "high" and "low" columns
    #df["price_spread"] = df["High"] - df["Low"]
    drop_df = df.drop(['Date','Close', 'Volume', 'Stock Trading'], axis=1)
    return drop_df