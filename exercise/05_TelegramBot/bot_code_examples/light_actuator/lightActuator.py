from MyMQTT import *
import time
import json

class lightActuator:
    def __init__(self,clientID,broker,port,topic_subscribe):
        self.clientID=clientID
        self.broker=broker
        self.port=port
        self.topic_subscribe=topic_subscribe
        self.lightActuatorClient=MyMQTT(clientID,broker,port,self)

    def notify(self,topic,payload):
        '''
        {'bn':"telegramBot",
         'e':[
            {'n':'switch','v':'', 't':','u':'bool'},
        ]
        }
        '''
        payload=json.loads(payload)
        self.status=payload['e'][0]['v']
        client=payload['bn']
        timestamp=payload['e'][0]['t']
        print(f'The led has been set to {self.status} at time {timestamp} by the client {client}')
        
    def startSim(self):
        self.lightActuatorClient.start()
        self.lightActuatorClient.mySubscribe(self.topic_subscribe)
    
    def stopSim(self):
        self.lightActuatorClient.unsubscribe()
        self.lightActuatorClient.stop()

if __name__=="__main__":
    config=json.load(open('config.json'))
    broker=config['mqtt_broker']
    port=config['mqtt_port']
    clientid='simpleSubscriberrafa1256789'
    topic=config['topic_subscribe']
    client_simplesub=lightActuator(clientid,broker,port,topic)
    client_simplesub.startSim()
    while True:
        time.sleep(5)
