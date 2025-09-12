from fastapi import FastAPI
from controller import GruaController

app = FastAPI()
controller = GruaController()

@app.post("/recomendar_grua/")
def recomendar_grua(datos: dict):
    """
    Recibe un JSON con los datos del izaje y retorna la recomendación de grúa.
    """
    return controller.recomendar_grua(datos)