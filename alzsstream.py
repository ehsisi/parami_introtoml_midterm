import streamlit as st
import pickle
import os
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Alzheimer's Prediction System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# sidebar
with st.sidebar:
    st.markdown("ALZHEIMER'S PREDICTION SYSTEM")
    st.markdown("---")

    # navigation menu
    selected = st.selectbox(
        "Navigate to:",
        ["Home", "Predict Alzheimer's"]
    )
    st.markdown("---")

    # Disclaimer (always visible in sidebar)
    st.markdown("### ⚠️ Disclaimer")
    st.markdown("""
                The predictions provided by this system are for informational purposes only.
                Consult a healthcare professional for accurate diagnosis and advice.
                """)
    
    st.markdown("---")

    # Student info in sidebar
    st.markdown("Student Info")
    st.write("Student Name: Eh Si Si")
    st.write("Student ID: PIUS20220018")

# Load model
# model = pickle.load('alz.pkl')
st.title("🧠 Alzheimer's Disease Prediction")
# st.caption(f"Model loaded: `{type(model)}`")

# Helper function to convert categorical to numerical
def convert_binary(value):
    if isinstance(value, str):
        value = value.upper()
        
        if value == 'YES' or value == 'M':
            return 1
        elif value == 'NO' or value == 'F':
            return 0
        
# Education mapping
def convert_education(value):
    mapping = {
        "NO FORMAL EDUCATION": 0,
        "HIGH SCHOOL": 1,
        "BACHELOR DEGREE": 2,
        "HIGHER DEGREES": 3
    }
    return mapping[value.upper()]

# Quality scale mapping
def convert_quality(value):
    value = value.upper()

    if value == "TERRIBLE":
        return 0
    elif value == "POOR":
        return np.random.randint(1, 3)
    elif value == "FAIR":
        return np.random.randint(4, 6)
    elif value == "GOOD":
        return np.random.randint(7, 9)
    elif value == "EXCELLENT":
        return 10
    else:
        return None

def load_model():
    with open("model1.pkl", "rb") as f:
        model = pickle.load(f)
    return model

# Main content
# Home Page
if selected == "Home":
    st.title("Introduction to Alzheimer's Disease")

    # Content
    st.markdown("""
                Alzheimer's disease (AD) is a progressive neurodegenerative disease.
                
                **Though best known for its role in declining memory functions, symptoms also include:**
                - Difficulty thinking and reasoning
                - Making judgements and decisions
                - Planning and performing familiar tasks
                
                It may also cause alterations in personality and behavior.
                
                The cause of AD is not well understood. Through this model, it is expected that one can predict the occurence of AD.)
                """)
    
    # Add some spacing
    st.markdown("---")

    # Preparations before the Prediction
    st.title("Preparations Before the Prediction")

    # Content

    st.markdown("""
                Before taking the test, there are pre-test that should be taken.
                - To calculate the BMI, it is suggested to visit the following website.

                https://www.yazio.com/en/bmi-calculator?utm_source=google&utm_medium=gads&utm_campaign=22055484152&utm_content=178242375332&utm_term=bmi%20calculator&gad_source=1&gad_campaignid=22055484152&gbraid=0AAAAAoNfjafMQfPH8vne3267mS_ju8_Gu&gclid=Cj0KCQiA6NTJBhDEARIsAB7QHD0AwMyTw1NmdfnP0x2RFpJ-kFeLKGVE-robR6pry2qn0odMD_XKsdgaAsAHEALw_wcB

                - To calculate the Weekly Alcohol Consumption Unit, it is suggested to visit the following website.
                
                https://www.nhs.uk/live-well/alcohol-advice/calculating-alcohol-units/

                - To calculate the Diet Quality Score, it is suggested to visit the following website.
                
                https://www.dietquality.org/calculator

                - To calculate the Systolic Blood Pressure and Diastolic Blood Pressure, 
                
                it is suggested to use a Sphygmomanomter.

                - To calculate the Total, LDL, HDL, and triglycerides level of Cholesterol, 
                
                it is suggested to either measure with Eelctronic Meter Kits for Cholesterol or measure at the Laboratory.

                - To calculate the Mini Mental State Examination Score, it is suggested to visit the following website.
                
                https://mmse.neurol.ru/

                - To calculate the Activities of Daily Living (ADL), it is suggested to visit the following website.
                
                https://www.mdcalc.com/calc/3912/barthel-index-activities-daily-living-adl
                """)

# Input form


# Create the form with sections
with st.form("prediction_form"):

    # Section 1 - Demographic Details
    st.markdown("### Demographic Details")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=150, value=None, placeholder="Enter age") # I want blank and no initial value
        gender = st.selectbox("Gender", ["", 'M', 'F'], index=0)

    with col2:
        educ = st.selectbox("EducationLevel", ["", 'No Formal Education', 'High School', 'Bachelor Degree', 'Higher Degrees'], index=0)

    st.markdown("---")

    # Section 2 - Lifestyle Factors
    st.markdown("### Lifestyle Factors")
    col3, col4 = st.columns(2)

    with col3:
        bmi = st.number_input("BMI*", min_value=10, max_value=50, value=None, placeholder="10.0 - 50.0")
        smoking = st.selectbox("Smoking", ["", 'Yes', 'No'], index=0)
        alcohol = st.number_input("Weekly Alchohol Consumption Unit*", min_value=0, max_value=30, value=None, placeholder="0 - 30")
    
    with col4:
        physical = st.selectbox("Weekly Physical Activity Quality",  ["", 'Terrible', 'Poor', 'Fair', 'Good', 'Excellent'], index=0)
        diet = st.number_input("Diet Quality Score*", min_value=0, max_value=30, value=None, placeholder="0 - 30")
        sleep = st.selectbox("Sleep Quality",  ["", 'Terrible', 'Poor', 'Fair', 'Good', 'Excellent'], index=0)
    
    st.markdown("---")

    # Section 3 - Medical History
    st.markdown("### Medical History")
    col5, col6 = st.columns(2)

    with col5:
        history = st.selectbox("Family History", ["", 'Yes', 'No'], index=0)
        cardio = st.selectbox("Cardiovascular Disease", ["", 'Yes', 'No'], index=0)
        diabetes = st.selectbox("Diabetes", ["", 'Yes', 'No'], index=0)
    
    with col6:
        depression = st.selectbox("Depression", ["", 'Yes', 'No'], index=0)
        head = st.selectbox("Head Injury", ["", 'Yes', 'No'], index=0)
        hypertension = st.selectbox("Hypertension", ["", 'Yes', 'No'], index=0)
    
    st.markdown("---")

    # Section 4 - Clinical Measurements
    st.markdown("### Clinical Measurements")
    col7, col8 = st.columns(2)

    with col7:
        systolic = st.number_input("Systolic Blood Pressure*", min_value=40, max_value=200, value=None, placeholder="40 - 200")
        diastolic = st.number_input("Diastolic Blood Pressure*", min_value=10, max_value=180, value=None, placeholder="10 - 180")
        cholesteroltotal = st.number_input("Cholesterol Total*", min_value=100, max_value=300, value=None, placeholder="100 - 300")
        
    with col8:
        cholesterolldl = st.number_input("Cholesterol LDL*", min_value=40, max_value=200, value=None, placeholder="40 - 200")
        cholesterolhdl = st.number_input("Cholesterol HDL*", min_value=10, max_value=120, value=None, placeholder="10 - 120")
        cholesteroltri = st.number_input("Cholesterol Triglycerides*", min_value=40, max_value=450, value=None, placeholder="40 - 450")
    
    st.markdown("---")

    # Section 5 - Cognitive and Functional Assessments
    st.markdown("### Cognitive & Functional Assessments")
    col9, col10 = st.columns(2)

    with col9:
        mmse = st.number_input("Mini Mental State Examination Score", min_value=0, max_value=30, value=None, placeholder="0 - 30")
        functassess = st.selectbox("FunctionalAssessment",  ["", 'Terrible', 'Poor', 'Fair', 'Good', 'Excellent'], index=0)
        memory = st.selectbox("Memory Complaints", ["", 'Yes', 'No'], index=0)
    
    with col10:
        behavior = st.selectbox("Behavioral Problems", ["", 'Yes', 'No'], index=0)
        adl = st.number_input("Activities of Daily Living Score*", min_value=0, max_value=10, value=None, placeholder="0 - 10")
    
    st.markdown("---")

    # Section 6 - Symptoms
    st.markdown("### Symptoms")
    col11, col12 = st.columns(2)

    with col11:    
        confusion = st.selectbox("Confusion", ["", 'Yes', 'No'], index=0)
        disorientation = st.selectbox("Disorientation", ["", 'Yes', 'No'], index=0)
        personality = st.selectbox("Personality Changes", ["", 'Yes', 'No'], index=0)
    
    with col12:
        completetasks = st.selectbox("Difficultiy in Completing Tasks", ["", 'Yes', 'No'], index=0)
        forgetful = st.selectbox("Forgetfulness", ["", 'Yes', 'No'], index=0)

    st.markdown("---")

    submitted = st.form_submit_button("🔍 Predict")



if submitted:
    # Convert all categorical values to numerical 
    gender_num = convert_binary(gender)
    educ_num = convert_education(educ)
    smoking_num = convert_binary(smoking)
    physical_num = convert_quality(physical)
    sleep_num = convert_quality(sleep)
    history_num = convert_binary(history)
    cardio_num = convert_binary(cardio)
    diabetes_num = convert_binary(diabetes)
    depression_num = convert_binary(depression)
    head_num = convert_binary(head)
    hypertension_num = convert_binary(hypertension)
    functassess_num = convert_quality(functassess)
    memory_num = convert_binary(memory)
    behavior_num = convert_binary(behavior)
    confusion_num = convert_binary(confusion)
    disorientation_num = convert_binary(disorientation)
    personality_num = convert_binary(personality)
    completetasks_num = convert_binary(completetasks)
    forgetful_num = convert_binary(forgetful)

    # Prepare input data
    input_data = pd.DataFrame({
        'Gender': [gender_num],
        'Age': [age],
        'EducationLevel': [educ_num],
        'BMI': [bmi],
        'Smoking': [smoking_num],
        'AlcoholConsumption': [alcohol],
        'PhysicalActivity': [physical_num],
        'DietQuality': [diet],
        'SleepQuality': [sleep_num],
        'FamilyHistoryAlzheimers': [history_num],
        'CardiovascularDisease': [cardio_num],
        'Diabetes': [diabetes_num],
        'Depression': [depression_num],
        'HeadInjury': [head_num],
        'Hypertension': [hypertension_num],
        'SystolicBP': [systolic],
        'DiastolicBP': [diastolic],
        'CholesterolTotal': [cholesteroltotal],
        'CholesterolLDL': [cholesterolldl],
        'CholesterolHDL': [cholesterolhdl],
        'CholesterolTriglycerides': [cholesteroltri],
        'MMSE': [mmse],
        'FunctionalAssessment': [functassess_num],
        'MemoryComplaints': [memory_num],
        'BehavioralProblems': [behavior_num],
        'ADL': [adl],
        'Confusion': [confusion_num],
        'Disorientation':[disorientation_num],
        'PersonalityChanges': [personality_num],
        'DifficultyCompletingTasks': [completetasks_num],
        'Forgetfulness': [forgetful_num]
    })
    
    model=load_model()
    result=model.predict(input_data)

    # Display result
    st.markdown("---")
    st.subheader("Prediction Result")
    
    if result[0] == 1:
        st.success(f"🔴 **Prediction: Positive for Alzheimer's Disease**")
        st.warning("Please consult a healthcare professional for further evaluation.")
    else:
        st.error(f"🟢 **Prediction: Negative for Alzheimer's Disease**")
        st.info("Continue with regular check-ups and healthy lifestyle.")






