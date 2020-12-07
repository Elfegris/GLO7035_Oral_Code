# docker run -d -it --name MyRedis -p:6379:6379 redis
# docker run -d -it --name MyMongo  -p:27017:27017 mongo

import redis
import time
#########################################################################
# Test de la fonctionnalité de souscription/publication (subscribe/publish)                                  #
#########################################################################


##########################################
# Ce code publie dans le canal "Trump"   #
# et écoute aucun canal                  #
##########################################

print('\nTrump')
time.sleep(1)

# Connection avec la Bd redis
Trump = redis.StrictRedis(host='redis', port=6379, db=0)
for i in range(10):
    time.sleep(1)
    Trump.publish('Trump', f"Message #{i} de Trump")
