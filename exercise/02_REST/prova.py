import string
import random
import cherrypy

def reverseString(str):
    return str[::-1]


class StringGeneratorWebService(object):
    expose=True

    # def GET(self, *uri, **param):
    #     if (len(uri)>0):
    #         newstr = ''
    #         for u in uri:
    #             newstr += reverseString(u)+'<br>'
    #         return newstr
    #     else:
    #         raise cherrypy.HTTPError(500)
    
    def PUT(self, *uri, **param):
        if (len(uri)>0):
            newstr = ''
            for u in uri:
                newstr += reverseString(u)+'<br>'
            return newstr
        else:
            raise cherrypy.HTTPError(500)  

if __name__=='__main__':
    conf = {
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }

    cherrypy.tree.mount(StringGeneratorWebService)

    cherrypy.config.update({'server.socket_host':'0.0.0.0'})
    cherrypy.config.update({'server.socket_port':'8080'})

    cherrypy.engine.start()
    cherrypy.engine.block()