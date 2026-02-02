
import pandas as pd
import numpy as np
import os
os.getcwd()
dataset=pd.read_csv("C:/Users/Amruta more/finalproject/dataset.csv")
df=dataset.to_csv("cleaned_data.csv",index=False)
df=dataset.sample(n=10000,random_state=123)
print(df)
df.head()
print(df.head())
df.info()
print(df.info())
print(df.describe())
print(df.isna().any().any())
print(df.isna().sum())
unique_values1=df['Education_Level'].unique()
print(unique_values1)
unique_values2=df['Employment_Status'].unique()
print(unique_values2)
count_unique=df['Employment_Status'].value_counts()
print(count_unique)
