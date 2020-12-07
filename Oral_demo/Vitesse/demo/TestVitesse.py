# docker run -d -it --name MyRedis -p:6379:6379 redis
# docker run -d -it --name MyMongo  -p:27017:27017 mongo

import redis
import pymongo
import time
import random
#########################################################################
# Test de vitesse entre les base de données Redis et Mondgo             #
# Dans les 2 cas, on écris un certain nombre de document "Clé:valeur"   #
# sous la formes {"entier":"entier"}                                    #
#########################################################################
# il faut monter des docker pour Redis Mongo
# docker run -d -it --name MyRedis -p:6379:6379 redis
# nc -v localhost 6379

# docker run -d -it --name MyMongo  -p:27017:27017 mongo


NbrWrite = 5000  # Nombre d'écriture
NbrRead = 5000  # Nombre de lecture

# Création du tableau de lecture  aléatoire
randomlist = []
for i in range(NbrRead):
    n = random.randint(0, NbrWrite-1)
    randomlist.append(n)


##############################
# Test de vitesse pour Redis #
##############################

print('\nRedis SpeedTest')
time.sleep(1)

# Connection avec la Bd redis
#r = redis.StrictRedis(host='localhost', port=6379, db=0)
r = redis.StrictRedis(host='redis', port=6379, db=0)


# Test de vitesse en écriture
start_time = time.time()

for x in range(NbrWrite):
    r.set(x, x)

print("     Temps nécessaire pour %.0f écritures = %.1f seconds" %
      (NbrWrite, (time.time() - start_time)))


# Test de vitesse en lecture aléatoire
start_time = time.time()

for x in randomlist:
    r.get(x)

print("     Temps nécessaire pour %.0f Lectures aléatoires = %.1f seconds" %
      (NbrRead, (time.time() - start_time)))

# efface les données question de toujours démaré dans la même situation
for x in range(NbrWrite):
    r.delete(x)


##############################
# Test de vitesse pour mongo #
##############################
print('\nMongo SpeedTest')
# Connection avec la Bd Mongo
#Client = pymongo.MongoClient("localhost:27017")
Client = pymongo.MongoClient("mongodb:27017")
db = Client.Oral
SpeedTest = db.SpeedTest

# Test de vitesse en écriture
start_time = time.time()

for x in range(NbrWrite):
    SpeedTest.insert_one({str(x): str(x)})

print("     Temps nécessaire pour %.0f écritures = %.1f seconds" %
      (NbrWrite, (time.time() - start_time)))


# Test de vitesse en lecture aléatoire
start_time = time.time()
for x in randomlist:
    SpeedTest.find_one({str(x): {'$exists': 1}})

print("     Temps nécessaire pour %.0f Lectures aléatoires = %.1f seconds" %
      (NbrRead, (time.time() - start_time)))

# efface les données question de toujours démaré dans la même situation
for x in range(NbrWrite):
    SpeedTest.delete_one({str(x): {'$exists': 1}})
