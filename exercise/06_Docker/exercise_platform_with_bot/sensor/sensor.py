import cherrypy
import requests
import json
import random
import time
import threading

class SensorREST(threading.Thread):
    exposed = True

    def __init__(self, pi):
        threading.Thread.__init__(self)
        self.settings = json.load(open('settings.json'))
        self.catalogURL=self.settings['catalogURL']
        self.deviceInfo=self.settings['deviceInfo']
        self.deviceInfo['ID'] = random.randint(1, 1000)
        self.deviceInfo['commands'] = ['hum', 'temp']
        self.pingInterval = pi
        time.sleep(5)
        requests.post(f'{self.catalogURL}/devices', data=json.dumps(self.deviceInfo))
        self.start()

    def GET(self, *uri, **params):
        if len(uri) != 0:
            if uri[0] == 'hum':
                value = random.randint(60, 80)
            if uri[0] == 'temp':
                value = random.randint(10, 25)
            output = {'deviceID': self.deviceInfo['ID'], str(uri[0]): value}
            return json.dumps(output)
        else:
            return json.dumps(self.deviceInfo)

    def run(self):
        while True:
            time.sleep(self.pingInterval)
            self.pingCatalog()
    
    def pingCatalog(self):
        requests.put(f'{self.catalogURL}/devices', data=json.dumps(self.deviceInfo))


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    s = SensorREST(5)
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 9090})
    #cherrypy.config.update({'server.socket_port': 9090})
    cherrypy.tree.mount(s, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
    cherrypy.engine.exit()
