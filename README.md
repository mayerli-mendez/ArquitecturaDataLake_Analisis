![image](https://user-images.githubusercontent.com/74840012/156794083-9295ada6-ee8c-4e8a-92a3-ffd774ee822b.png)

La fuente 3 consiste en obtener datos de la red social de Twitter, estos datos guardarlos en la base de datos MongoDB y una vez guardados , importarlos a otra base MYSQL y finalmente analizar la información mediante la herramienta PowerBI. 

Lo primero que se realizo es la importación de librerías :

```
import tweepy
import json
import requests
from pymongo import MongoClient 
```
A continuación, se colocó las API :

```
###API ########################
ckey = 'SKepyS4uZlyBmXV9xtxQP9hN8'
csecret = '02DIS0kb8qGJpRAd1YfFn89Pmw73gSUGBVPJMWu5B8CD46rYNp'
atoken = '115946548-UmysCzkNSMsbdUqad25NO2TlV6KodCfBjJ2RjMDJ'
asecret = 'Lx1VT6yVeC2b3eQPmfyBMhQwKjViObqYZ6tF8dnUcJQU7'
```

Se creo una clase la cual permite la extracción de datos y mediante un mensaje indica que los datos se han guardado o si ya existen :
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
Después se pasó las APIS como parámetro para tener acceso a la información, también se realizó la conexión con la base de datos localmente y mediante un mensaje indica si se realizó la conexión o si fue rechazada : 

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

Una vez realizada la conexión con la base de datos, se procede a crear la base de datos y la colección donde se van a guardar los datos: 
```
dbm = client['dbproyecto']
col = dbm['covid']

```

Finalmente se hace la obtención de datos mediante filtro de palabras: 

```
twitter_stream.filter(track=['coronavirus,mundo,covid,enfermedad'])

```

Una vez realizado la obtención de datos se verifico en la base de datos MongoDB :

![image](https://user-images.githubusercontent.com/74840012/156654852-b35d7546-2aef-411f-96ff-ff3bf1608b34.png)

Una vez que se verifico los datos se procedió a exportar en formato csv y de ahí se importó a la base de datos MYSQL mediante interfaz gráfica.

Para ello lo primero que se realizo es crear una base de datos en MYSQL:

![image](https://user-images.githubusercontent.com/74840012/156654878-a4b7e55e-c421-48a7-87dc-bc48c28c2da9.png)

Una vez creada la base, cargamos e importamos el archivo csv : 

![image](https://user-images.githubusercontent.com/74840012/156654897-9cd9b217-0b0f-41b4-a498-22335b8edcd7.png)


Y verificamos que los datos se han importado, ingresando a la tabla : 

![image](https://user-images.githubusercontent.com/74840012/156654915-1882bc7d-e2f5-4780-ae4e-3c6100e8f894.png)


Una vez importado los datos en MYSQL se procedió a importar a la herramienta PowerBI mediante interfaz gráfica y se realizó el análisis. 

Para ello ingresamos a PowerBI cargamos e importamos el documento csv que teníamos anteriormente : 

![image](https://user-images.githubusercontent.com/74840012/156654933-99ddf535-a180-476f-a094-b1da0eb9edbd.png)

Una vez importado, se hizo un filtrado por nombre de usuario y según seleccionemos, muestra los datos de la persona : 

![image](https://user-images.githubusercontent.com/74840012/156655040-73265b06-011f-4358-989a-fe4c0ceb4b69.PNG)

