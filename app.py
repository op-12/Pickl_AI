import streamlit as st
import pandas as pd
import joblib

rfc_1 = joblib.load('rfc.joblib')
svm_1 = joblib.load('svm_pipeline.joblib')



st.set_page_config(page_title = "LoanAlchemist🔍",
                   page_icon = "🧪")
st.title("Personalized Lending for the Digital Age 📱 [Enter the details below]")
st.divider()

model_selected = st.selectbox("Select hyperparameter tuned model", ["rfc", "svm"])
pin = st.select_slider("Enter Pin Code", [110001, 110014, 110003, 110004, 110011])
age = st.slider("Enter Age🧓👶", 21, 65, value=64)
Fam = st.select_slider("Enter Number of members in your family", [1, 2, 3, 4])
education = st.selectbox("Enter your education 📚", ["Under Graduate", "Graduate", "Post Graduate"])
experience = st.slider("Enter Experience", 0, 43)
income = st.slider("Enter Income", 64000, 1792000)
Mortgage = st.slider('Enter Mortgage', 0, 5080000)
Fixed_deposit = st.select_slider("f_deez", ['yes', 'no'])
demat = st.select_slider('Do you have a demat account', ["yes", "no"])
net_banking = st.select_slider('Do you use net_banking', ["yes", "no"])


def predict():
    sample_data = pd.DataFrame([{
        'Pin-code': int(pin),
        'age': int(age), 
        'Fam members': int(Fam),
        'Education': str(education),
        'T.Experience':int(experience),
        'Income': int(income),
        'Mortgage': int(Mortgage),
        'Fixed Deposit': str(Fixed_deposit),
        'Demat': str(demat),
        'Net Banking': str(net_banking)
    }])
    
   
    sample_data = sample_data[['Pin-code', 'age', 'Fam members', 'Education', 'T.Experience', 'Income', 'Mortgage', 'Fixed Deposit', 'Demat', 'Net Banking']]
    
    
    if model_selected == 'rfc':
            model = rfc_1
            
    else:
            model = svm_1


            
    predictions = model.predict(sample_data)
    if predictions[0] == 'yes':
        st.balloons()
        st.success("Congratulation!!! YOur loAn WIll be AcCepTed 🎉🎊🥳")
    else:
        st.error("Sorry!!! Your loan will rejected ⚠️😔😔")

trigger = st.button("Predict 🪄", on_click=predict)