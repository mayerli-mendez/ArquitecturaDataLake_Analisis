
![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!YP5u9sklC0iywPgRepMQVOdg8BAkAQlLoHr_GSobHaPNJuBAAf_VQKAw4x81bXaz%2Fitems%2F01PVDBQA3UHF3HCQ6LKFGK2EARQB7YMYRI%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MDkyODAwIiwiZXhwIjoiMTY0NjExNDQwMCIsImVuZHBvaW50dXJsIjoiTWwyby9jRUxiSDVZQ0NNcy9JeVlTQjBNM1VnY0ZVVDZKZk5kd2hITUZBQT0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6IlpqWTJaV1psTmpBdE1qVmpPUzAwT0RCaUxXSXlZekF0WmpneE1UZGhPVE14TURVMCIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.LzZIR2FuM09jdTBKNlFvc3lFVlJ0NytOcUp0d3BMM1pTTUl6djlvZTNzWT0&cTag=%22c%3A%7B71763974-CB43-4C51-AD10-11807F866228%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)

La fuente 7 consiste en obtener datos de la red social Facebook, estos datos se guardaran en la base de datos CouchDb y una vez guardados, importarlos a la base de MongoAtlas finalmente analizar la información mediante la herramienta PowerBi. 

Como primer paso será descargar una librería llamada Facebook-scraper que nos permitirá acceder a todos los datos requeridos en Facebook 
```
pip install facebook-scraper
```
Llamamos a la librería descargada de Facebook-scraper, de la misma manera se importa varias librerías que utilizaremos más adelante como el couchdb, Json y time. 

```
from facebook_scraper import get_posts
import couchdb
import json
import time
```
Realizamos una conexión con el couch,continuamos definiendo una variable que será nombredb, y en este apartado ponemos el nombre de la base de datos previamente creada en nuestro couchdb. 

```
couch=couchdb.Server('http://admin:12345@127.0.0.1:5984')
nombredb='facebook-olympics'
db=couch[nombredb]
```
Se muestra un el codigo donde se procede a extraer la informacion de facebook y guardarlo en la base de datos de cocuch, con un formato json mostrado a continuacion 
```
i=1
for post in get_posts('olympics', pages=10, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db.save(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))
 ```
 Se verifica la informacion guardada en la base de couchDB
 ```
 ```
 
 Ahora se procedera a exportar los datos de couchDB y cargarlo en la base de datos atlas para eso se comienza con importar las librerias de client, couch json y certifi
  ```
  import requests
from pymongo import MongoClient
import couchdb
import json
import certifi
 ```
Se define la URL, y se realiza una validación de conexión a mongo Atlas.
```
URL = 'http://admin:12345@localhost:5984'
server=couchdb.Server(URL)
try:
    ca=certifi.where()#busque el certificado y no tengamos problemas de seguridad
    client = MongoClient('mongodb+srv://admin:12345@cluster0.vz0v3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    client.server_info()
    print('Conexion realizada con exito')
except pymongo.erros.ServerSelectionTimeoutError as errorTiempo:
    print('Coneexion fallida')
 ```
 Definimos tres variables diferentes, entre ellas estara el nombre de la nueva base a crear
 
   ```
db = server["facebook-olympics"]# nombre de bd en couchDB

dbc=client['Facebook_Olympics']#nombre Cient en MongoAtlas

colect=dbc['datos1_olympics']#nombre coleccion en MongoAtlas
 ```
Se guardan los datosn en MongoAtlas con un formato json
  ```
try:
    for docid in db.view('_all_docs'):
        id=docid['id']
        doc=db[id]
        dato={
            "_id": doc["_id"],
            "_rev": doc["_rev"],
            "texto": doc["texto"],
            "likes": doc["likes"],
            "shares": doc["shares"],
            "post_url": doc["post_url"]
        }
        
        colect.insert_one(dato)
    print("base de datos creada")
    
except requests.ConnectionError as e:
    raise e
    print("Error al crear datos")
 ```
Para la finalizacion de la fuente se utiliza la herramienta PowerBi donde se realiza un estudio de todos los datos obtenidos en las diferentes bases de datos
