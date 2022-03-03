
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
