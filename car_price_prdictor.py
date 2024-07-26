import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,accuracy_score
from sklearn.compose import ColumnTransformer,make_column_transformer
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier
from sklearn.linear_model import LinearRegression
import streamlit as st 
car= pd.read_csv(r"C:\Users\krish\OneDrive\Desktop\ok\quikr_car.csv")
backup= car

car = car[car['year'].str.isnumeric()]
car['year']= car['year'].astype(int)
car['Price'] = car['Price'].str.replace(',','')
car = car[car['Price']!= "Ask For Price"]
car['Price'] = car['Price'].astype(int)
car['kms_driven'] =car['kms_driven'].str.split(' ').str.get(0).str.replace(',','')
car = car[car['kms_driven'].str.isnumeric()]
car['kms_driven'] = car['kms_driven'].astype(int)
car = car[~car['fuel_type'].isna()]
car['name'] = car['name'].str.split(' ').str.slice(0,3).str.join(' ')
car = car.reset_index(drop=True)

#  model building

x =car[['name','company','year','kms_driven','fuel_type']]
y = car['Price']
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=247)


ohe =OneHotEncoder()
ohe.fit(x[['name','company','fuel_type']])
column_trans=make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name','company','fuel_type']),
                                    remainder='passthrough')
lr= LinearRegression()
pipe=make_pipeline(column_trans,lr)
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)

st.title("Car Price Predictor")
st.header("Training dataset")
st.write(car)

st.subheader("Visualisation")
st.subheader("Price:")
st.bar_chart(car['Price'])
st.subheader("kilometers driven")
st.bar_chart(car['kms_driven'])
st.subheader("year")
st.bar_chart(car['year'])
st.balloons()

st.sidebar.title("Enter your input")
def user_input():
    name = st.sidebar.text_input("enter the name","Mahindra Jeep CL550",key="placeholder")
    company = st.sidebar.radio("Enter the company name",options=['Hyundai', 'Mahindra' ,'Ford', 'Maruti', 'Skoda', 'Audi', 'Toyota', 'Renault',
 'Honda', 'Datsun', 'Mitsubishi', 'Tata', 'Volkswagen', 'Chevrolet', 'Mini',
 'BMW' ,'Nissan' ,'Hindustan' ,'Fiat', 'Force', 'Mercedes', 'Land' ,'Jaguar',
 'Jeep', 'Volvo',])
    year = st.sidebar.radio("enter the year",options=['1995','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])
    kms_driven = st.sidebar.slider('kms driven',0,500000,400)
    fuel_type = st.sidebar.radio("enter the fuel type",options=['Petrol','Diesel'])

    user_data ={
        'name' : name,
        'company' : company,
        'year' : year,
        'kms_driven' : kms_driven,
        'fuel_type' : fuel_type
    }
    report_data = pd.DataFrame(user_data,index=[0])
    return report_data

user_data = user_input()


st.subheader("The price of the car will be:")
result = pipe.predict(user_data)
print(result)
st.write(result)