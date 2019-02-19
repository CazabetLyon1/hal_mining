from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/");
print("Connection Successful")
db = client.DATABASETEST

#TEST DATABASE
dblist = client.list_database_names()
print(dblist)
if "DATABASETEST" in dblist:
  print("The database exists.")


#TEST COLLECTION
collist = db.list_collection_names()
if "customers" in collist:
  print("The collection exists.")


#INSERTION DOC JSON
page = open("testCursor.json",'r')
parsed = json.loads(page.read())
for item in parsed["response"]["docs"]:
    col.insert(item)

client.close()
