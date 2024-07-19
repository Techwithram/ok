import numpy as np
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score 
from sklearn.ensemble import RandomForestClassifier
dia_dataset= pd.read_csv("C:\\Users\\krish\\Downloads\\diabetes.csv")
st.title("Diabetes Checkup")

st.subheader("Training Data")
st.sidebar.header("Patient Data")
st.write(dia_dataset.describe())

st.subheader("Visualisation")
st.bar_chart(dia_dataset)

x = dia_dataset.drop(columns= 'Outcome',axis=1)
y = dia_dataset['Outcome']

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2,random_state=2)

def user_input():
  pregancies = st.sidebar.slider('pregancies', 0,17,2)
  glucose = st.sidebar.slider('glucose',0,200,120)
  bp = st.sidebar.slider('blood presure',0,122,75)
  skinthickness = st.sidebar.slider('skin thickness',0,100,65)
  insulin = st.sidebar.slider('insulin',0,100,20)
  bmi = st.sidebar.slider('bmi',0,900,83)
  dpf = st.sidebar.slider('Diabetes pedigree function',0.0,2.4,0.67)
  age = st.sidebar.slider('Age',0,100,30)

  user_report = {
    'Pregnancies': pregancies,
    'Glucose': glucose,
    'BloodPressure': bp,
    'SkinThickness': skinthickness,
    'Insulin': insulin,
    'BMI': bmi,
    'DiabetesPedigreeFunction': dpf,
    'Age': age
  }
  report_data = pd.DataFrame(user_report,index=[0])
  return report_data

user_data = user_input()



rf= RandomForestClassifier()
rf.fit(X_train,Y_train)


user_result = rf.predict(user_data)

st.subheader("Your report")
output=""
if user_result[0] == 0:
  output ="You are absolutely healthy"
else: 
  output =" you are not healthy"

st.write(output)
print("ok")