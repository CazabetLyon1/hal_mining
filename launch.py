import requests
import json
from pymongo import MongoClient

def parseCursor(new_cursor):
    str1 = ""
    if new_cursor.find('=')!=-1:
        str1=new_cursor.replace('=', '%3D').find
    elif new_cursor.find('+')!=-1:
        str1=new_cursor.replace('+', '%2B')
    
    else:
        str1=str(new_cursor)
    return str1

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
quit = False
i=0
str2=''


while cursor != jsons['nextCursorMark']:
    
    print(jsons['nextCursorMark']+" "+cursor)
    print('\n')
    for item in jsons['response']['docs']:
        #database add
        col.insert_one(item)
    #2nd request init
    str2= parseCursor(jsons['nextCursorMark'])
    url = url.replace(cursor, str2)
    cursor = jsons['nextCursorMark']
    r=requests.request('GET', url) 
    jsons=json.loads(r.text)
   
       
client.close()
