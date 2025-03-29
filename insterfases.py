from pydantic import BaseModel

class dataTest(BaseModel):
    nombre: str
    estudiantes: float


class CultivoData(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float
    
