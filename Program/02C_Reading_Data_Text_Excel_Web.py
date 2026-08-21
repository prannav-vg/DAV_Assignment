"""
Experiment 2C: Reading Data from Text Files, Excel, and the Web

AIM:
To read and process data from various sources, including text files, Excel
spreadsheets, and web-based data, using Python's Pandas library.
"""

import pandas as pd

# Read data
text_df = pd.read_csv('Google_data (2b.c1).csv')
excel_df = pd.read_excel('data (2c2).xlsx', sheet_name='Sheet1')
web_df = pd.read_csv('https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv')  # Replace with actual URL

# Display data
print(text_df.head(), "\n", excel_df.head(), "\n", web_df.head())

# Handle missing values
text_df.fillna(method='ffill', inplace=True)
excel_df.fillna(method='bfill', inplace=True)
web_df.dropna(inplace=True)

# Save processed data
text_df.to_csv('processed_text.csv', index=False)
excel_df.to_excel('processed_excel.xlsx', index=False)
