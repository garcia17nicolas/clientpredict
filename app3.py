from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import routerPreditions

app = FastAPI()
app.include_router(routerPreditions.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar "*" por ["http://127.0.0.1:5500&quot;] si quieres más seguridad
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)


if __name__=="__main__":
    app.rum()