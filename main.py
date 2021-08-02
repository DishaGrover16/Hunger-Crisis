from google.protobuf.reflection import GeneratedProtocolMessageType
import numpy as np
import pandas as pd
import sklearn 
import streamlit as st
from sklearn.svm import SVR

st.title('Hunger Crisis')
st.sidebar.subheader('Input Feature')
df=pd.read_csv("data/preprocessed_data.csv")
X=df[['Gender', 'Age', 'Weight', 'Height','Diseases']].values
y_rice=df['rice'].values
y_vegetables=df['vegetables'].values
y_burgers=df['burgers'].values
y_pizza=df['pizza'].values
y_beverages=df['beverages'].values
y_meat=df['meat'].values
y_sea_food=df['sea_food'].values
st.sidebar.text("Fill your details here")
ipt=[]
ipt.append(st.sidebar.radio("Gender",["Male","Female"]))
ipt.append(st.sidebar.slider("Age", 1,100,20))
ipt.append(st.sidebar.number_input("Height in cm"))
ipt.append(st.sidebar.number_input("Weight in kg"))
ipt.append(st.sidebar.selectbox("Do you have any health issues?",('None', 'Diabetes', 'Acidity', 'High Cholestrol','Increased Uric Acid','Hypertension')))
st.header("Please enter your order below")
order=st.selectbox("What do you want to order?",('Rice', 'Vegetables','Pizza','Burgers','Beverages','Meat','Sea Food'))
if ipt[0]=='Male':
    ipt[0]=1
if ipt[0]=='Female':
    ipt[0]=0
if ipt[4]=='None':
    ipt[4]=0
if ipt[4]=='Diabetes':
    ipt[4]=1
if ipt[4]=='High Cholestrol':
    ipt[4]=2
if ipt[4]=='Acidity':
    ipt[4]=3
if ipt[4]=='Hypertension':
    ipt[4]=4
if ipt[4]=='Increased Uric Acid':
    ipt[4]=5

#try:
regressor=SVR(kernel='rbf')
if order=='Rice':
    regressor.fit(X, y_rice)
if order=='Vegetables':
    regressor.fit(X, y_vegetables)
if order=='Burgers':
    regressor.fit(X, y_burgers)
if order=='Pizza':
    regressor.fit(X, y_pizza)  
if order=='Beverages':
    regressor.fit(X, y_beverages)
if order=='Meat':
    regressor.fit(X, y_meat)
if order=='Sea Food':
    regressor.fit(X, y_sea_food)  
if st.button('Predict'):
    #st.write(ipt)
    result=int(regressor.predict([ipt]))
    st.info(f'You are advised to order "{result}" servings of this food')
#except:
    #st.error('Sum unexpected error has ocurred. Please try again.')
