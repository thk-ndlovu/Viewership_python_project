# Meta Deta
The dataset provides detailed information on customer viewing activity. Each record includes the date of viewing (DateID), a unique customer identifier (CustomerID), the total time spent watching (TotalTimeWatched), the platform used to access the content (Platform), the type of playback event (PlayEventType), and the title of the video viewed (VideoTitle). This structure allows for analysis of viewing patterns, customer behavior, and platform usage.

# Install Dependencies
# Allows to open an Excel file and read data                                                                                                                                                                                                                                                                                                                                                                                            
!pip install openpyxl
Requirement already satisfied: openpyxl in /local_disk0/.ephemeral_nfs/envs/pythonEnv-93dd90d0-48c3-47e6-8d5c-7b6310c36c27/lib/python3.12/site-packages (3.1.5)
Requirement already satisfied: et-xmlfile in /local_disk0/.ephemeral_nfs/envs/pythonEnv-93dd90d0-48c3-47e6-8d5c-7b6310c36c27/lib/python3.12/site-packages (from openpyxl) (2.0.0)
Note: you may need to restart the kernel using %restart_python or dbutils.library.restartPython() to use updated packages.

# Import Library
Library is a collection of pre-written code that you can use to perform common tasks without having to write the code from scratch.They are built-in and are used by importing them with the import statement.

# Pandas are for data analysis, manupulation and  working with tables/excel sheets (DataFrames).
import pandas as pd 

# Numpy is for numerical operations or math functions.
import numpy as np

# Matplotlib to create viewership visualizations, 
import matplotlib.pyplot as plt

# Data Import

# location of data
data_path="/Workspace/Users/tkndlovu111@gmail.com/Class Projects/Viewer_ Analysis_ Ex.xlsx"

# read excel file
df = pd.read_excel(data_path)
display(df)

# To see your dataframe
display(df)

# Show last 5 rows.
df.tail(5)

# Summary of DataFrame (columns, types, nulls).
df.info()

# number of rows, columns
df.shape

# Data types of columns.
df.dtypes

# Select a column.
# df['column']
df["VideoTitle"]

# Select multiple columns.
# df[["Col1", "Col2"]]
df[['Platform', 'PlayEventType']]

# Get unique values in a column (Platform)
df['Platform'].unique()

# Get unique values in a column (PlayEventType)
df['PlayEventType'].unique()

# Maximum value in the column (TotalTimeWatched)
df['TotalTimeWatched'].max()

# Minimum value in the column (TotalTimeWatched)
df['TotalTimeWatched'].min()

# Check if any row is duplicated
df.duplicated().sum()

# Remove duplicates from the whole DataFrame
df.drop_duplicates(inplace=True)
df.duplicated().sum()

# check missing values
df.isnull().sum()



