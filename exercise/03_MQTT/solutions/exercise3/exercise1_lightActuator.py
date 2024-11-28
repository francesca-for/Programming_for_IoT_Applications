from MyMQTT import *
import time

class LightActuator:
    def __init__(self,clientID,broker,port,topic_subscribe):
        self.lightStatus = "OFF"
        self.lightClientSub = MyMQTT(clientID,broker,port,self)
        self.topic_subscribe = topic_subscribe

    def notify(self,topic,payload):
        message_json = json.loads(payload)
        self.lightStatus = message_json["status"]
        if self.lightStatus == 1:
            print (f'The Light was turned ON at {time.ctime(message_json["timestamp"])}')
        else:
            print (f'The Light was turned OFF at {time.ctime(message_json["timestamp"])}')
            
    def startSim(self):
        self.lightClientSub.start()
        self.lightClientSub.mySubscribe(self.topic_subscribe)
    
    def stopSim(self):
        self.lightClientSub.unsubscribe()
        self.lightClientSub.stop()

if __name__ == "__main__":
    clientID = "rafafontana12131997"
    broker = "mqtt.eclipseprojects.io"
    port = 1883
    #topic to subscribe
    topic_subscribe_lA = "IoT/rafafontana1234/led/set"
    lightSub = LightActuator(clientID,broker,port,topic_subscribe_lA)
    lightSub.startSim()
    try:
        while True:        
            time.sleep(10)
    except KeyboardInterrupt:
            lightSub.stopSim()