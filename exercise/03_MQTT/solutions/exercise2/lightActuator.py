from MyMQTT import *
import time

class LightActuator:
    def __init__(self,clientID,broker,port,topic_subscribe,topic_publish):
        self.lightStatus = 0
        self.lightClientSub = MyMQTT(clientID,broker,port,self)
        self.__message={'client':clientID,'message':'','timestamp':''}
        self.topic_subscribe = topic_subscribe
        self.topic_publish = topic_publish

    def notify(self,topic,payload):
        message_json = json.loads(payload)
        if message_json["status"] == self.lightStatus:
            if self.lightStatus == 1:
                alert_to_sent=f'Be Aware. You try to turn ON the light, but it was already ON'
                self.publish(alert_to_sent)
                print (f'The Light was already ON at {time.ctime(message_json["timestamp"])}')
            else:
                alert_to_sent=f'Be Aware. You try to turn OFF the light, but it was already OFF'
                self.publish(alert_to_sent)
                print (f'The Light was already OFF at {time.ctime(message_json["timestamp"])}')
        else:
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
    
    def publish(self,message_to_sent):
        message=self.__message
        message['message']=message_to_sent
        message['timestamp']=time.time()
        self.lightClientSub.myPublish(self.topic_publish,message)
        print("Alert Sent!")

if __name__ == "__main__":
    clientID = "rafafontana12131997"
    broker = "mqtt.eclipseprojects.io"
    port = 1883
    #topic to subscribe
    topic_subscribe_lA = "IoT/rafafontana1234/led/set"
    topic_publish_lA = "IoT/rafafontana1234/led/alert"
    lightSub = LightActuator(clientID,broker,port,topic_subscribe_lA,topic_publish_lA)
    lightSub.startSim()
    try:
        while True:        
            time.sleep(10)
    except KeyboardInterrupt:
            lightSub.stopSim()