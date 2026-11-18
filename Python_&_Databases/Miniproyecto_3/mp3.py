import requests
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["feriados"]
collection = db["feriados2024"]

collection.delete_many({})

# Extracción de datos de la API e inserción en MongoDB
url = "https://www.chia.cl/api/feriados/2024"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data:
        collection.insert_many(data)
        print("-> Datos extraídos e insertados exitosamente en la colección 'feriados2024'.\n")

# 4. Preguntas 

# a. Obtener todos los feriados
print("=== 4a. Todos los feriados ===")
for f in collection.find():
    print(f)

# b. Obtener solo los feriados de tipo "Religioso"
print("\n=== 4b. Feriados de tipo Religioso ===")
for f in collection.find({"tipo": "Religioso"}):
    print(f)

# c. Obtener solo los feriados irrenunciables
print("\n=== 4c. Feriados irrenunciables ===")
for f in collection.find({"irrenunciable": {"$in": [1, "1"]}}):
    print(f)

# d. Obtener los feriados que incluyen el texto "Santo" en su nombre
print("\n=== 4d. Feriados con 'Santo' en el nombre ===")
for f in collection.find({"nombre": {"$regex": "Santo", "$options": "i"}}):
    print(f)

# e. Obtener los feriados celebrados entre el 11 de marzo y el 31 de agosto de 2024
print("\n=== 4e. Feriados entre 2024-03-11 y 2024-08-31 ===")
query_fecha = {"fecha": {"$gte": "2024-03-11", "$lte": "2024-08-31"}}
for f in collection.find(query_fecha):
    print(f)

# 5. Insertar un nuevo feriado 
nuevo_feriado = {
    "nombre": "Unión de los dos paisajes",
    "comentarios": "Primera vez que una expedición chilena logró unir la Cordillera de los Andes y la costa del Pacífico en un solo día",
    "fecha": "2024-03-11",
    "irrenunciable": 0,
    "tipo": "Religioso"
}

resultado = collection.insert_one(nuevo_feriado)
print(f"\n-> Nuevo feriado insertado con ID: {resultado.inserted_id}")