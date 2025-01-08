import cherrypy
import json

class sensors:
    exposed=True
    def __init__(self):
        pass

    def GET ():




if __name__=="__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'toolssessions.on':True
        }
    }
    cherrypy.tree.mount(webService(),'/',conf)
    cherrypy.config.update({'server.socket_port':8080})
    cherrypy.engine.start()
    cherrypy.engine.block()