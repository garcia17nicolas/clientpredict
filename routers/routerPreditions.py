import pickle 
from fastapi import APIRouter, FastAPI
import numpy as np

from insterfases import CultivoData


app = FastAPI()
router = APIRouter()

with open ("cultivo.pkl","rb") as file:
    model=pickle.load(file)



@router.post("/predict")
def predict(data: CultivoData):
    data = data.model_dump()
    print(data)

    
    N=data["N"]
    P=data["P"]
    K=data["K"]
    temperature=data["temperature"]
    humidity=data["humidity"]
    ph=data["ph"]
    rainfall=data["rainfall"]

    xin = np.array([N,P,K,temperature,humidity,ph,rainfall]).reshape(1,7)
    prediction = model.predict(xin)
    print(prediction)


    print(prediction)

    return {"prediction" : prediction[0]}


if __name__=="__main__":
    app.rum()