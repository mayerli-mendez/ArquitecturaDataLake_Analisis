
![image](https://user-images.githubusercontent.com/74840012/156653511-74915d0f-9344-4e37-89e8-a9f717a74aea.PNG)

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
![image](https://user-images.githubusercontent.com/74801652/156790163-bee7a4b6-e0e7-4c22-a2e8-a5adda13788b.png)

Para la finalizacion de la fuente se utiliza la herramienta PowerBi donde se realiza un estudio de todos los datos obtenidos en las diferentes bases de datos



