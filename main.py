import requests

pregunta = input("Título de la película")

API_KEY = "da22215a"

direccion = "http://www.omdbapi.com/?apikey={}&s={}".format(API_KEY, pregunta)

respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos['Response'] == "False":
        print(datos['Error'])
    else:
        primera_peli = datos["Search"][0]
        clave = primera_peli["imdbID"]

        otra_direccion = "http://www.omdbap.com/?apikey={}&i={}".format(API_KEY, clave)
        nueva_respuesta = requests.get(otra_direccion)
        if nueva_respuesta.status_code == 200:
            datos = nueva_respuesta.json()
            if datos["Response"] == "False":
                print(datos['Error'])
            else:
                titulo = datos["Title"]
                anyo = datos["Year"]
                director = datos["Director"]
                print("La peli {}, estrenada en el año {}, fue dirigida por {}").format(titulo, anyo, director)
        else: 
            print("Error en consulta:", nueva_respuesta.status_code)
else:
    print("Error en búsqueda:", respuesta.status_code)