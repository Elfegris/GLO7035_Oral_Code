# docker run -d -it --name MyRedis -p:6379:6379 redis
# docker run -d -it --name MyMongo  -p:27017:27017 mongo

import redis
import time
#########################################################################
# Test de la fonctionnalité de souscription/publication (subscribe/publish)                                  #
#########################################################################


##########################################################
# Ce code ecoute le canal "Trump" et le canal "Trudeau"  #
##########################################################

print("\nMacron")
time.sleep(1)

# Connection avec la Bd redis
Macron = redis.StrictRedis(host='redis', port=6379, db=0)
MacronPS = Macron.pubsub()
MacronPS.subscribe('Trump')
MacronPS.subscribe('Trudeau')

while(True):
    time.sleep(0.1)
    new_Tweet = MacronPS.get_message()
    if new_Tweet:
        if new_Tweet['type'] == 'message':
            print("Recu le message: " +
                  new_Tweet['data'].decode("utf-8") + " du canal de: " + new_Tweet['channel'].decode("utf-8"))
