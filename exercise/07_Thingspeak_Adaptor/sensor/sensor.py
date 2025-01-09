import cherrypy
import requests
import json
import random
import time
import threading
import uuid
from MyMQTT import *

class SensorREST_MQTT(threading.Thread):
    exposed = True

    def __init__(self, pi):
        threading.Thread.__init__(self)
        self.settings = json.load(open('settings.json'))
        self.catalogURL=self.settings['catalogURL']
        self.deviceInfo=self.settings['deviceInfo']
        self.deviceInfo['ID'] = random.randint(1, 1000)
        self.deviceID=self.deviceInfo['ID']
        self.deviceInfo['commands'] = ['hum', 'temp']
        self.pingInterval = pi
        #mqtt configurations
        self.mqtt_data=self.settings['mqtt_data']
        self.topic_publish=self.mqtt_data['mqtt_topic_publish']
        self.broker=self.mqtt_data['broker']
        self.port=self.mqtt_data['port']
        self.clientID=str(uuid.uuid1())
        self.client=MyMQTT(self.clientID,self.broker,self.port,None)
        self.__message_temperature={'bn':f'SensorREST_MQTT_{self.deviceID}','e':[{'n':'temperature','v':'', 't':'','u':'cel'}]}
        self.__message_humidity={'bn':f'SensorREST_MQTT_{self.deviceID}','e':[{'n':'humidity','v':'', 't':'','u':'%'}]}
        requests.post(f'{self.catalogURL}/devices', data=json.dumps(self.deviceInfo))
        self.start()  # related to the mqtt part. We start the thread -> we must have a method run

    def read_humidity_value(self):
        value_hum=random.randint(60,80)
        return value_hum
    
    def read_temperature_value(self):
        value_temperature=random.randint(10,25)
        return value_temperature

    def startSim(self):
        self.client.start()
    
    def stopSim (self):
        self.client.stop()
    
    def publish (self):
        # read and publish temperature measurement
        message_temperature=self.__message_temperature
        message_temperature['e'][0]['v']=self.read_temperature_value()
        message_temperature['e'][0]['t']=time.time()
        self.client.myPublish(f'{self.topic_publish}/{self.deviceID}/temperature',message_temperature)
        print(f"published Message: \n {message_temperature}")
        
        # read and publish humidity measurement
        message_humidity=self.__message_humidity
        message_humidity['e'][0]['v']=self.read_humidity_value()
        message_humidity['e'][0]['t']=time.time()
        self.client.myPublish(f'{self.topic_publish}/{self.deviceID}/humidity',message_humidity)
        print(f"published Message: \n {message_humidity}")

    def GET(self, *uri, **params):
        if len(uri) != 0:
            if uri[0] == 'hum':
                message=self.__message_humidity
                message['e'][0]['v']=self.read_humidity_value()
                message['e'][0]['t']=time.time()
            if uri[0] == 'temp':
                message=self.__message_temperature
                message['e'][0]['v']=self.read_temperature_value()
                message['e'][0]['t']=time.time()
            return json.dumps(message)
        else:
            return json.dumps(self.deviceInfo)

    def run(self):
        self.startSim()
        while True:
            time.sleep(self.pingInterval)
            self.pingCatalog()
            self.publish()
    
    def pingCatalog(self):
        requests.put(f'{self.catalogURL}/devices', data=json.dumps(self.deviceInfo))


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    s = SensorREST_MQTT(30)
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 80})
    #cherrypy.config.update({'server.socket_port': 9090})
    cherrypy.tree.mount(s, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
    cherrypy.engine.exit()
