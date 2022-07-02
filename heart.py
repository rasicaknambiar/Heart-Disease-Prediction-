import streamlit as st
import pandas as pd
import pickle
st.write("""# Heart Disease  Prediction App
""")
#st.balloons()

heartdiseaseclassifier = open('heart_prediction.pkl', 'rb')
classifier = pickle.load(heartdiseaseclassifier)

# Text Input
Age = st.text_input("Enter the age (in years)",)
Sex = st.text_input("Enter the sex (1 = male; 0 = female) ",)
CP = st.text_input("Enter the Chest pain type(0= asymptomatic; 1=atypical angina; 2= non-anginal pain; 3= typical angina)",)
trestps = st.text_input("Enter the trestbps: resting blood pressure (in mm Hg on admission to the hospital(80-120)",)
Chol = st.text_input("Enter the serum cholestoral in mg/dl (serum cholestoral in mg/dl (126-564))",)
Fbs = st.text_input("Enter the fasting blood sugar &gt; >120 mg/dl (1 = true; 0 = false)" ,)
restecg = st.text_input("Enter the resting electrocardiographic results (0= normal; 1= having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV); 2= showing probable or definite left ventricular hypertrophy by Estes' criteria )",)
Thalach = st.text_input("Enter the thalachmaximum heart rate achieved(50-100)",)
Exang = st.text_input("Enter the exangexercise induced angina (1 = yes; 0 = no)",)
Oldpeak = st.text_input("Enter the oldpeakST depression induced by exercise relative to rest(0-6)",)

slop = st.text_input("Enter the the slope of the peak exercise ST segment(1-upsloping,2-flat,3-downsloping ",)
Ca = st.text_input("Enter the ca number of major vessels (0-3) colored by flourosopy trestbps: resting blood pressure (in mm Hg on admission to the hospital)",)
thal = st.text_input("Enter the thal:  1 = normal; 2 = fixed defect; 3 = reversable defect )",)
#target: 1 = disease, 0 = no disease



submit = st.button('Classify')

if submit:
	with st.spinner("Classifying.."):
        	result = classifier.predict([[Age, Sex, CP, trestps, Chol,Fbs, restecg, Thalach, Exang, Oldpeak, slop, Ca, thal]])
	#st.write(result)
	if result == 0:
		st.write("no heart disease")
	else:
		st.write("heart disease")		
		
       		
 
