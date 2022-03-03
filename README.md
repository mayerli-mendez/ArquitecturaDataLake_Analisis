
![image](https://user-images.githubusercontent.com/74840012/156655478-4edef9d6-aaf2-4577-be06-9da5213f9cbc.PNG)

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
Finalmente utilizaremos Power Bi para obtener los datos directamente con la opcion de obtener Datos por medio de SQL y luego podremos poner en crear datos. Luego introduciremos graficos acorde al analisis que entedamos por meido de los campos del archivo de SQL Server y las multiples opciones de visualizacion como : Mapa coreograico, rueda de paste y tabla de lineas.
![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docidepnecuador-my.sharepoint.com/personal/jorge_ortiz_epn_edu_ec/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjorge%5Fortiz%5Fepn%5Fedu%5Fec%2FDocuments%2FWhatsApp%20Image%202022%2D02%2D25%20at%208%2E47%2E01%20PM%2Ejpeg&parent=%2Fpersonal%2Fjorge%5Fortiz%5Fepn%5Fedu%5Fec%2FDocuments
