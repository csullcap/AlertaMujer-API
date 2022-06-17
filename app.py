from fastapi import FastAPI
from src.models.CentroEmergenciaMujer import CentroEmergenciaMujer
from src.models.Comisaria import Comisaria
from src.metodos import calculo_de_distancias, getData

comisarias_data=[]
centros_emergencia_mujer_data=[]

app = FastAPI()

@app.get('/')
async def home():
    await getData('comisarias',comisarias_data,Comisaria)
    return comisarias_data

""" @app.get('/comisarias')
async def mas_cercano_comisaria(lat:float,log:float):
    if (comisarias_data==[]):
        await getData('comisarias',comisarias_data,Comisaria)
    calculo_de_distancias(log,lat,comisarias_data)
    return comisarias_data[0]

@app.get('/centros-emergencia-mujer')
async def mas_cercano_centros_emergencia_mujer(lat:float,log:float):
    if (centros_emergencia_mujer_data==[]):
        await getData('centros_emergencia_mujer',centros_emergencia_mujer_data,CentroEmergenciaMujer)
    calculo_de_distancias(log,lat,centros_emergencia_mujer_data)
    return centros_emergencia_mujer_data[0] """