from pymongo import MongoClient
import json

def decoupeTitre(titre , liste, countKW):
    titre.replace('\'', ' ')
    titre.replace(',', ' ')
    listeTitre = str.split(' ')
    print(listeTitre[0])
    for x in listeTitre:
        print(x)
        if  len(x)>3:
            if x in liste:
                countKW[liste.index(x)] += 1
            else:
                try:
                    liste.append(x)
                    countKW.append(1)
                    print(len(liste))
                except IndexError:
                    print(IndexError)
   
            
def KWClassement():
    dico={}
    i=0
    max = 0
    idMax=0
    while i < 10:
        for it in countKW:
            print(it)
            if countKW[it]>max:
                max=countKW[it]
                print(max)
                idMax = it
        dico[str(i)] = listeKW[idMax]
        i+=1
    return dico

#recup docs
cli = MongoClient("mongodb://localhost:27017/")
print("Connection Successful")
db = cli.DATABASETEST
col =db["articles"]

listeKW=[]
countKW=[]

for x in col.find({"labStructName_s": {'$exists': 1},  "labStructAddress_s": {'$exists': 1}}):
    for y in x['title_s']:
        
        s=str(x['labStructAddress_s'])
        if(('Lyon' or 'Villeurbanne' or "BRON")in s):
           
            decoupeTitre(y, listeKW, countKW)
    

d= KWClassement()
print(d)
    

