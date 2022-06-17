from firebase import db
import random

images=["https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502036/CEM_PERU/CEM_Lambayeque_e5orwh.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502036/CEM_PERU/CEM_SanMartin_eey3ud.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502036/CEM_PERU/CEM_Tacna_ptapkm.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502036/CEM_PERU/CEM_Tumbes_ohzmeh.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502035/CEM_PERU/CEM_Piura_qgpmiw.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502035/CEM_PERU/CEM_Arequipa_y7srae.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502035/CEM_PERU/CEM_Lima_r9ifqr.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502034/CEM_PERU/CEM_Cajamarca_bom4nw.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502034/CEM_PERU/CEM_Callao_xbgfxq.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502034/CEM_PERU/CEM_Cuzco_rdpuaa.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502034/CEM_PERU/CEM_Moquegua_kdcewm.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502033/CEM_PERU/CEM_Apurimac_t9cf5u.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502033/CEM_PERU/CEM_Ayacucho_pdzk8g.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502033/CEM_PERU/CEM_Puno_tf9mnx.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502033/CEM_PERU/CEM_Huancavelica_ua5nh9.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502033/CEM_PERU/CEM_Junin_v40x2j.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502033/CEM_PERU/CEM_Ica_a83py6.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502033/CEM_PERU/CEM_MadreDeDios_pqdbpi.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502032/CEM_PERU/CEM_Huanuco_kv19ul.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502032/CEM_PERU/CEM_Ucayali_moakko.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502031/CEM_PERU/CEM_Loreto_r3epxp.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502031/CEM_PERU/CEM_Ancash_wyoj5o.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502031/CEM_PERU/CEM_LaLibertad_ubqsxq.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502031/CEM_PERU/CEM_Pasco_ozquje.jpg",
        "https://res.cloudinary.com/dk2g5rw5w/image/upload/v1653502031/CEM_PERU/CEM_Amazonas_mr85cv.jpg"]

def selectRandomImage():
  return random.choice(images)

async def getData(collection,arr,obj):
    if(arr==[]):
        docs = db.collection(collection).order_by("departamento").stream()
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