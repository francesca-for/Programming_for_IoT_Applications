import requests
import json
import time
class Viewer(object):
	"""docstring for Viewer"""
	def __init__(self, settings):
		self.catalogURL=settings['catalogURL']
		self.devices=self.getDevices()
		self.removeThreshold=settings['removeThreshold']
		self.removeInterval=settings['removeInterval']
		self.serviceInfo=settings['serviceInfo']
		self.actualTime = time.time()
	
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
				requests.delete(f'{self.catalogURL}/devices/{device["ID"]}')
				print(f'Device {device["ID"]} has been removed')

if __name__ == '__main__':
	settings=json.load(open('settings.json','r'))
	v=Viewer(settings)
	v.run()