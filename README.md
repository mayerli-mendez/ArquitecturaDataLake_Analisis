
![Esta es una imagen](![image](https://user-images.githubusercontent.com/74840012/156651558-361e0104-f575-4d5a-8aa1-92217cdf9eee.png)
)

La fuente 1 consiste en obtener datos de la red social de Twitter, estos datos guardarlos en la base de datos CouchDb y una vez guardados, importarlos a otra base SQL Server y finalmente analizar la información mediante la herramienta PowerBi. 

Lo primero que se realizo es la importación de librerías:

```
import couchdb
import tweepy
import json
```
A continuación, se colocó las API:

```
###API ########################
ckey = 'SKepyS4uZlyBmXV9xtxQP9hN8'
csecret = '02DIS0kb8qGJpRAd1YfFn89Pmw73gSUGBVPJMWu5B8CD46rYNp'
atoken = '115946548-UmysCzkNSMsbdUqad25NO2TlV6KodCfBjJ2RjMDJ'
asecret = 'Lx1VT6yVeC2b3eQPmfyBMhQwKjViObqYZ6tF8dnUcJQU7'
```

Se creo una clase la cual permite la extracción de datos y mediante un mensaje indica que los datos se han guardado o si ya existen:
```
class listener(tweepy.Stream):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
```
Después se pasó las APIS como parámetro para tener acceso a la información, también se realizó la conexión con la base de datos localmente , en donde se coloca el nombre del usuario y contraseña : 

```
twitter_stream = listener(ckey, csecret,atoken,asecret)
server = couchdb.Server('http://admin:12345@127.0.0.1:5984/')

```

Una vez realizada la conexión con la base de datos, se procede a crear la base de datos : 
```
try:
    db = server.create('dbproyecto')
except:
    db = server['dbproyecto']

```

Finalmente se hace la obtención de datos mediante filtro de palabras: 

```
twitter_stream.filter(track=['delincuencia','violencia','robos','Quito'])

```

Una vez realizado la obtención de datos se verifico en la base de datos CouchDB :

![Esta es una imagen](![image](https://user-images.githubusercontent.com/74840012/156651676-7deeecae-13a5-4c02-8cef-1077274c0150.png)


Una vez que se verifico los datos se procedió a exportar en formato csv y de ahí se importó a la base de datos SQL server mediante interfaz gráfica.

Para ello lo primero que se realizo es crear una base de datos en SQL server :

```
CREATE DATABASE PROYECTO 

```

Una vez creada la base se importó : 


![Esta es una imagen](![image](https://user-images.githubusercontent.com/74840012/156651717-4308f242-8874-45d2-b27d-f4875a27ce1c.png)


Y verificamos que los datos se han importado correctamente con la función SELECT y el nombre de la tabla en la base de datos de SQL server : 

```
SELECT * FROM bdproyecto

```

![Esta es una imagen](![image](https://user-images.githubusercontent.com/74840012/156651756-66f7334d-e2e9-4478-815d-74be5fe53938.png)



Una vez importado los datos en SQL server se procedió a importar a la herramienta PowerBi y se realizó el análisis. 

Para ello hacemos conexión con el nombre de servidor y el nombre de la base de datos la cual se desea importar : 

![Esta es una imagen](![image](![image](https://user-images.githubusercontent.com/74840012/156651828-910e2097-94e3-4851-8103-bc0175923ee9.png)



A continuación, se hizo un filtrado por hashtag  y descripción según el tweet : 

![Esta es una imagen](![image](https://user-images.githubusercontent.com/74840012/156651857-8059745b-d341-4b74-877b-c1282046caec.png)

