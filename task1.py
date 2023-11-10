# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Code Report

# Task 1: Exploring Global AI, ML, Data Science Jobs Overview for 2023

# Dataset Selection:
# I chose the dataset from ai-jobs.net, which provides information about salaries in AI, ML, and Data Science.
# The dataset link: https://ai-jobs.net/salaries/download
# This dataset is valuable for understanding trends, job titles, and experience levels in the industry for the year 2023.
# Kaggle Dataset Link: https://www.kaggle.com/datasets/lorenzovzquez/data-jobs-salaries/versions/3/data

# Initial Setup:
# The code begins with the necessary imports, including libraries like NumPy, Pandas, and Matplotlib.
# Additionally, it checks the file directory to ensure the correct file path.
# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
# Checking file directory
import os
# Replace '/kaggle/input' with the actual path if not using Kaggle
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Reading the CSV file
df = pd.read_csv('C:/Users/hadid/Downloads/salaries.csv')

# Displaying the dataset
df.head()  # Displaying the first few rows for a quick overview

# Checking the shape of the dataset
rows, columns = df.shape
print(f"The dataset has {rows} rows and {columns} columns.")

# Checking for missing values
missing_values = df.isna().sum().sum()
print(f"There are {missing_values} missing values in the dataset.")

# Checking for duplicated rows
duplicate_percentage = df.duplicated().sum() / rows
print(f"{duplicate_percentage:.2%} of the rows are duplicates.")

# Removing duplicate rows
df.drop_duplicates(inplace=True)

# Updated shape after removing duplicates
updated_rows, updated_columns = df.shape
print(f"After removing duplicates, the dataset has {updated_rows} rows and {updated_columns} columns.")

# Counting unique job titles
unique_job_titles = len(df.job_title.value_counts().index)
print(f"There are {unique_job_titles} unique job titles in the dataset.")

# Exploratory Data Analysis (EDA):

# Extracting data for the year 2023 and counting the top 10 job titles
data_2023 = df[df.work_year == 2023].job_title.value_counts().head(10)

# Bar chart for the top 10 most popular data-related job titles in 2023
data_2023.sort_values(ascending=True).plot(kind='bar', color='skyblue')

# Adding title and labels to the bar chart
plt.title('Top 10 Most Popular Data-Related Job Titles in 2023')
plt.xlabel('Job Titles')
plt.ylabel('Amount')

# Displaying the bar chart
plt.show()

# Visualizing Experience Levels:
# The code analyzes and visualizes the distribution of experience levels in the dataset.
# It shows the percentage of each experience level group using a bar chart.
# The chart is appropriately labeled with relevant information.

# Bar chart for the distribution of experience levels
experience_distribution = df.experience_level.value_counts(normalize=True) * 100
experience_distribution.reindex(['EN', 'MI', 'SE', 'EX']).plot(kind='bar', color='skyblue')

# Adding title and labels to the bar chart
plt.title('Experience Level Distribution')
plt.xlabel(None)
plt.ylabel('Percentage')
plt.xticks(np.arange(0, 4), ['Entry-level', 'Mid-level', 'Senior-level', 'Executive-level'], rotation=0)

# Displaying the bar chart
plt.show()
