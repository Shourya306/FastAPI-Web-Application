from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()
model = pickle.load(open('/linear_model_fastapi.pkl','rb'))


@app.get('/')
def home():
    return 'Home page'

