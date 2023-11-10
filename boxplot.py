# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 02:56:33 2023

@author:  
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Function to generate a box plot for given columns in a DataFrame
def plot_box(df, x_col, y_col, xlabel, ylabel, title, rotation=None):
    """
    Parameters:
    - df: DataFrame
    - x_col: str, column name for x-axis
    - y_col: str, column name for y-axis
    - xlabel: str, label for x-axis
    - ylabel: str, label for y-axis
    - title: str, title of the plot
    - rotation: int, rotation angle for x-axis labels (default=None)
    """
    sns.boxplot(x=x_col, y=y_col, data=df)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if rotation:
        plt.xticks(rotation=rotation)
    plt.show()

# Section 1: Data Loading and Preprocessing
# Read the CSV file (Update the path to your specific location)
df = pd.read_csv("C:/Users/hadid/Downloads/used_cars_UK.csv")
df.drop(columns=["Unnamed: 0"], inplace=True)

# Data preprocessing and label encoding
# Map categorical values to numerical values
df["Emission Class"] = df["Emission Class"].map({"Euro 1": 1, "Euro 2": 2, "Euro 3": 3, "Euro 4": 4, "Euro 5": 5, "Euro 6": 6})
df["Fuel type"] = df["Fuel type"].map({"Diesel": 0, "Petrol": 1})
label_encoder = LabelEncoder()
df["Engine"] = label_encoder.fit_transform(df["Engine"])
df["Body type"] = label_encoder.fit_transform(df["Body type"])

# Section 2: Correlation Analysis
# Select relevant columns for correlation analysis
correlation_matrix = df[["Price", "Mileage(miles)", "Doors", "Previous Owners", 
                         "Emission Class", "Fuel type", "Engine", "Body type"]].corr()

# Section 3: Data Visualization
# Plot box plot for Price by Emission Class
plot_box(df, 'Emission Class', 'Price', 'Emission Class', 'Price', 'Box Plot of Price by Emission Class')

# Convert "Mileage(miles)" column to int type values
df["Mileage(miles)"] = df["Mileage(miles)"].astype(int)

# Group "Mileage(miles)" values in specific ranges
df["Mileage Group"] = pd.cut(df["Mileage(miles)"], bins=30).astype(str)

# Plot box plot for Price by Mileage Group
plot_box(df, 'Mileage Group', 'Price', 'Mileage Group', 'Price', 'Box Plot of Price by Mileage Group', rotation=45)
