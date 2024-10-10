import pandas as pd
file_path = "F:\Data Analysis - Python\Superstore.csv"
data = pd.read_csv(file_path, encoding='ISO-8859-1')
print(data.head(2))

# exploring the data
print(data.info())

# describing the numerical columns
print(data.describe())

# checking for nulls
print(data.isnull().sum())
data_cleaned = data.dropna()

# Basic Analysis
# Group data by a certain column and calculate mean
grouped_data = data_cleaned.groupby('Region')['Profit'].mean()

# Print grouped data
print(grouped_data)

# load the visualization libraries
import seaborn as sb
import matplotlib.pyplot as plt

# a simple visualization
plt.figure(figsize=(20,8))
sb.barplot(x='Region', y= 'Profit', data = data_cleaned)
plt.title('Profit Analysis by Region')
plt.show()
