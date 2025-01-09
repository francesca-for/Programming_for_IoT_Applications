import json
import time

import requests
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup

from MyMQTT import *


class MQTTbot:
    def __init__(self,token,clientID,broker,port,topic):
        # Local token
        self.tokenBot = token
        # Catalog token
        # self.tokenBot=requests.get("http://catalogIP/telegram_token").json()["telegramToken"]
        self.bot = telepot.Bot(self.tokenBot)
        self.chatIDs=[]
        self.client = MyMQTT(clientID, broker, port, self)
        self.client.start()
        self.topic = topic
        self.client.mySubscribe(topic)
        MessageLoop(self.bot, {'chat': self.on_chat_message}).run_as_thread()

    def on_chat_message(self, msg):
        content_type, chat_type, chat_ID = telepot.glance(msg)
        self.chatIDs.append(chat_ID)
        message = msg['text']
        if message=="/start":
            self.bot.sendMessage(chat_ID, text="Welcome to the Alert MQTT Bot. You are now registered. You will received new alerts when they arrive!")
        else:
            self.bot.sendMessage(chat_ID, text="Command not supported")
        
    def notify(self,topic,message):
        print(message)
        msg=json.loads(message)
        
        alert=msg["alert"]
        action=msg["action"]
        tosend=f"ATTENTION!!!\n{alert}, you should {action}"
        for chat_ID in self.chatIDs:
            self.bot.sendMessage(chat_ID, text=tosend)

if __name__ == "__main__":
    conf = json.load(open("settings.json"))
    token = conf["telegramToken"]
    broker = conf["brokerIP"]
    port = conf["brokerPort"]
    topic = conf["mqttTopicAlert"]
    mqttclientID = "telegramBotIoT1987254"
    sb=MQTTbot(token,mqttclientID,broker,port,topic)
    while True:
        time.sleep(3)
