#!/usr/bin/env python3

import requests
import json
from faker import Faker


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

# Funcion para obtiener el token mediante la Api LoginviaBasic
def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Código de estado {r.status_code} y texto {r.text}, mientras intenta autenticarse.")

# Funcion para agregar libros mediante el metodo Post de la Api
def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Libro {book} agregado.")
    else:
        raise Exception(f"Error codigo {r.status_code} y texto {r.text}, al intentar agregar un libro {book}.")

# Obtiene la clave del token de autenticación
apiKey = getAuthToken()

# Usando el módulo faker, se genera libros "fake" aleatorios
fake = Faker()
for i in range(4, 105):
    fakeTitle = fake.catch_phrase()
    fakeAuthor = fake.name()
    fakeISBN = fake.isbn13()
    book = {"id":i, "title": fakeTitle, "author": fakeAuthor, "isbn": fakeISBN}
    # agrega el nuevo libro aleatorio "fake" usando la API
    addBook(book, apiKey) 