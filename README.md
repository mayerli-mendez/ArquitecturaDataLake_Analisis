
![Esta es una imagen](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Fepnecuador-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!YP5u9sklC0iywPgRepMQVOdg8BAkAQlLoHr_GSobHaPNJuBAAf_VQKAw4x81bXaz%2Fitems%2F01PVDBQAZSCPQRHYHJBNCL2G3IKVMLQF5F%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZXBuZWN1YWRvci1teS5zaGFyZXBvaW50LmNvbUA2ODJhNGU2YS1hNzdmLTQ5NTgtYTNhYy05ZTI2NmQxOGFhMzciLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNjQ2MDkyODAwIiwiZXhwIjoiMTY0NjExNDQwMCIsImVuZHBvaW50dXJsIjoiTWwyby9jRUxiSDVZQ0NNcy9JeVlTQjBNM1VnY0ZVVDZKZk5kd2hITUZBQT0iLCJlbmRwb2ludHVybExlbmd0aCI6IjEyMCIsImlzbG9vcGJhY2siOiJUcnVlIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6IlpqWTJaV1psTmpBdE1qVmpPUzAwT0RCaUxXSXlZekF0WmpneE1UZGhPVE14TURVMCIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8bWF5ZXJsaS5tZW5kZXpAZXBuLmVkdS5lYyIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfDEwMDMyMDAwNzEyOGU5ZmNAbGl2ZS5jb20iLCJzZXNzaW9uaWQiOiI0NDQ2NjI5MC0yYmRjLTQyNjQtOTc0Yi1hMjM0NjNiYjI2MWEiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMyIsImlwYWRkciI6IjE1Ny4xMDAuMTcwLjExOCJ9.LzZIR2FuM09jdTBKNlFvc3lFVlJ0NytOcUp0d3BMM1pTTUl6djlvZTNzWT0&cTag=%22c%3A%7B13E11332-E9E0-440B-BD1B-685558B817A5%7D%2C1%22&encodeFailures=1&width=1366&height=581&srcWidth=&srcHeight=)

La  fuente 8 consiste en obtener datos de Noticias o Eventos del mundo mediante WebScraping, estos datos se guardaran en la base de datos MongoDB, luego se exportaran a la base de datos MySQL y, finalmente se analizarán los datos obtenidosmediante el uso de la herramienta PowerBi..

Inspeccionamos nuestra página web, en este caso sera: https://www.bbc.com/mundo/topics/c2lej05epw5t
![image](https://user-images.githubusercontent.com/74751902/156231688-3c0840ad-4c15-4454-abf7-9b24e4b1001a.png)


El primer paso que debemos seguir, luego de haber inspeccionado nuestra página web, es exportar nuestras librerias:

```
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
```

Una vez exportadas las librerias, ejecutamos nuestro driver.

```
driver = webdriver.Chrome(executable_path=r'C:/Users/Usuario/chromedriver.exe')
```

Es importante que se indique la ruta en donde se encuentra descargado nuestro driver.

Luego indicamos la página de donde obtendremos nuestros datos utilizando el driver.

```
driver.get("https://www.bbc.com/mundo/topics/c2lej05epw5t")
```

Procedemos a recolectar nuestros datos, para ello haremos uso de las etiquetas donde se encontraban los datos que visualizamos en el Inspeccionar con sus respectivas clases.
Una vez recolectados, imprimiremos nuestros datos para verificar que se encuentren correctos (si no es el caso, verificar que las etiquetas esten correctas con sus respectivas clases).

```
count = 0
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('li',{'class':'lx-stream__post-container'}):
    contenido = a.find('p',{'class':'lx-stream-related-story--summary qa-story-summary'}).getText()
    title = a.find('span',{'class':'lx-stream-post__header-text gs-u-align-middle'}).getText()
    hora = a.find('span',{'class':'qa-post-auto-meta'}).getText()
    autor = a.find('p',{'class':'qa-contributor-name lx-stream-post__contributor-name gel-long-primer gs-u-m0'}).getText()
    fuente = a.find('p',{'class':'qa-contributor-role lx-stream-post__contributor-description gel-brevier gs-u-m0'}).getText()
    
    #IMPRIMIR LOS RESULTADOS
    count = count+1
    print('Noticia ',count)
    print ('\033[1mFecha y hora de publicación: \033[0m',hora)
    print ('\033[1mAutor: \033[0m',autor)
    print ('\033[1mFuente: \033[0m',fuente)
    print ('\033[1mTitulo: \033[0m',title)
    print ('\033[1mContenido: \033[0m',contenido)
    print()
```

![image](https://user-images.githubusercontent.com/74751902/156231983-41bd8250-8267-41fb-8097-a365e34af6f8.png)



Visto que nuestros datos se encuentran correctos, procederemos a enviar nuestros datos a MongoDB, para ello exportamos nuestra libreria pymongo, la cual nos permitira realizar la conexión con nuestra base:

```
from pymongo import MongoClient
```

Luego nos conectamos con MongoDB y creamos nuestra base de datos que en este caso se llamará 'Noticias_Mundo' junto con la colección que se llamaará "nuevo". 

```
client = MongoClient("localhost", 27017)
dbs=client["Noticias_Mundo"] 
db=dbs.nuevo
```

El procedimiento para enviar los datos es como el que realizamos anteriormente. Sin embargo en esta ocasión no imprimiremos los datos, sino que los guardaremos en una lista llamada "doc", misma que será enviada mediante la linea de comando "db.insert_one(doc)".

```
count = 0
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('li',{'class':'lx-stream__post-container'}):
    contenido = a.find('p',{'class':'lx-stream-related-story--summary qa-story-summary'}).getText()
    title = a.find('span',{'class':'lx-stream-post__header-text gs-u-align-middle'}).getText()
    hora = a.find('span',{'class':'qa-post-auto-meta'}).getText()
    autor = a.find('p',{'class':'qa-contributor-name lx-stream-post__contributor-name gel-long-primer gs-u-m0'}).getText()
    fuente = a.find('p',{'class':'qa-contributor-role lx-stream-post__contributor-description gel-brevier gs-u-m0'}).getText()
    
    doc={}
    doc['id']= count
    doc['Fecha y hora de publicación'] = hora
    doc['Autor'] = autor
    doc['Fuente'] = fuente
    doc['Titulo'] = title
    doc['Contenido'] = contenido
    db.insert_one(doc)
```

Verificamos que los datos se encuentren en nuestra base de datos

![image](https://user-images.githubusercontent.com/74751902/156232973-2e89af6a-83f3-4273-ab62-b2fefd1fd066.png)


Ahora procederemos a enviar nuestros datos a MySQL, para ello descargaremos nuestros datos de MongoDB en un formato CSV 

![image](https://user-images.githubusercontent.com/74751902/156233310-1a26ef0f-3234-4411-a92b-5a4f5cf8ae82.png)


Luego exportamos nuestras librerias que serviran para la conexión con MySQL

```
import json
import pymongo
import pandas as pd
import pymysql
from sqlalchemy import create_engine
```

Y finalmente, mediante el siguiente código nos conectaremos con MySQL especificamente a nuestra base de datos llamada "web", está debe estar previamente creada.
Luego procederemos a leer los datos de nuestro archivo .csv que descargamos previamente de MongoDB y los enviaremos a  una tabla llamada "BBCNews" con los campos que teniamos en nuestro archivo.

```
cadenacon='mysql+pymysql://root:casa@localhost:3306/web'
engine=create_engine(cadenacon)
df=pd.read_csv("nuevo.csv")
print (df)
df.to_sql("BBCNews",con=engine,if_exists="replace")
```

Al ejecutar dicho código obtendremos lo siguiente: 

![image](https://user-images.githubusercontent.com/74751902/156234518-f8541424-9ac3-4063-b52c-b4e9dc8ec68c.png)

Verificamos los datos en MySQL 

![image](https://user-images.githubusercontent.com/74751902/156440309-241b6b3c-4e49-436b-800f-a0bd38f26cf5.png)

Y como podemos observar se agregaron correctamente los datos a MySQL
