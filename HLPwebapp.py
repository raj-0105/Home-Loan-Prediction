import pickle
import streamlit as st
import math

with open("D:/vs code/python/model_RF.pkl",'rb') as f:
  mp=pickle.load(f)

from PIL import Image
img = Image.open("F:/pythonp/importance.png")

def prediction(ch,loan_req,app_in,coapp_in,term,gender,married,dependents,educ,employ,prop_area):
    ls=[0.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if ch=="Repaid Debts":
        ls[0]=1.0

    ls[1]=math.log(loan_req)
    ls[2]=app_in+coapp_in
    ls[3]=math.log(ls[2])
    ls[4]=loan_req/term
    ls[5]=ls[2]-ls[4]*1000
    if gender=="Female":
        ls[6]=1
    elif gender=="Male":
        ls[7]=1

    if married=="No":
        ls[8]=1
    else:
        ls[9]=1

    if dependents=="three or more":
        ls[10]=1
    elif  dependents=="zero":
        ls[11]=1
    elif  dependents=="one":
        ls[12]=1                   
    elif  dependents=="two":
        ls[13]=1

    if educ=="Graduate":
        ls[14]=1
    else:
        ls[15]=1

    if employ=="No":
        ls[16]=1
    else:
        ls[17]=1
    if prop_area=="Rural":
        ls[18]=1
    elif prop_area=="Semi Urban":
        ls[19]=1                       
    elif prop_area=="Urban":
        ls[20]=1 
    
    pred=mp.predict([ls])
    if pred==1:
        st.success("ELIGIBLE")
    else:
        st.success("NOT ELIGIBLE")        


st.title("Home Loan Prediction Using Machine Learning")
st.image(img,"IMPORTANCE GRAPH ", width=800)
ch=st.selectbox("Credit_History",["Repaid Debts","Not Repaid Debts"])

loan_req=st.number_input("Enter Required Loan Amount in Lakhs")

app_in=st.number_input("Enter Applicant's Income")
app_in=app_in/10
coapp_in=st.number_input("Enter Co-Applicant's Income")
coapp_in=coapp_in/10
term=st.number_input("Enter Loan Amount term in Months")
gender=st.selectbox("Gender",["Male","Female"])
married=st.selectbox("Married",["Yes","No"])
dependents=st.selectbox("Dependents",["zero","one","two","three or more"])
educ=st.selectbox("Education",["Graduate","Not Graduate"])
employ=st.selectbox("Self Employed",["Yes","No"])
prop_area=st.selectbox("Property Area",["Urban","Semi Urban","Rural"])

if st.button("Predict"):
    prediction(ch,loan_req,app_in,coapp_in,term,gender,married,dependents,educ,employ,prop_area)