import cherrypy
import json

def string_reverse(string):
    #there is a python function that does this: reversed(string)
    return string[::-1] # [a:b:step] going from a to b using a step equal to step

class StringReverse(object):
    exposed = True
    def __init__(self):
        pass
    def GET(self,*uri,**params):
        pass
        '''
        output=""
        if len(uri)>0:
            output= ""
            for pathi in uri:
                output+=string_reverse(pathi)+"<br>"
        else:
            output= "No string to reverse"
        return output
        '''
    def POST(self,*uri,**params):
        pass
    def PUT(self,*uri,**params):
        body_read=cherrypy.request.body.read()
        if len(body_read)>0:
            try:
                json_body=json.loads(body_read)
                output={}
                for key in json_body.keys():
                    output[key]=string_reverse(json_body[key])
                return json.dumps(output)
            except json.decoder.JSONDecodeError:
                raise cherrypy.HTTPError(400,"Bad Request. Body must be a valid JSON")
            except:
                raise cherrypy.HTTPError(500,"Internal Server Error")
        else:
            return "Empty body"
    def DELETE(self,*uri,**params):
        pass

if __name__=="__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }
    cherrypy.tree.mount(StringReverse(),'/',conf)
    cherrypy.config.update({'server.socket_port':8080})
    cherrypy.engine.start()
    cherrypy.engine.block()