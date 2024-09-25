from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy
from pyngrok import ngrok
import nest_asyncio
import uvicorn
app = FastAPI()

class model_input(BaseModel):
    Pregnancies	: int
    Glucose	: int
    BloodPressure : int
    SkinThickness : int
    Insulin	: int
    BMI	: float
    DiabetesPedigreeFunction : float
    Age : int

model = pickle.load(open('C:/Users/priya/Downloads/diabetes_model.sav', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_prediction(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    preg = input_dictionary['Pregnancies']
    glc = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    st = input_dictionary['SkinThickness']
    ins = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    ag = input_dictionary['Age']

    input_list = [preg, glc, bp ,st, ins ,bmi, dpf, ag] 
    load_scaler = pickle.load(open("C:/Users/priya/Downloads/scaler.sav", 'rb'))
    arr = numpy.asarray(input_list, dtype=float)
    reshape_data = arr.reshape(1,-1)
    std_data = load_scaler.transform(reshape_data)
    prediction = model.predict(std_data)
    if prediction[0] == 0:
        result = 'The person is not diabetic'
    else:
        result = 'The person is diabetic'
    return result
ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port= 8000)