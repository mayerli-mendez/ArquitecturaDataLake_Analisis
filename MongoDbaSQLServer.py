from lib2to3.pgen2.driver import Driver
import pyodbc
import pandas as pd
import pymongo
import json

client=pymongo.MongoClient('mongodb://localhost:27017')
db = client.get_database('JuegosUbisoft')
collection = db.get_collection('BlackFlag')
# Get a df with full collection:
df = pd.DataFrame(list(collection.find()))
## Exportar a Excel o CSV:
df.to_csv('AssasinsCreed4.csv', index=False,)
#df.to_excel('AssasinsCreed4.xlsx', index=False)
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
