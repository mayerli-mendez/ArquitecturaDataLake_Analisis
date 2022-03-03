
![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!YP5u9sklC0iywPgRepMQVOdg8BAkAQlLoHr_GSobHaPNJuBAAf_VQKAw4x81bXaz%2Fitems%2F01PVDBQA53CR5HC7PJUNGZHWDBGXAE2JED%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MDkyODAwIiwiZXhwIjoiMTY0NjExNDQwMCIsImVuZHBvaW50dXJsIjoiTWwyby9jRUxiSDVZQ0NNcy9JeVlTQjBNM1VnY0ZVVDZKZk5kd2hITUZBQT0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6IlpqWTJaV1psTmpBdE1qVmpPUzAwT0RCaUxXSXlZekF0WmpneE1UZGhPVE14TURVMCIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.LzZIR2FuM09jdTBKNlFvc3lFVlJ0NytOcUp0d3BMM1pTTUl6djlvZTNzWT0&cTag=%22c%3A%7B717A14BB-E97D-4DA3-93D8-6135C04D2483%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)

Para la Realizacion de este proyecto de la fuente 6 primero descargaremos meidante tiktok scrpaer datos actualizados acerca de un tema en especifico: Assasins Creed Black Flag
Podremos visualizarlo y obtner los resultados mediante el comando tiktok-scraper hashtag AssasinsCreedBlackFlag -n 10 -d -t -z all donde nos ayudara con la descarga:
d: fomrato csv
z: formato zip
t:formato json
Al momoento de tener un archivo csv o json podremos utilizar Python para la realizacion del envio de datos a MongoDB entonces que libreria se usaran:
```
import json
import pandas as pd
import pymongo
```
Esto nos ayudara con el desarrollo del envio. Utilizando pyomongo.Client() nos ayudara en la URL de conexion de mongo y el puerto 27017 de nuestro localhost y podremos usar pandas para la lectura de nuestro csv o json al envio de nuestra base de datos Mongo. Si seguimos todos estos pasos podremos enviar sin ningun problema nuestro archivo a MongoDB.
```
import json
import pandas as pd
import pymongo
client=pymongo.MongoClient('mongodb://localhost:27017')
df=pd.read_json("AssasinsCreedIV.json")
print(df.head())
data=df.to_dict(orient="record")
print(data)
db=client["JuegosUbisoft"]
print(db)
db.BlackFlag.insert_many(data)

```
Al momento de tener nuestro archivo a MongoDB ahora dispondremos de enviarlo a SQLServer donde nos ayudara a ver de una mejor manera los datos en las tabals relacionales por ello se añadira una libreria llamada pyodbc para la conexion de SQL y al momento de la solicitud de conexion introducir en los string (') el nombre del servidor de su SQL Server.
Si seguimos todo este sript tendremos un mayor posbilidad de compilar al 100%. La creacion de tablas como se mostrara en el script debe ser manual por lo que pandas tiene una funcion llamado .head() y .columns donde podremos ver el tipo de variable que trbaja y sus cabeceras. De igual manera se utilizara un for para la insercion manual de SQl en los elementos que contiene nuestro archivo csv.
El archivo que exisitia en MongoDB exportaremos por codigo gracias a la funcion de pymongo get_database y get:collection para poder visualizar y extraer los datos de nuestra base de datos Mongo.
Libreria a  añadir :
```
from lib2to3.pgen2.driver import Driver
import pyodbc
import pandas as pd
import pymongo
import json
```
Como exportariamos En Mongo a un archivo csv:
```
client=pymongo.MongoClient('mongodb://localhost:27017')
db = client.get_database('JuegosUbisoft')
collection = db.get_collection('BlackFlag')
# Get a df with full collection:
df = pd.DataFrame(list(collection.find()))
## Exportar a Excel o CSV:
df.to_csv('AssasinsCreed4.csv', index=False,)
#df.to_excel('AssasinsCreed4.xlsx', index=False)
```
Despues eso imprtariamos a SQL Server:
```
r=pyodbc.drivers()
print(r)
try:
  conn=pyodbc.connect('DRIVER={SQL SERVER};SERVER=DESKTOP-PSENE10\SQLEXPRESS;DATABASE=JUEGOSUBISFOT;Trusted_Connection=yes;')
  print("Conexion Exitosa")
except Exception as es:
  print(es)

cursor=conn.cursor()
dif=pd.read_csv("AssasinsCreed4.csv")
print(dif.head())
print(dif.columns)
dip=pd.DataFrame(dif)
dip=dip.fillna(value=0)
solucion=cursor.execute('''CREATE TABLE BLACKFLAG (
                            id nvarchar(50),
                            id1 bigint,
                            secretID bigint,
                            texto nvarchar(300),
                            createTime int,
                            authorMeta nvarchar(700),
                            musicMeta nvarchar(850),
                            covers nvarchar(550),
                            webVideoUrl nvarchar(100),
                            videoUrl nvarchar(450),
                            videonoUrlWatrermark nvarchar(1),
                            VideoApinoUrlWatermark nvarchar(1),
                            videoMeta nvarchar(50),
                            diggCount int,
                            shareCount smallint,
                            playCount int,
                            commentCount smallint,
                            downloaded nvarchar(50),
                            mentions nvarchar(50),
                            hasthag nvarchar(1800),
                            effectStickers nvarchar(50) 
                                           )
                            ''')
print(solucion)

for row in dip.itertuples():
  cursor.execute(''' INSERT INTO BLACKFLAG (id,id1,secretID,texto,createTime,authorMeta,musicMeta,covers,webVideoUrl,videoUrl,videonoUrlWatrermark,VideoApinoUrlWatermark,videoMeta,diggCount,shareCount,playCount,commentCount,downloaded,mentions,hasthag)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ''', 
                    row.id,
                    row.id,
                    row.secretID,
                    row.text,
                    row.createTime,
                    row.authorMeta,
                    row.musicMeta,
                    row.covers,
                    row.webVideoUrl,
                    row.videoUrl,
                    row.videoUrlNoWaterMark,
                    row.videoApiUrlNoWaterMark,
                    row.videoMeta,
                    row.diggCount,
                    row.shareCount,
                    row.playCount,
                    row.commentCount,
                    row.downloaded,
                    row.mentions,
                    row.hashtags,
                    

                            )
conn.commit()
```
La funcion row. ayudara a extraer el contenido de nuestrp csv

