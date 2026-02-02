import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.model_selection
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report
df=pd.read_csv("C:/Users/Amruta more/finalproject/cleaned_data.csv")
cat_cols= ['Country_of_Origin','Education_Level','Internship_Experience','Region_of_Study','Employment_Status','University_Ranking']
for col in cat_cols:df[col] =LabelEncoder().fit_transform(df[col].astype(str))
x=df[['Education_Level','Internship_Experience','Region_of_Study','Age','GPA','University_Ranking']]
y=df['Employment_Status']

#train, test split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)

model=LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Logistic Regression Accuracy:",
      accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

y_prob=model.predict_proba(x_test)
employement_precentage=y_prob[:,1]*100
unemployement_precentage=y_prob[:,0]*100

for i in range(5):
    print(f"Employed Probability:{employement_precentage[i]:.2f}%")
    print(f"UnEmployed Probability:{unemployement_precentage[i]:.2f}%")
print("-"*30)