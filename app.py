import joblib
import pandas as pd
import os
import streamlit as st
from huggingface_hub import hf_hub_download



#PAGE CONFIGURATION

st.set_page_config(
    page_title="Health Status Prediction",
     layout="wide"
)

#================================================================== IMPORTANT FUNCTIONS ====================================================================================
HF_REPO_ID = "ayaYasser283/health_prediction_model"
MODEL_FILENAME = "health_pipeline.pkl"


#LOAD THE MODEL
#BECAUSE OF THE SIZE OF THE MODEL I UPLOAD IT IN HUGGING FACE AND IMPORT IT HERE
@st.cache_resource
def load_model():

    model_path = hf_hub_download(
        repo_id=HF_REPO_ID,
        filename=MODEL_FILENAME,
        repo_type="model"
    )

    pipeline = joblib.load(model_path)

    return pipeline


# PREPROCESSING FUNCTION WHICH ENCODE THE DATA AND APPLY PCA
def preprocess_data(user_input):
    data = pd.DataFrame([user_input])
    data['gender'] = data['gender'].map(label_maps['gender'])
    data['exercise_type'] = data['exercise_type'].map(label_maps['exercise_type'])
    data['caffeine_intake'] = data['caffeine_intake'].map(label_maps['caffeine_intake'])
    data['sleep_quality'] = data['sleep_quality'].map(label_maps['sleep_quality'])
    data['smoking_level'] = data['smoking_level'].map(label_maps['smoking_level'])
    data['mental_health_support'] = data['mental_health_support'].map(label_maps['mental_health_support'])
    data['education_level'] = data['education_level'].map(label_maps['education_level'])
    data['job_type'] = data['job_type'].map(label_maps['job_type'])
    data['occupation'] = data['occupation'].map(label_maps['occupation'])
    data['diet_type'] = data['diet_type'].map(label_maps['diet_type'])
    data['device_usage'] = data['device_usage'].map(label_maps['device_usage'])
    data['healthcare_access'] = data['healthcare_access'].map(label_maps['healthcare_access'])
    data['insurance'] = data['insurance'].map(label_maps['insurance'])
    data['family_history'] = data['family_history'].map(label_maps['family_history'])
    data['sunlight_exposure'] = data['sunlight_exposure'].map(label_maps['sunlight_exposure'])
    data['pet_owner'] = data['pet_owner'].map(label_maps['pet_owner'])
    data = pca.transform(data)
    return data

#FUNCTION TO EASE USING SELECT BOX FUNCTION AND ENHANCING READABILITY
def select_option(column, name, label):

    options = list(label_maps[name].keys())

    return column.selectbox( label , options , index= None)


#FUNCTION TO EASE USING RADIO FUNCTION AND ENHANCING READABILITY
def select_radio (column , name  , label):

    options = list(label_maps[name].keys())

    return column.radio( label , options , index= None)



#===========================================================================================================================================================================

# LOAD THE PIPELINE WHICH CONTAIN THE MODEL AND PREPROCESSING
pipeline = load_model()
model = pipeline['model']
label_maps = pipeline['label_maps']
pca = pipeline['pca']

#========================================================================= APP GUI ==========================================================================================
st.title("Health Status Prediction")
st.write("Enter your health and lifestyle information to predict your health status")

#FIRST SECTION
st.header("Personal and Professional Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age:",
        min_value=0,
        value=0
    )

    income = st.number_input(
        "Income:",
        min_value=0.0,
        value=0.0
    )
    work_hours = st.number_input(
        "Work Hours:",
        min_value=0,
        value=0
    )
    occupation = select_option(
        col1,
        "occupation",
        "Occupation / Your Job Title:"
    )
with col2:
    gender = select_radio(
        col2,
        "gender",
        'Gender:'
    )

    education_level = select_option(
        col2,
        "education_level",
        "Education Level:"
    )

    job_type = select_option(
        col2,
        "job_type",
        "Job Type:"
    )




st.divider()
#SECOND SECTION
st.header("Health / Medical Information")
col1 , col2  = st.columns(2)

with col1:
    blood_pressure = st.number_input(
        "Blood Pressure:",
        min_value=0.0,
        value=0.0
    )

    insulin = st.number_input(
        "Insulin:",
        min_value=0.0,
        value=0.0
    )

    cholesterol = st.number_input(
        "Cholesterol:",
        min_value=0.0,
        value=0.0
    )

    insurance = select_radio(
        col1,
        "insurance",
        'Insurance:'
    )

    family_history = select_radio(
        col1,
        "family_history",
        'Does your family have a history of a particular disease?'
    )


with col2:
    heart_rate = st.number_input(
        "Heart Rate:",
        min_value=0.0,
        value=0.0
    )

    glucose = st.number_input(
        "Glucose:",
        min_value=0.0,
        value=0.0
    )

    daily_supplement_dosage = st.number_input(
        "Daily Supplement Dosage:",
        min_value=0.0,
        value=0.0
    )

    healthcare_access = select_option(
        col2,
        "healthcare_access",
        'Evaluate your health access:'
    )




st.divider()

#THIRD SECTION
st.header("Physical Health Information")
col1 , col2 = st.columns(2)

with col1:
    bmi = st.number_input(
        "BMI:",
        min_value=0.0,
        value=0.0
    )

    diet_type = select_option(
        col1,
        "diet_type",
        "Diet Type:"
    )

    calorie_intake = st.number_input(
        "Calorie Intake:",
        min_value=0.0,
        value=0.0
    )
    water_intake = st.number_input(
        "Water Intake:",
        min_value=0.0,
        value=0.0
    )


    physical_activity = st.number_input(
        "Exercise Hours per Week:",
        min_value=0.0,
        value=0.0,
    )






with col2:
    waist_size = st.number_input(
        "Waist Size:",
        min_value=0.0,
        value=0.0
    )
    meals_per_day = st.number_input(
        "Meals Per Day:",
        min_value=0,
        value=0
    )
    sugar_intake = st.number_input(
        "Sugar Intake:",
        min_value=0.0,
        value=0.0
    )
    exercise_type = select_option(
        col2,
        "exercise_type",
        "Exercise Type:"
    )
    daily_steps = st.number_input(
        "Daily Steps:",
        min_value=0.0,
        value=0.0
    )

st.divider()

#FORTH SECTION
st.header("Mental Health Information")
col1 , col2 = st.columns(2)


with col1:
    mental_health_support = select_radio(
        col1,
        "mental_health_support",
        'Do you have a Mental Health Support?'
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0,
        value=0
    )


    stress_level = st.slider(
        "Rate your Stress Level from 0 to 10:",
        min_value=0,
        max_value=10
    )



    screen_time = st.number_input(
        "Screen Time",
        min_value=0.0,
        value=0.0
    )

    caffeine_intake = select_option(
        col1,
        "caffeine_intake",
        "Caffeine Intake: "
    )

    sunlight_exposure = select_option(
        col1,
        "sunlight_exposure",
        "Evaluate your sunlight exposure:"
    )

with col2:
    mental_health_score = st.slider(
        "Rate your mental health from 0 to 10",
        min_value=0,
        max_value=10
    )


    sleep_quality = select_option(
        col2,
        "sleep_quality",
        "Sleep Quality"
    )

    device_usage = select_option(
        col2,
        "device_usage",
        "Device Usage"
    )

    smoking_level = select_option(
        col2,
        "smoking_level",
        "Smoking Level"
    )

    pet_owner = select_radio(
        col2,
        "pet_owner",
        'Pet Owner'
    )





#PREDICTION
st.divider()
st.divider()

if st.button(
    "Predict Health Status",
    type="primary",
    use_container_width=True
):

    user_input = {
    'age':age,
    'gender':gender,
    'bmi':bmi,
    'waist_size':waist_size,
    'blood_pressure':blood_pressure,
    'heart_rate':heart_rate,
    'cholesterol':cholesterol,
    'glucose':glucose,
    'insulin':insulin,
    'sleep_hours':sleep_hours,
    'sleep_quality':sleep_quality,
    'work_hours':work_hours,
    'physical_activity':physical_activity,
    'daily_steps':daily_steps,
    'calorie_intake':calorie_intake,
    'sugar_intake':sugar_intake,
    'smoking_level':smoking_level,
    'water_intake':water_intake,
    'screen_time':screen_time,
    'stress_level':stress_level,
    'mental_health_score':mental_health_score,
    'mental_health_support':mental_health_support,
    'education_level':education_level,
     'job_type':job_type,
    'occupation':occupation,
    'income':income,
    'diet_type':diet_type,
    'exercise_type':exercise_type,
     'device_usage':device_usage,
     'healthcare_access':healthcare_access,
    'insurance':insurance,
    'sunlight_exposure':sunlight_exposure,
     'meals_per_day':meals_per_day,
    'caffeine_intake':caffeine_intake,
    'family_history':family_history,
    'pet_owner':pet_owner,
    'daily_supplement_dosage':daily_supplement_dosage,
  }

    try:

        data = preprocess_data(user_input)

        prediction = model.predict(data)[0]

        if prediction == 1:

            st.success("Healthy")

        else:

            st.error("Diseased")

    except Exception as e:

        st.error(
            f"An error occurred during prediction: {str(e)}"
        )

st.warning("This model does not replace a visit to the doctor. Get tests done at a reputable lab and show them to your doctor.")