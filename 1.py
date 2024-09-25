import pickle
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
# loading the saved model
def diabetes_prediction(input_data):
    print(input_data)
    load_model = pickle.load(open ("C:/Users/priya/Downloads/diabetes_model (1).sav", 'rb'))
    load_scaler = pickle.load(open("C:/Users/priya/Downloads/scaler.sav", 'rb'))
    arr = np.asarray(input_data, dtype=float)
    reshape_data = arr.reshape(1,-1)
    std_data = load_scaler.transform(reshape_data)
    prediction = load_model.predict(std_data)
    print(prediction)
    if(prediction[0] == 0):
        return 'not diabetic'
    else:
        return 'diabetic'   
    
def main():
    js_code = """
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const inputs = document.querySelectorAll('input[type="text"]');
        inputs.forEach((input, index) => {
            input.addEventListener('keydown', function(event) {
                if (event.key === 'Enter') {
                    event.preventDefault();
                    const nextInput = inputs[index + 1];
                    if (nextInput) {
                        nextInput.focus();
                    }
                }
            });
        });
    });
</script>
"""
    components.html(js_code)
    st.title('Diabetes prediction')
    
    Pregnancies = st.text_input('Number of pregnancies: ')
    Glucouse = st.text_input('Glucouse level: ')
    BloodPressure = st.text_input('Enter blood pressure: ')
    SkinThickness = st.text_input('skin thickness: ')
    InsulinLevel = st.text_input('Insulin level: ')
    BMI = st.text_input('Body mass index: ')
    DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function: ')
    Age = st.text_input('Age of the person: ')
        

        

    diagnosis = ''
    if st.button('Diabetes test result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucouse, BloodPressure, SkinThickness, InsulinLevel, BMI, DiabetesPedigreeFunction , Age])
        st.success(diagnosis)
main()

