from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib

app = FastAPI()

model=joblib.load('sentiment_model.pkl')

class textInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to the Sentiment Analysis API!"}
@app.post("/predict")
def predict(data: textInput):
    text=[data.text]
    prediction=model.predict([text][0])
    return {
        "Prediction":str(prediction[0]),
    }