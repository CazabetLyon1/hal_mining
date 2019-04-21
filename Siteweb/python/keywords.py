from pymongo import MongoClient
import json

def decoupeTitre(titre , liste, countKW):
    titre.replace('\'', ' ')
    listeTitre = str.split(' ')
    for x in listeTitre:
        if  len(x)>3:
            if x in liste:
                countKW[liste.index(x)] += 1
            else:
                liste.append(x)
                countKW.append(1)
                print(len(liste))
    
   
            
def KWClassement():
    dico={}
    i=0
    max = 0
    idMax=0
    print(len(countKW))
    while i < 10:
        for it in countKW:
            if it>max:
                max=it
                idMax = countKW.index(it)
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
        print(x['labStructAddress_s'])
        s=str(x['labStructAddress_s'])
        print((s.find('Lyon'))!=-1 or (s.find('Villeurbanne'))!=-1)
        if(('Lyon' or 'Villeurbanne')in s):
            strin =y
            decoupeTitre(strin, listeKW, countKW)
    

d= KWClassement()
print(d)
    

