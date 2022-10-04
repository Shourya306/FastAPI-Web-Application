import numpy as np
from fastapi import FastAPI
import pickle
from base import linear_model

app = FastAPI()
model = pickle.load(open('linear_model_fastapi.pkl','rb'))


@app.get('/')
def home():
    return 'Profit prediction of a company'

@app.post('/predict')
def prediction(data:linear_model):
    data = data.dict()
    R_D = data['R_D']
    Administration = data['Administration']
    Marketing = data['Marketing']
    State_California = data['State_California']
    State_Florida = data['State_Florida']
    State_New_York = data['State_New_York']

    result = model.predict(np.array([R_D,Administration,Marketing,State_California,State_Florida,State_New_York]).reshape(1,-1))
    return f'The profit of the startup is {result[0]}'