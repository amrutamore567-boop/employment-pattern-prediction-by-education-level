import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:/Users/Amruta more/finalproject/cleaned_data.csv")
print("\nDatset Structure:")
df.info()
gpa = df['GPA']
age=df['Age']

print("\nGPA statistics:")
print("Mean:",gpa.mean())
print("Median:",gpa.mean())
print("Stdv Dev:",gpa.std())
print("Variance:",gpa.var())
print("Quartile:\n",gpa.quantile([0.25,0.5,0.75]))

print("\nAge statistics:")
print("Mean:",age.mean())
print("Median:",age.median())
print("Std Dev",age.std())
print("Variance:",age.var())
print("Quartiles\n",gpa.quantile([0.25,0.5,0.75]))

print("\nColumn Names:")
print(df.columns)
print("\nEmployemennt Status Frequency:")
print(df['Employment_Status'].value_counts())

def get_mode(series):
    return series.value_counts().idxmax()

print("\nMode of Employment_Status:", get_mode(df['Employment_Status']))
print("Mode of Education_Level:",get_mode(df['Education_Level']))

print("\nEmpployment Status Distribution (%):")
print(df["Employment_Status"].value_counts(normalize=True)*100)

#visualization

# Education Level vs Employment Status
plt.figure()
sns.countplot(
    data=df,
    x='Education_Level',
    hue='Employment_Status'
)
plt.title("Education Level vs Employment Status")
plt.xlabel("Education Level")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Internship Experience vs Employment Status
plt.figure()
sns.countplot(
    data=df,
    x='Internship_Experience',
    hue='Employment_Status'
)
plt.title("Internship Experience vs Employment Status")
plt.xlabel("Internship Experience")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# GPA vs Employment Status (Boxplot)
plt.figure()
sns.boxplot(
    data=df,
    x='Employment_Status',
    y='GPA'
)
plt.title("GPA vs Employment Status")
plt.xlabel("Employment Status")
plt.ylabel("GPA")
plt.tight_layout()
plt.show()

# Age vs Employment Status (Boxplot)
plt.figure()
sns.boxplot(
    data=df,
    x='Employment_Status',
    y='Age'
)
plt.title("Age vs Employment Status")
plt.xlabel("Employment Status")
plt.ylabel("Age")
plt.tight_layout()
plt.show()

# Region of Study vs Employment Status
plt.figure()
sns.countplot(
    data=df,
    x='Region_of_Study',
    hue='Employment_Status'
)
plt.title("Region of Study vs Employment Status")
plt.xlabel("Region of Study")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()