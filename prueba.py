import requests

direccion = "http://www.omdbapi.com/?apikey=26e87f71&i=tt3896198"

respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    print(respuesta.text)
    datos = respuesta.json()
    print(datos)
else:
    print("Se ha producido un error", respuesta.status)