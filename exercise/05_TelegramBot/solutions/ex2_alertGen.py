from MyMQTT import *
import time
import json

class AlertGenerator:
    def __init__(self,clientID,broker,port,topic_publish):
        self.clientID=clientID
        self.broker=broker
        self.port=port
        self.topic_publish=topic_publish
        self.alertGeneratorClient=MyMQTT(clientID,broker,port,None)
        self.__message={"alert":"","action":"","timestamp":""}
        
    def startSim(self):
        self.alertGeneratorClient.start()
    
    def stopSim(self):
        self.alertGeneratorClient.stop()
    
    def publish(self,alert_text,action_text):
        message_to_send=self.__message
        message_to_send['alert']=alert_text
        message_to_send['action']=action_text
        message_to_send['timestamp']=time.time()
        self.alertGeneratorClient.myPublish(self.topic_publish,message_to_send)
        print("Alert Sent!")

if __name__=="__main__":
    broker='mqtt.eclipseprojects.io'
    port=1883
    clientid="alertGenerator1245654"
    topic="rafafontana/alert/temp1"
    client_simplepub=AlertGenerator(clientid,broker,port,topic)
    client_simplepub.startSim()
    print('Welcome to Alert Manual Generator')
    message_to_print='Type:\n First, type the alert you want to send, then the action that should be performed \n Type "q" to end'
    while True:
        print(message_to_print)
        user_input_alert=input("Enter the alert: ")
        user_input_action=input("Enter the action to be perfomed: ")
        if user_input_alert.lower()=='q' or user_input_action.lower()=='q':
            break
        else:
            client_simplepub.publish(user_input_alert,user_input_action)