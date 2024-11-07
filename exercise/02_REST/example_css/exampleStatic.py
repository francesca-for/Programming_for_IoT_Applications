import cherrypy
import os

class ExampleStatic(object):
	exposed=True
	def __init__(self):
		self.id=1
	def GET(self):
		return open("index.html")


if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tools.staticdir.root': os.path.abspath(os.getcwd()),
				'tools.sessions.on':True,
			},
		 '/css':{
		 'tools.staticdir.on': True,
		 'tools.staticdir.dir':'./css'
		 },
		 '/js':{
		 'tools.staticdir.on': True,
		 'tools.staticdir.dir':'./js'
		 },
	}		
	cherrypy.tree.mount(ExampleStatic(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
