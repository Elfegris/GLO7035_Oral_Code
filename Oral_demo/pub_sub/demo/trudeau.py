# docker run -d -it --name MyRedis -p:6379:6379 redis
# docker run -d -it --name MyMongo  -p:27017:27017 mongo

import redis
import time
import threading
#########################################################################
# Test de la fonctionnalité de souscription/publication (subscribe/publish)                                  #
#########################################################################


##########################################
# Ce code publie dans le canal "Trudeau" #
# et écoute le canal "Trump"             #
##########################################

print("\Trudeau")
time.sleep(1)


def LectureMSG():

    Trudeau = redis.StrictRedis(host='redis', port=6379, db=0)
    TrudeauPS = Trudeau.pubsub()
    TrudeauPS.subscribe('Trump')

    while(True):
        time.sleep(0.1)
        new_Tweet = TrudeauPS.get_message()
        if new_Tweet:
            if new_Tweet['type'] == 'message':
                print("Recu le message: " + new_Tweet['data'].decode(
                    "utf-8") + " du canal de: " + new_Tweet['channel'].decode("utf-8"))


threading.Thread(target=LectureMSG, name='worker-Trideai').start()
Trudeau = redis.StrictRedis(host='redis', port=6379, db=0)

for i in range(10):
    time.sleep(1)
    Trudeau.publish('Trudeau', f"Message #{i} de Trudeau")
