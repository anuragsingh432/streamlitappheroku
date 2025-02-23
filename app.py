#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:45:58 2025

@author: anuragsingh
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu




#loading the saved models

diabetes_model=pickle.load(open('/Users/anuragsingh/Desktop/multiple/savedmodels/diabetes_model.sav','rb'))
parkinsons_model=pickle.load(open('/Users/anuragsingh/Desktop/multiple/savedmodels//parkinsons_model.sav','rb'))
heart_diseases_model=pickle.load(open('/Users/anuragsingh/Desktop/multiple/savedmodels/heart_diseases_model.sav','rb'))

#for sidemenu bar

with st.sidebar:
    
    selected = option_menu(
     menu_title="Multiple Diseases Prediction System",  # Title for sidebar
     options=['Diabetes Prediction','Parkinson Prediction','Heart Diseases Prediction'],
     icons=['activity','heart','person'],
     default_index=0
 )
    
#now prediction page

if(selected=='Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = float(st.text_input('Number of Pregnancies', "0"))
    with col2:
        Glucose = float(st.text_input('Glucose Level', "0"))
    with col3:
        BloodPressure = float(st.text_input('Blood Pressure Value', "0"))
    with col1:
        SkinThickness = float(st.text_input('Skin Thickness Value', "0"))
    with col2:
        Insulin = float(st.text_input('Insulin Level', "0"))
    with col3:
        BMI = float(st.text_input('BMI Value', "0"))
    with col1:
        DiabetesPedigreeFunction = float(st.text_input('Diabetes Pedigree Function Value', "0"))
    with col2:
        Age = float(st.text_input('Age of the Person', "0"))

    diab_diagnosis = ''

    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is Diabetic"
        else:
            diab_diagnosis = "The person is Non-Diabetic"

        st.success(diab_diagnosis)

# Parkinson Prediction Page
elif selected == 'Parkinson Prediction':
    st.title('Parkinson Prediction using ML')
    
    
    
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        fho = (st.text_input('MDVP:Fo(Hz)', "0"))
    with col2:
        fi= float(st.text_input('MDVP:Fhi(Hz)', "0"))
    with col3:
        flo = float(st.text_input('MDVP:Flo(Hz)', "0"))
    with col4:
        Jitter_percent = float(st.text_input('MDVP:Jitter(%)', "0"))
    with col5:
        Jitter_Abs = float(st.text_input('MDVP:Jitter(Abs)', "0"))
    with col1:
        RAP = float(st.text_input('MDVP:RAP', "0"))
    with col2:
        PPQ = float(st.text_input('MDVP:PPQ', "0"))
    with col3:
        DDP = float(st.text_input('Jitter:DDP', "0"))
    with col4:
        Shimmer = float(st.text_input('MDVP:Shimmer', "0"))  # ✅ Fixed issue
    with col5:
         Shimmer_dB = float(st.text_input('MDVP:Shimmer(dB)', "0"))  # ✅ Fixed issue    
    with col1:
        APQ3 = float(st.text_input('Shimmer:APQ3', "0"))
    with col2:
        APQ5 = float(st.text_input('Shimmer:APQ5', "0"))
    with col3:
        APQ = float(st.text_input('MDVP:APQ', "0"))
    with col4:
        DDA = float(st.text_input('Shimmer:DDA', "0"))  # ✅ Fixed incorrect reference
    with col5:
        NHR = float(st.text_input('NHR', "0"))
    with col1:
        HNR = (st.text_input('HNR', "0"))
    with col2:
        RPDE = float(st.text_input('RPDE', "0"))
    with col3:
        DFA = float(st.text_input('DFA', "0"))
    with col4:
        spread1 = float(st.text_input('spread1', "0"))
    with col5:
        spread2 = float(st.text_input('spread2', "0"))    
    with col1:
         D2 = float(st.text_input('D2', "0"))
    with col2:
         PPE = float(st.text_input('PPE', "0"))
    parkinsons_diagnosis = ''

    if st.button("Parkinson's Prediction Result"):
        parkinsons_prediction =  parkinsons_model.predict([[fho,fi,flo,Jitter_percent,Jitter_Abs,RAP,PPQ,DDA,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has parkinsons disease"
        else:
            parkinsons_diagnosis = "The person does not have parkinsons disease"

        st.success(parkinsons_diagnosis)
    
    
    
    
    
    
    
    

# Heart Diseases Prediction Page
elif selected == 'Heart Diseases Prediction':
    st.title('Heart Diseases Prediction using ML')

    col1,col2,col3 = st.columns(3)

    with col1:
        Age = (st.text_input('Age', "0"))
    with col2:
        Sex = float(st.text_input('Sex', "0"))
    with col3:
        cp = float(st.text_input('Chest Pain types', "0"))
    with col1:
        tresbps = float(st.text_input('Resting Blood Pressure', "0"))
    with col2:
        chol = float(st.text_input('Serum Cholesterol in mg/dl', "0"))
    with col3:
        BMI = float(st.text_input('BMI Value', "0"))
    with col1:
        fbs = float(st.text_input('Fasting Blood Sugar > 120 mg/dl', "0"))
    with col2:
        thalac = float(st.text_input('Maximum Heart Rate Achieved', "0"))
    with col3:
        exang = float(st.text_input('Exercise Induced Angina', "0"))  # ✅ Fixed issue
    with col1:
        oldpeak = float(st.text_input('Depression induced by exercise', "0"))
    with col2:
        slope = float(st.text_input('Slope of peak exercise segment', "0"))
    with col3:
        ca = float(st.text_input('Major vessels colored by Fluoroscopy', "0"))
    with col1:
        restecg = float(st.text_input('Resting Electrocardiograph Results', "0"))  # ✅ Fixed incorrect reference
    with col2:
        thal = float(st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defects', "0"))

    heart_diagnosis = ''

    if st.button("Heart Diseases Prediction Result"):
        heart_prediction = heart_diseases_model.predict([[Age, Sex, cp, tresbps, chol, BMI, fbs, thalac, exang, oldpeak, slope, ca, restecg, thal]])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = "The person has heart disease"
        else:
            heart_diagnosis = "The person does not have heart disease"

        st.success(heart_diagnosis)
    
    
    
    
    
    
    
    
    
    
    
    
    
    