import requests
import json
import urllib
from pymongo import MongoClient


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
filtres ='&fl=docid, title_s,docType_s,authFullName_s, ePublicationDate_tdate, domain_s, domainAllCode_s, structName_s, languages_s'

cursor= "*"

url='https://api.archives-ouvertes.fr/search/?q=city_s:Lyon'+filtres+'&rows=10000&sort=docid%20asc&cursorMark='+cursor

r = requests.request('GET',url)
jsons=json.loads(r.text)


while cursor != jsons['nextCursorMark']:
  
   for item in jsons['response']['docs']:
       
       #database add    
       if col.count_documents({"docid": item['docid']}) == 0:
           col.insert(item)
           print("insert success")

       else:
           print('Ce document a déjà été ajouté')                   
  
   #2nd request init
   tmpCurs = urllib.parse.quote(jsons['nextCursorMark'])
   url= url.replace(cursor,tmpCurs)
   cursor = tmpCurs
   r=requests.request('GET', url) 
   jsons=json.loads(r.text)


client.close()


