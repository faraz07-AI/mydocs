import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('pickel_model.pkl','rb') as file:
          data=pickle.load(file)
    return data

data =load_model()


regressor =data["model"]

def show_predict_page():
    st.title("Covid19 infection Prediction ")
     
    st.write("""we need some information to predict the covid19 possibility for you """) 

    bodypains_1 ={
       "yes",
       "No",

    }
    runnyNose_1 ={
      "yes",
      "No"

    }

    diffBreath_1={
        "yes",
        "no"
    }

    fever=st.slider("temperature of your body",0,110,99)
    body1=st.selectbox("body pain",bodypains_1)
    if body1=="Yes":
         bodyPain=1
    else: 
        bodyPain=0

    age=st.slider("your age",0,150,6)

    runningnose1=st.selectbox("Running nose(Cold)",runnyNose_1)
    if runningnose1=="Yes":
        runnyNose=1
    else: 
        runnyNose=0
    diffbreath1=st.selectbox("difficulty in breathing",diffBreath_1)
    if diffbreath1=="Yes":
        diffBreath=1
    else: 
        diffBreath=0    
    clicked=st.button("kown the probability of infection") 
    if clicked:
        x=np.array([[fever,bodyPain,age,runnyNose,diffBreath]])
        x
        y_pred=regressor.predict(x)
        st.subheader(f"the probability of covid infection id {y_pred*100}")
