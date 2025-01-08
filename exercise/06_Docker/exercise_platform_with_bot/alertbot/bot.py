import json
import time

import requests
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup

from MyMQTT import *


class MQTTbot:
    def __init__(self,settings):
        # config
        self.catalogURL=settings['catalogURL']
        self.serviceInfo=settings['serviceInfo']
        self.tokenBot = settings['serviceInfo']['token']
        # MQTT config
        self.clientID=settings['mqttData']['mqttclientID']
        self.broker=settings['mqttData']['brokerIP']
        self.port=settings['mqttData']['brokerPort']
        self.topic_subscribe=settings['mqttData']['mqttTopicAlert']
        # run bot
        self.bot = telepot.Bot(self.tokenBot)
        self.chatIDs=[]
        self.botmqttclient = MyMQTT(self.clientID, self.broker, self.port, self)
        self.botmqttclient.start()
        self.botmqttclient.mySubscribe(self.topic_subscribe)
        time.sleep(5)
        self.registerService()
        MessageLoop(self.bot, {'chat': self.on_chat_message}).run_as_thread()
    
    def notify(self,topic,message):
        print(message)
        msg=json.loads(message)
        alert=msg["alert"]
        action=msg["action"]
        tosend=f"ATTENTION!!!\n{alert}, you should {action}"
        for chat_ID in self.chatIDs:
            self.bot.sendMessage(chat_ID, text=tosend)

    def on_chat_message(self, msg):
        content_type, chat_type, chat_ID = telepot.glance(msg)
        message = msg['text']
        if message=="/start":
            if chat_ID not in self.chatIDs:
                self.chatIDs.append(chat_ID)
                self.bot.sendMessage(chat_ID, text="Welcome to the Alert MQTT Bot. You are now registered. You will received new alerts when they arrive!")
            else:
                self.bot.sendMessage(chat_ID, text="You are already registered")
        else:
            self.bot.sendMessage(chat_ID, text="Command not supported")
    
    def stopSim(self):
        self.botmqttclient.unsubscribe()
        self.botmqttclient.stop()
    
    def registerService(self):
        print('Starting Alert Bot')
        time.sleep(5)
        self.serviceInfo['last_update']=time.time()
        requests.post(f'{self.catalogURL}/services',data=json.dumps(self.serviceInfo))
    
    def updateService(self):
        self.serviceInfo['last_update']=time.time()
        requests.put(f'{self.catalogURL}/services',data=json.dumps(self.serviceInfo))

if __name__ == "__main__":
    configurations_settings = json.load(open("settings.json"))
    sb=MQTTbot(configurations_settings)
    while True:
        try:
            time.sleep(3)
            sb.updateService()
        except KeyboardInterrupt:
            sb.stopSim()
            break