# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 02:29:44 2023

@author: 
"""

# Import necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def read_dataset(file_path):
    """Read the CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def display_dataset_info(dataframe):
    """Display the first and last few rows of the DataFrame and its information."""
    print("First Few Rows:")
    print(dataframe.head())
    print("\nLast Few Rows:")
    print(dataframe.tail())
    print("\nDataFrame Information:")
    print(dataframe.info())

def handle_missing_values(dataframe):
    """Fill missing values in 'Open', 'Close', 'High', and 'Low' columns with their respective modes."""
    for col in ['Open', 'Close', 'High', 'Low']:
        mode_value = dataframe[col].mode().iloc[0]
        dataframe[col] = dataframe[col].fillna(value=mode_value)
    
    # Check again for missing values after filling them
    print("\nMissing Values After Handling:")
    print(dataframe.isnull().sum())

def convert_date_and_set_index(dataframe, date_column='date'):
    """Convert the 'date' column to datetime format and set it as the index."""
    dataframe[date_column] = pd.to_datetime(dataframe[date_column])
    dataframe.set_index(date_column, inplace=True)
    
    return dataframe

def drop_missing_values(dataframe):
    """Drop rows with any remaining missing values."""
    dataframe = dataframe.dropna(axis=0)
    return dataframe

def plot_time_series(dataframe):
    """Plot a line chart for 'Close', 'High', 'Low', and 'Open' prices over time."""
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe['Close'], label='Close Value', color='pink', linestyle='-')
    plt.plot(dataframe['High'], label='High Value', color='blue', linestyle='-')
    plt.plot(dataframe['Low'], label='Low Value', color='yellow', linestyle='-')
    plt.plot(dataframe['Open'], label='Open Value', color='purple', linestyle='-')
    plt.title('Line Plot of Close, High, Low, and Open Prices Over Time')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

def display_descriptive_statistics(dataframe):
    """Display descriptive statistics of the DataFrame."""
    print("\nDescriptive Statistics:")
    print(dataframe.describe())

# File path to the dataset
file_path = 'C:/Users/hadid/Downloads/WLD_RTFP_country_2023-10-02.csv'

# Task 1: Exploratory Data Analysis

# Step 1: Read the dataset
df = read_dataset(file_path)

# Step 2: Display dataset information
display_dataset_info(df)

# Step 3: Handle missing values
handle_missing_values(df)

# Step 4: Convert date column and set index
df = convert_date_and_set_index(df)

# Step 5: Drop remaining missing values
df = drop_missing_values(df)

# Step 6: Plot time series
plot_time_series(df)

# Step 7: Display descriptive statistics
display_descriptive_statistics(df)

# Task 2: Dataset Information

"""
Dataset Name: Exploratory Data Analysis of Global Food Price Estimates

1. Purpose:
   - The code aims to perform Exploratory Data Analysis (EDA) on a global food price estimates and inflation information dataset.
   - The dataset includes monthly data by product, market, and country.

2. Dataset Information:
   - Source: https://www.kaggle.com/datasets/anshtanwar/monthly-food-price-estimates/data
   - Files: The dataset consists of three CSV files:
      - Monthly Food Price Inflation Estimates By Country
      - Monthly food price inflation estimates aggregated for all food products 
      - Monthly food price estimates by product and market

3. Data Cleaning:
   - Handling Missing Values:
      - The code identifies and addresses missing values in the 'Open', 'Close', 'High', and 'Low' columns by filling them with the respective mode values.
      - Remaining missing values are dropped.

4. Time Series Visualization:
   - Plotted a line chart showing the trends of 'Close', 'High', 'Low', and 'Open' prices over time, with the x-axis representing years.
"""
