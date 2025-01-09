import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import json
import requests
import time
import cherrypy

class RESTBot:
    exposed=True
    def __init__(self, token):
        # Local token
        self.tokenBot = token
        # Catalog token
        # self.tokenBot=requests.get("http://catalogIP/telegram_token").json()["telegramToken"]
        self.bot = telepot.Bot(self.tokenBot)
        self.chatIDs=[]
        MessageLoop(self.bot, {'chat': self.on_chat_message}).run_as_thread()

    def on_chat_message(self, msg):
        content_type, chat_type, chat_ID = telepot.glance(msg)
        self.chatIDs.append(chat_ID)
        message = msg['text']
        if message=="/start":
            self.bot.sendMessage(chat_ID, text="Welcome to the Alert REST Bot. You are now registered. You will received new alerts when they arrive!")
        else:
            self.bot.sendMessage(chat_ID, text="Command not supported")

    def POST(self,*uri):
        tosend=''
        output={"status":"not-sent","message":tosend}
        if len(uri)!=0:
            if uri[0]=='temp':
                body=cherrypy.request.body.read()
                jsonBody=json.loads(body)
                alert=jsonBody["alert"]
                action=jsonBody["action"]
                tosend=f"ATTENTION!!!\n{alert}, you should {action}"
                output={"status":"sent","message":tosend}
                for chat_ID in self.chatIDs:
                    self.bot.sendMessage(chat_ID, text=tosend)
        return json.dumps(output)

if __name__ == "__main__":
    conf = json.load(open("settings.json"))
    token = conf["telegramToken"]
    cherryConf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True
		}
	}	
    bot=RESTBot(token)
    cherrypy.tree.mount(bot,'/',cherryConf)
    cherrypy.engine.start()
    cherrypy.engine.block()
