from MyMQTT import *
import time

class LightManager:
	def __init__(self, clientID,broker,port,topic_publish):
		self.topic_publish=topic_publish
		self.__message={'client': clientID,'n':'switch','status':None, 'timestamp':'','unit':"bool"}
		self.client=MyMQTT(clientID,broker,port,None)
		self.statusToBool={"on":1,"off":0}

	def startSim (self):
		self.client.start()

	def stopSim (self):
		self.client.unsubscribe()
		self.client.stop()

	def publish(self,value):
		message=self.__message
		message['timestamp']=time.time()
		message['status']=self.statusToBool[value]
		self.client.myPublish(self.topic_publish,message)
		print("Command Sent!")
		#print(f"published Message: {message} \n \n")



if __name__ == "__main__":
	broker="mqtt.eclipseprojects.io"
	port=1883
	#topic publish
	topic_publish_lM = "IoT/rafafontana1234/led/set"
	light_manager = LightManager("rafafontana12",broker,port,topic_publish_lM)
	light_manager.startSim()
	time.sleep(2)
	print('\nWelcome to the client to switch on/off the lamp\n')
	done=False
	command_list='------------------------\n \nType:\n"on" to set the light on\n"off" to set it off\n"q" to quit\n'
	while not done:
		print(command_list)
		user_input=input()
		if user_input=="on" or user_input=="off":
			light_manager.publish(user_input)
		elif user_input=='q':
			done=True
		else:
			print('Unknown command')
	light_manager.stopSim()   