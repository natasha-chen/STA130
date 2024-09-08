#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset from the URL
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
df = pd.read_csv(url)

# Get the count of missing values for each column
missing_counts = df.isnull().sum()

# Output the missing values count
print(missing_counts)


# In[3]:


import pandas as pd

# Load the dataset into a DataFrame
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
df = pd.read_csv(url)

# Get the shape of the DataFrame
num_rows, num_columns = df.shape

# Print the results
print(f"The dataset has {num_rows} rows and {num_columns} columns.")


# "observations": characteristics of a data point represented by a row
# "variables": characteristics recorded of all observations represented by a column

# In[5]:


import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
df = pd.read_csv(url)

# Descriptive statistics for numerical columns
print("Descriptive Statistics for Numerical Columns:\n")
print(df.describe())

# Value counts for categorical columns like 'Type 1'
print("\nDistribution of Pokémon by Primary Type:\n")
print(df['Type 1'].value_counts())


# "attributes": access characteristics of an object within the object. It does not compute anything since it is an existing value. 
# "method": a function that computes the data within the object that may need arguments inputed (which is why it has ()). It returns a new object or modifies the original one. 

# ChatGPT link:https://chatgpt.com/c/66ddfbd2-01cc-8007-8ad4-ea838530bb25 and summary: 
# 
# Dataset: Pokémon dataset from GitHub (link).
# 
# Used df.shape to determine that the dataset has 800 rows (observations) and 12 columns (variables).
# Observations & Variables:
# 
# Observations: Each row represents a Pokémon.
# Variables: Each column represents an attribute (e.g., Name, Type 1, HP).
# Data Summary:
# 
# df.describe(): Provides statistical summaries of numerical columns (e.g., mean, min, max).
# df['column'].value_counts(): Displays the frequency of unique values in categorical columns (e.g., Pokémon types).
# Attributes vs. Methods:
# 
# Attributes (e.g., df.shape): Represent stored information and do not use parentheses.
# Methods (e.g., df.describe()): Perform actions or computations and require parentheses.
# This summary outlines our key discussions on analyzing and summarizing the Pokémon dataset using pandas.
