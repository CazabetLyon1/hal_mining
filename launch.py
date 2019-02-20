import requests
import json
from pymongo import MongoClient
import urllib

##MongoDB  Database creation 
client = MongoClient("mongodb://localhost:27017/")
print("Connection Successful")
db = client.DATABASETEST

    #TEST DATABASE
dblist = client.list_database_names()
print(dblist)
if "DATABASETEST" in dblist:
  print("Database creation successfull." )

col = db["articles"]
collist = db.list_collection_names()
if "articles" in collist:
  print("The collection exists.")

## init requete
filtres ="&fl=title_s, docType_s, authFullName_s, ePublicationDate_tdate, domain_s, domainAllCode_s, structName_s, languages_s"
cursor= "*"
url='https://api.archives-ouvertes.fr/search/?q=city_s:Lyon'+filtres+'&rows=10000&sort=docid%20asc&cursorMark='+cursor

r = requests.request('GET',url)
jsons=json.loads(r.text)

while cursor != jsons['nextCursorMark']:
  
    for item in jsons['response']['docs']:
        #database add
        col.insert_one(item)
    #2nd request init
    str2 = urllib.parse.quote(jsons['nextCursorMark'])
    url= url.replace(cursor,str2)
    cursor = str2

    r=requests.request('GET', url) 
    jsons=json.loads(r.text)
  
       
client.close()
