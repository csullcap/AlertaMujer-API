from firebase import db

async def getData(collection,arr,obj):
    if(arr==[]):
        docs = db.collection(collection).stream()
        for doc in docs:
            aux=obj.from_dict(doc.id,doc.to_dict())
            arr.append(aux)

def calculo_de_distancias(log,lat,arr):
    for element in arr:
        distancia=haversine(log,lat,element.longitud,element.latitud)
        element.setDistancia(distancia)
    arr.sort(key=lambda p :p.distancia) 

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    # CONVERTIR GRADOS DECIMALES A RADIANES 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # FORMULA HAVERSINE
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # RADIO DE LA TIERRA EN KMTS 6371
    km = 6371*c
    return km*1000 