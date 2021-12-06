import steamlit as st
import numpy as np
import pickle
import Covid19_Prediction_


def load_model():
    pickle.dump(dec_tree,open('pickel_model (1).pkl','wb'))
    model=pickle.load(open('pickel_model (1).pkl','rb'))
    return model

model =load_model()

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
        "yes"
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
    diffbreath1=st.selectbox("Running nose(Cold)",diffBreath_1)
    if diffbreath1=="Yes":
        diffBreath=1 
    else: 
        diffBreath=0    
    clicked=st.button("kown the probability of infection") 
    if clicked:
        x=np.array([[fever,bodyPain,age,runnyNose,diffBreath]])
        x
        y_pred = clflo.predict_proba(x)
        y_pred

    fin=y_pred[0]
    st.subheader(f"the estimated probabity is {fin*100}")