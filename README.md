
![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!YP5u9sklC0iywPgRepMQVOdg8BAkAQlLoHr_GSobHaPNJuBAAf_VQKAw4x81bXaz%2Fitems%2F01PVDBQA32V2ET7YBPRVALAQVNMSCIL67R%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MDkyODAwIiwiZXhwIjoiMTY0NjExNDQwMCIsImVuZHBvaW50dXJsIjoiTWwyby9jRUxiSDVZQ0NNcy9JeVlTQjBNM1VnY0ZVVDZKZk5kd2hITUZBQT0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6IlpqWTJaV1psTmpBdE1qVmpPUzAwT0RCaUxXSXlZekF0WmpneE1UZGhPVE14TURVMCIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.LzZIR2FuM09jdTBKNlFvc3lFVlJ0NytOcUp0d3BMM1pTTUl6djlvZTNzWT0&cTag=%22c%3A%7B3F89AE7A-2FE0-408D-B042-AD648485FBF1%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)

La fuente 3 consite en obtener datos de la red social de Twitter , estos datos guardarlos en la base de datos MongoDb y una vez guardados , importarlos a otra base MYSQL y finalmente analizar la informacion mediante la herramienta PowerBi. 

Lo primero que se realizo es la importacion de librerias :

```
import tweepy
import json
import requests
from pymongo import MongoClient 
```
A continuacion se coloco las API:

```
###API ########################
ckey = 'SKepyS4uZlyBmXV9xtxQP9hN8'
csecret = '02DIS0kb8qGJpRAd1YfFn89Pmw73gSUGBVPJMWu5B8CD46rYNp'
atoken = '115946548-UmysCzkNSMsbdUqad25NO2TlV6KodCfBjJ2RjMDJ'
asecret = 'Lx1VT6yVeC2b3eQPmfyBMhQwKjViObqYZ6tF8dnUcJQU7'
```

Se creo una clase la cual permite la extraccion de datos y mediante un mensaje indica que los datos se han guardado o si ya existen :
```
class listener (tweepy.Stream):
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = col.insert_one(dictTweet)
            print ("SAVED" +str (doc) + "=>"+ str(data))
        except:
            print("Already exists")
            pass
        return True
    def on_error(self, status):
        print(status)
```
Despues se paso las APIS como parametro para tener acceso a la informacion , tambien se realizo la conexion con la base de datos localmente y mediante un mensaje indica si se realizo la conexion o si fue rechazada : 

```
twitter_stream = listener(ckey, csecret, atoken, asecret )
try:
    client = MongoClient('mongodb://localhost:27017')
    client.server_info()
    print("Conexion exitosa")
    client.close
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Conexión rechazada") 

```

Una vez realizada la conexion con la base de datos , se procede a crear la base de datos y la coleccion donde se van a guardar los datos: 
```
dbm = client['dbproyecto']
col = dbm['covid']

```

Finalmente se hace la obtencion de datos mediante filtro de palabras : 

```
twitter_stream.filter(track=['coronavirus,mundo,covid,enfermedad'])

```

Una vez realizado la obtencion de datos se verifico en la base de datos MongoDB :

![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!vd8GfzWINEKFEhiNEYMU15jj6lZl0nFPswxixSkFbJ_qp7H30B29Q49S3ZRZ0OyW%2Fitems%2F01CMLOFC3UR2S3EOXE6NG2DED4EAAEI3RS%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MTAzNjAwIiwiZXhwIjoiMTY0NjEyNTIwMCIsImVuZHBvaW50dXJsIjoidVBSL3RZNHQ1Qlk3NENYL3JMV3ZLMnRVWiszTnh2eG55S25IckgwbnluMD0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6Ik4yWXdObVJtWW1RdE9EZ3pOUzAwTWpNMExUZzFNVEl0TVRnNFpERXhPRE14TkdRMyIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.N3RrVktKOUJmVk9SSGZ6aUx4SURYTWRlV0Q0SEJUeHlNUkZhN3ZtUU1ZND0&cTag=%22c%3A%7BB2A58E74-E43A-4DF3-A190-7C2000446E32%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)

Una ves que se verifico los datos se procedio a exportar en formato csv y de ahi se importo a la base de datos MYSQL mediante interfaz grafica.

Para ello lo primero que se realizo es crear una base de datos en MYSQL :

![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!vd8GfzWINEKFEhiNEYMU15jj6lZl0nFPswxixSkFbJ_qp7H30B29Q49S3ZRZ0OyW%2Fitems%2F01CMLOFC2HWC5W7PZMNFFLPMKS2BRA6QWQ%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MTAzNjAwIiwiZXhwIjoiMTY0NjEyNTIwMCIsImVuZHBvaW50dXJsIjoidVBSL3RZNHQ1Qlk3NENYL3JMV3ZLMnRVWiszTnh2eG55S25IckgwbnluMD0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6Ik4yWXdObVJtWW1RdE9EZ3pOUzAwTWpNMExUZzFNVEl0TVRnNFpERXhPRE14TkdRMyIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.N3RrVktKOUJmVk9SSGZ6aUx4SURYTWRlV0Q0SEJUeHlNUkZhN3ZtUU1ZND0&cTag=%22c%3A%7B6FBBB047-2CBF-4A69-B7B1-52D0620F42D0%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)

Una vez creada la base cargamos el archivo e importamos: 

![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!vd8GfzWINEKFEhiNEYMU15jj6lZl0nFPswxixSkFbJ_qp7H30B29Q49S3ZRZ0OyW%2Fitems%2F01CMLOFC4L4JBU6GMEKZF2BTIESMLHGIVY%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MTAzNjAwIiwiZXhwIjoiMTY0NjEyNTIwMCIsImVuZHBvaW50dXJsIjoidVBSL3RZNHQ1Qlk3NENYL3JMV3ZLMnRVWiszTnh2eG55S25IckgwbnluMD0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6Ik4yWXdObVJtWW1RdE9EZ3pOUzAwTWpNMExUZzFNVEl0TVRnNFpERXhPRE14TkdRMyIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.N3RrVktKOUJmVk9SSGZ6aUx4SURYTWRlV0Q0SEJUeHlNUkZhN3ZtUU1ZND0&cTag=%22c%3A%7B4F43E28B-8419-4B56-A0CD-0493167322B8%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)

Y verificamos que los datos se han importado correctamente ingresando a la tabla en la base de datos de MYSQL : 

![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!vd8GfzWINEKFEhiNEYMU15jj6lZl0nFPswxixSkFbJ_qp7H30B29Q49S3ZRZ0OyW%2Fitems%2F01CMLOFC4DRZX2Y7YCOBDKUWIVHTWGLMSD%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MTAzNjAwIiwiZXhwIjoiMTY0NjEyNTIwMCIsImVuZHBvaW50dXJsIjoidVBSL3RZNHQ1Qlk3NENYL3JMV3ZLMnRVWiszTnh2eG55S25IckgwbnluMD0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6Ik4yWXdObVJtWW1RdE9EZ3pOUzAwTWpNMExUZzFNVEl0TVRnNFpERXhPRE14TkdRMyIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.N3RrVktKOUJmVk9SSGZ6aUx4SURYTWRlV0Q0SEJUeHlNUkZhN3ZtUU1ZND0&cTag=%22c%3A%7BAC6F8E83-027F-4670-AA59-153CEC65B243%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)


Una vez importado los datos en MYSQL se procedio a importar a la herramienta PowerBi y se realizo el analisis. 

Para ello ingresamos a PowerBi cargamos e importamos el documento csv que teniamos anteriormente : 

![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!vd8GfzWINEKFEhiNEYMU15jj6lZl0nFPswxixSkFbJ_qp7H30B29Q49S3ZRZ0OyW%2Fitems%2F01CMLOFC6F53VADXZYTVGZTFUBBMUG5B4Q%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MTAzNjAwIiwiZXhwIjoiMTY0NjEyNTIwMCIsImVuZHBvaW50dXJsIjoidVBSL3RZNHQ1Qlk3NENYL3JMV3ZLMnRVWiszTnh2eG55S25IckgwbnluMD0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6Ik4yWXdObVJtWW1RdE9EZ3pOUzAwTWpNMExUZzFNVEl0TVRnNFpERXhPRE14TkdRMyIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.N3RrVktKOUJmVk9SSGZ6aUx4SURYTWRlV0Q0SEJUeHlNUkZhN3ZtUU1ZND0&cTag=%22c%3A%7B01EAEEC5-38DF-4D9D-9996-810B286E8790%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)

Una vez importado , se hizo un filtrado por nombre de usuario y segun seleccionemos , muestra los datos de la persona : 

![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!vd8GfzWINEKFEhiNEYMU15jj6lZl0nFPswxixSkFbJ_qp7H30B29Q49S3ZRZ0OyW%2Fitems%2F01CMLOFCZHTOONVKYBPBA2A64JUM6YGUZC%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MTAzNjAwIiwiZXhwIjoiMTY0NjEyNTIwMCIsImVuZHBvaW50dXJsIjoidVBSL3RZNHQ1Qlk3NENYL3JMV3ZLMnRVWiszTnh2eG55S25IckgwbnluMD0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6Ik4yWXdObVJtWW1RdE9EZ3pOUzAwTWpNMExUZzFNVEl0TVRnNFpERXhPRE14TkdRMyIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.N3RrVktKOUJmVk9SSGZ6aUx4SURYTWRlV0Q0SEJUeHlNUkZhN3ZtUU1ZND0&cTag=%22c%3A%7BDA9C9B27-01AB-4178-A07B-89A33D835322%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)
