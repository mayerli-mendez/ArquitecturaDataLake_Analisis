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




