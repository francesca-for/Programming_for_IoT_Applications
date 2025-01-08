import requests
import json
import time
from MyMQTT import *

class Viewer(object):
	"""docstring for Viewer"""
	def __init__(self, settings):
		self.catalogURL=settings['catalogURL']
		self.devices=self.getDevices()
		self.removeThreshold=settings['removeThreshold']
		self.removeInterval=settings['removeInterval']
		self.serviceInfo=settings['serviceInfo']
		self.actualTime = time.time()
		# MQTT config
		self.clientID=settings['mqttData']['mqttclientID']
		self.broker=settings['mqttData']['brokerIP']
		self.port=settings['mqttData']['brokerPort']
		self.topic_publish=settings['mqttData']['mqttTopicAlert']
		self.devicemonitormqttclient = MyMQTT(self.clientID, self.broker, self.port, self)
	
	def startSim(self):
		self.devicemonitormqttclient.start()    
    
	def stopSim(self):
		self.devicemonitormqttclient.unsubscribe()
		self.devicemonitormqttclient.stop()
	
	def getDevices(self):
		response=requests.get(f'{self.catalogURL}/devices').json()
		print('List of available devices obtained')
		return  response['devices']
	
	def registerService(self):
		self.serviceInfo['last_update']=self.actualTime
		requests.post(f'{self.catalogURL}/services',data=json.dumps(self.serviceInfo))
	def updateService(self):
		self.serviceInfo['last_update']=self.actualTime
		requests.put(f'{self.catalogURL}/services',data=json.dumps(self.serviceInfo))

	def run(self):
		print('Starting Device Monitor')
		self.startSim()
		time.sleep(20)
		self.registerService()
		while True:
			time.sleep(self.removeInterval)
			self.removeInactive()
			self.updateService()
	
	def removeInactive(self):
		self.actualTime = time.time()
		devices=self.getDevices()
		for device in devices:
			if self.actualTime-device['last_update'] > self.removeThreshold:
				message_to_send={'alert':f'Device {device["ID"]} has been removed','action':'Please check the device'}
				requests.delete(f'{self.catalogURL}/devices/{device["ID"]}')
				self.devicemonitormqttclient.myPublish(self.topic_publish,message_to_send)
				print(f'Device {device["ID"]} has been removed')

if __name__ == '__main__':
	settings=json.load(open('settings.json','r'))
	v=Viewer(settings)
	v.run()