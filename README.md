
![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!YP5u9sklC0iywPgRepMQVOdg8BAkAQlLoHr_GSobHaPNJuBAAf_VQKAw4x81bXaz%2Fitems%2F01PVDBQA7VLEVK7B7UDJC3PIV4ODKO7ZB4%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MDkyODAwIiwiZXhwIjoiMTY0NjExNDQwMCIsImVuZHBvaW50dXJsIjoiTWwyby9jRUxiSDVZQ0NNcy9JeVlTQjBNM1VnY0ZVVDZKZk5kd2hITUZBQT0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6IlpqWTJaV1psTmpBdE1qVmpPUzAwT0RCaUxXSXlZekF0WmpneE1UZGhPVE14TURVMCIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.LzZIR2FuM09jdTBKNlFvc3lFVlJ0NytOcUp0d3BMM1pTTUl6djlvZTNzWT0&cTag=%22c%3A%7BAF2A59F5-F487-451A-B7A2-BC70D4EFE43C%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)
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
Para la finalizacion de la fuente 5 se utiliza la herramienta PowerBi donde se realiza un estudio de todos los datos obtenidos en las diferentes bases de datos, realizando su respectivo filtrado y estudio de los datos
