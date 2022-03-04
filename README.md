
![image](https://user-images.githubusercontent.com/74840012/156794167-8731121e-4d1c-44e1-92dd-15ff6447dcfe.png)

La fuente 5 consiste en obtener datos de la red social de Facebook, estos datos guardarlos en la base de datos MongoDb y una vez guardados, importarlos a la base de datos SQLite y finalmente analizar la información mediante la herramienta PowerBi. 


Como primer paso será descargar una librería llamada Facebook-scraper que nos permitirá acceder a todos los datos requeridos en Facebook 
```
pip install facebook-scraper
```
Se importa get_posts, de igual manera se utiliza varias librerías como pymongo json y Time. 
Para la conexión con mongo se importa MongoClient, se define una variaible client se coloca el localhost.
Se definimos una variable dbs,donde se coloca el nombre de la base de datos previamente creada en mongo. 
```
from facebook_scraper import get_posts
import pymongo
import json
import time

from pymongo import MongoClient
client = MongoClient("localhost", 27017)
dbs=client["facebook-free-fire"]
db=dbs.Documentos 
```

A continuacion se procede a guardar la informacion extraida de facebook a mongoDB, lo que resta por hacer esdefinir la estructura de como se mostraran la informacion recopilada la mejor opcion es en formato json
```
i=1
for post in get_posts('FreeFireSA', pages=10, extra_info=True):
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
        db.insert_one(doc)              

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))
```
![image](https://user-images.githubusercontent.com/74801652/156793507-b336400e-9f3b-4c62-b8cf-2828310e0661.png)



Ahora se procedera a exportar la informacion recopilida en mongoDb a la base de datos SQlite
Se guardaran los datos en formato csv
```
client=pymongo.MongoClient('mongodb://localhost:27017')
db = client.get_database('facebook-free-fire')
collection = db.get_collection('Documentos')

df = pd.DataFrame(list(collection.find()))## Exportar a Excel o CSV:

df.to_csv('facebook-free-fire.csv', index=False,)

```
Se realiza la conexión de la base Sqlite, y se crea una nueva tabla en la base con el nombre respectivo

```
import sqlite3
import pandas as pd

conn = sqlite3.connect('free-fire1.db')
c = conn.cursor()
users = pd.read_csv('facebook-free-fire.csv')
users.to_sql('recoleccion', conn, if_exists='append', index = False, chunksize = 10000)
```
![image](https://user-images.githubusercontent.com/74801652/156793360-858d54ad-7247-4d4d-acdb-f2ab6660cccb.png)



Para la finalizacion de la fuente 5 se utiliza la herramienta PowerBi donde se realiza un estudio de todos los datos obtenidos en las diferentes bases de datos, realizando su respectivo filtrado y estudio de los datos
