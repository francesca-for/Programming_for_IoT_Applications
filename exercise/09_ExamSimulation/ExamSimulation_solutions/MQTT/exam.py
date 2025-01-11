import paho.mqtt.client as PahoMQTT
import time
import json

class WCFCounter:

    def __init__(self, client_ID, broker, port, players_catalog):
        '''
        Catalog Structure
        {
            "playersList":[
                {
                    "name":"Kylian Mbappe",
                    "votes":0
                },
                {
                    "name":"Lionel Messi",
                    "votes":0
                }
            ]
        }
        '''
        self.paho = PahoMQTT.Client(client_ID, True)
        self.paho.on_connect = self.myOnConnect
        self.paho.on_message = self.myOnMessage
        self.broker = broker
        self.port = port
        self.client_ID = client_ID
        self.subs = []
        self.players_catalog= players_catalog

    def Start(self):
        self.paho.connect(self.broker, self.port)
        self.paho.loop_start()
        self.paho.subscribe("WCF/2022/votes",2)


    def Stop(self):
        for topic in self.subs:
            self.Unsubscribe(topic)
        self.paho.loop_stop()
        self.paho.disconnect()
        print("Disconnected")

    def myOnConnect(self, paho_mqtt, userdata, flags, rc):
        print(f"Connected to {self.broker} (port {self.port}) with request code: {rc}")

    def myOnMessage(self, paho_mqtt, userdata, msg):
        '''
        Message Structure
        {
            "players":["Kylian Mbappe", "Lionel Messi"]
        }
        '''
        # can read json.load(open("WCFvotes.json", 'r')) to get the players
        message_received= json.loads(msg.payload)
        votes_players= message_received['players']
        # or you assume always two players are voted
        voted_player1=votes_players[0]
        voted_player2=votes_players[1]
        for player in self.players_catalog["playersList"]:
            if player['name']==voted_player1:
                player['votes']+=1
            if player['name']==voted_player2:
                player['votes']+=1
        with open("WCFvotes.json", 'w') as f:
            json.dump(self.players_catalog, f)
        self.Publish()
        
    def Publish(self):
        msg= {
            "player":"",
            "percentage of votes":0    
        }
        total_votes=0
        votes_best_player=0
        best_player=""
        for player in self.players_catalog["playersList"]:
            total_votes+=player['votes']
            if player['votes']>votes_best_player:
                best_player=player['name']
                votes_best_player=player['votes']
        msg["player"]=best_player
        msg["percentage of votes"]=votes_best_player/total_votes*100
        self.paho.publish('WCF/2022/mostvoted', msg, 2)
        print(f"Published to 'WCF/2022/mostvoted' with QoS")


    def Subscribe(self, topic, QoS):
        if topic not in self.subs:
            self.paho.subscribe(topic, QoS)
            self.subs.append(topic)
            print(f"Subscribed to {topic} with QoS = {QoS}")
        else:
            print(f"Already subscribed to {topic}")

    def Unsubscribe(self, topic):
        if topic in self.subs:
            self.paho.unsubscribe(topic)
            self.subs.remove(topic)
            print(f"Unsubscribed from {topic}")
        else:
            print(f"Not yet subscribed to {topic}")

if __name__ == '__main__':
    f = open("settings.json", 'r')
    players_catalog= json.load(open("WCFvotes.json", 'r'))
    conf = json.load(f)
    sWT = WCFCounter("MyClientName", conf['broker'], conf['port'], players_catalog)
    sWT.Start()
    while True:
        time.sleep(5)

    sWT.Stop()