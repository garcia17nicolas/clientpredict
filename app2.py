import pickle
from fastapi import FastAPI
import numpy as np

from insterfases import CultivoData

app = FastAPI()

# Cargar el modelo desde el archivo pickle
with open("cultivo.pkl", "rb") as file:
    model = pickle.load(file)

@app.get("/")
def index():
    return {"Mensaje": "API 2 running"}

@app.post("/predict")
def predict(data: CultivoData):
    # Convertir los datos del modelo en un diccionario
    data = data.model_dump()
    print(data)

    # Extraer los valores de las variables de entrada
    N = data["N"]
    P = data["P"]
    K = data["K"]
    temperature = data["temperature"]
    humidity = data["humidity"]
    ph = data["ph"]
    rainfall = data["rainfall"]

    # Preparar los datos de entrada para el modelo
    xin = np.array([N, P, K, temperature, humidity, ph, rainfall]).reshape(1, 7)
    
    # Realizar la predicción
    prediction = model.predict(xin)
    print(prediction)

    # Retornar los resultados, incluyendo las variables de entrada y la predicción
    return {
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

