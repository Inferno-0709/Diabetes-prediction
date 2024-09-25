import requests
import json
url = 'https://6b09-14-97-208-186.ngrok-free.app/diabetes_prediction'
input_data = {
    'Pregnancies' : 5,
    'Glucose' : 116,
    'BloodPressure'	: 74,
    'SkinThickness'	: 0,
    'Insulin'	: 0,
    'BMI'	: 25.6,
    'DiabetesPedigreeFunction' : 0.201,
    'Age' : 30
}
response = requests.post(url, json=input_data)
print(response.text)