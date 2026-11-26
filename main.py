from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI(title="Proyecto IA")

@app.get("/")
def inicio():
    return FileResponse("templates/index.html")

@app.get("/salud")
def salud():
    return {"estado": "correcto"}
from pydantic import BaseModel
import requests

class Consulta(BaseModel):
    mensaje: str

@app.post("/ia")
def inteligencia(data: Consulta):
    respuesta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:0.5b",
            "prompt": data.mensaje,
            "stream": False
        },
        timeout=120
    )
    respuesta.raise_for_status()
    return {"respuesta": respuesta.json()["response"]}


