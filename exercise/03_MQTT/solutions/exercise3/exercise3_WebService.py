import cherrypy
import os
from exercise1_lightManager import *

class LightREST(object):
	exposed=True
	def __init__(self):
		conf=json.load(open("settings.json"))
		broker=conf["broker"]
		port=conf["port"]
		topic_publish="IoT/rafafontana1234/led/set"
		self.light_client=LightManager("rafafontana_lightpublisher",broker,port,topic_publish)
		self.light_client.startSim()
	def GET(self):
		return open('index.html')
	def PUT(self, *uri):
		command=uri[0]
		self.light_client.publish(command)
		

if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tools.sessions.on':True,
				'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		#You need to include the part below if you want to activate the css and give to the button a nicer look
		'/css':{
				'tools.staticdir.on': True,
				'tools.staticdir.dir':'./css'
		}
	}		
	cherrypy.tree.mount(LightREST(),'/',conf)
	cherrypy.engine.start()
