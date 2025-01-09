import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import json
import requests
import time
from MyMQTT import *

class MyBot:
    def __init__(self,token):
        # Local token
        self.tokenBot=token
        #Catalog token
        #self.tokenBot=requests.get("http://catalogIP/telegram_token").json()["telegramToken"]
        self.bot=telepot.Bot(self.tokenBot)
        MessageLoop(self.bot,{'chat': self.on_chat_message}).run_as_thread()

    def on_chat_message(self,msg):
        content_type, chat_type ,chat_ID = telepot.glance(msg)
        message=msg['text']
        if message=='/helloworld':
            self.bot.sendMessage(chat_ID,text="Command Hello World 🤓 ")
        else:
            self.bot.sendMessage(chat_ID,text="You sent:\n"+message)

class SimpleSwitchBot:
    def __init__(self,token,broker,port,topic_publish):
        self.tokenBot=token
        #Catalog token
        #self.tokenBot=requests.get("http://catalogIP/telegram_token").json()["telegramToken"]
        self.bot=telepot.Bot(self.tokenBot)
        self.client=MyMQTT("telegramBot12345rafa20241213",broker,port,None)
        self.client.start()
        self.topic_publish=topic_publish
        self.__message={'bn':"telegramBot",'e':[{'n':'switch','v':'', 't':'','u':'bool'}]}
        MessageLoop(self.bot,{'chat': self.on_chat_message}).run_as_thread()

    def on_chat_message(self,msg):
        content_type, chat_type ,chat_ID = telepot.glance(msg)
        message=msg['text']
        if message=="/switchon":
            payload=self.__message.copy()
            payload['e'][0]['v']="on"
            payload['e'][0]['t']=time.time()
            self.client.myPublish(self.topic_publish,payload)
            self.bot.sendMessage(chat_ID,text="Led switched on")
        elif message=="/switchoff":
            payload=self.__message.copy()
            payload['e'][0]['v']="off"
            payload['e'][0]['t']=time.time()
            self.client.myPublish(self.topic_publish,payload)
            self.bot.sendMessage(chat_ID,text="Led switched off")
        else:
            self.bot.sendMessage(chat_ID,text="Command not supported")
    

class FancyBot:
    def __init__(self,token,broker,port,topic_publish):
        self.tokenBot=token
        #Catalog token
        #self.tokenBot=requests.get("http://catalogIP/telegram_token").json()["telegramToken"]
        self.bot=telepot.Bot(self.tokenBot)
        self.client=MyMQTT("telegramBot12345rafa20241213",broker,port,None)
        self.client.start()
        self.topic_publish=topic_publish
        self.__message={'bn':"telegramBot",'e':[{'n':'switch','v':'', 't':'','u':'bool'}]}
        MessageLoop(self.bot, {'chat': self.on_chat_message,'callback_query': self.on_callback_query}).run_as_thread()
    
    def on_chat_message(self,msg):
        content_type, chat_type ,chat_ID = telepot.glance(msg)
        message=msg['text']
        '''
        if message=="/switchon":
            payload=self.__message.copy()
            payload['e'][0]['v']="on"
            payload['e'][0]['t']=time.time()
            self.client.myPublish(self.topic_publish,payload)
            self.bot.sendMessage(chat_ID,text="Led switched on")
        elif message=="/switchoff":
            payload=self.__message.copy()
            payload['e'][0]['v']="off"
            payload['e'][0]['t']=time.time()
            self.client.myPublish(self.topic_publish,payload)
            self.bot.sendMessage(chat_ID,text="Led switched off")
        else:
            self.bot.sendMessage(chat_ID,text="Command not supported")
        '''
        if message=="/switch":
            buttons=[[InlineKeyboardButton(text=f'ON ✅',callback_data=f'on'),InlineKeyboardButton(text=f'OFF ',callback_data=f'off')]]
            keyboard=InlineKeyboardMarkup(inline_keyboard=buttons)
            self.bot.sendMessage(chat_ID,text="What do you want to do with the led?", reply_markup=keyboard)
        else:
            self.bot.sendMessage(chat_ID,text="Command not supported")

    
    def on_callback_query(self,msg):
        query_ID , chat_ID , query_data = telepot.glance(msg,flavor='callback_query')
        payload = self.__message.copy()
        payload['e'][0]['v'] = query_data
        payload['e'][0]['t'] = time.time()
        self.client.myPublish(self.topic_publish, payload)
        self.bot.sendMessage(chat_ID, text=f"Led switched {query_data}")


if __name__=="__main__":
    configuration=json.load(open('config.json'))
    token_bot=configuration['token']
    mqtt_broker=configuration['mqtt_broker']
    mqtt_port=configuration['mqtt_port']
    topic_publish=configuration['topic_publish']
    #myboy=MyBot(token_bot)
    #switchbot=SimpleSwitchBot(token_bot,mqtt_broker,mqtt_port,topic_publish)
    fancybotrafa=FancyBot(token_bot,mqtt_broker,mqtt_port,topic_publish)
    while True:
        time.sleep(3)