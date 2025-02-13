# EXAMPLE 1

# import cherrypy

# class HelloWorld(object):
#     @cherrypy.expose
#     def index(self):
#         return "Hello world!"
    

# if __name__=='__main__':
#     cherrypy.tree.mount(HelloWorld())
#     cherrypy.engine.start()
#     cherrypy.engine.block()
    



# EXAMPLE 2

# import random
# import string
# import cherrypy

# class StringGenerator(object):
#     @cherrypy.expose
#     def index(self):
#         return "Hello world!"
    
#     @cherrypy.expose
#     def generate(self, length=8):
#         return ''.join(random.sample(string.hexdigits, int(length)))
    

# if __name__=='__main__':
#     cherrypy.tree.mount(StringGenerator())
#     cherrypy.engine.start()
#     cherrypy.engine.block()




# EXAMPLE 3

# import random
# import string
# import cherrypy
# import cherrypy.test

# class StringGenerator(object):
#     @cherrypy.expose
#     def index(self):
#         return "Hello world!"
    
#     @cherrypy.expose
#     def generate(self, length=8):
#         some_string = ''.join(random.sample(string.hexdigits, int(length)))
#         cherrypy.session['mystring'] = some_string
#         return some_string
    
#     @cherrypy.expose
#     def display(self):
#         return cherrypy.session['mystring']
    

# if __name__=='__main__':
#     conf = {
#         '/':{'tools.sessions.on':True
#              }
#     }
#     cherrypy.tree.mount(StringGenerator(), '/', conf)
#     cherrypy.engine.start()
#     cherrypy.engine.block()




#  EXAMPLE 4

# import os, os.path
# import random
# import string
# import cherrypy

# class StringGenerator(object):
#     @cherrypy.expose
#     def index(self):
#         return """<html><head><link href="/static/scc/style.css"rel="stylesheet"></head><body><p>Hello world!!</p></body></html>"""


# if __name__=='__main__':
#     conf={
#         '/':{
#             'tools.sessions.on':True,
#             'tools.staticdir.root':os.path.abspath(os.getcwd())
#         },
#         '/static':{
#             'tools.staticdir.on':True,
#             'tools.staticdir.dir':'./public'
#         }
#     }
#     cherrypy.tree.mount(StringGenerator(), '/', conf)
#     cherrypy.engine.start()
#     cherrypy.engine.block()
   



# --------- REST ----------


#  EXAMPLE 5

# import random
# import string
# import cherrypy

# class StringGeneratorWebService(object):
#     exposed = True

#     def GET(self, *path, **query): 
#         return cherrypy.session['mystring']

#     def POST(self, *path, **query):
#         some_string = ''.join(random.sample(string.hexdigits, int(query['lenght'])))
#         cherrypy.session['mystring'] = some_string
#         return some_string

#     def PUT(self, *path, **query):
#         cherrypy.session['mystring'] = params['another_string']

#     def DELETE(self, *path, **query):
#         cherrypy.session.pop('mystring', None)


# if __name__ == '__main__':
#     conf = {
#         '/':{
#             'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
#             'tools.sessions.on':True
#         }
#     }
#     cherrypy.tree.mount(StringGeneratorWebService(), '/', conf)

#     cherrypy.config.update({'server.socket_host':'0.0.0.0'})
#     cherrypy.config.update({'server.socket_port':8080})

#     cherrypy.engine.start()
#     cherrypy.engine.block()
    



#  EXAMPLE 6

# import random
# import string
# import cherrypy

# class StringGeneratorWebService(object):
#     exposed = True

    
#     def GET(self, *path):  # conta elementi nel path
#         return ("uri:%s; uri length %s" %(str(path), len(path)))

#     def GET(self, **query):  # conta parametri nella query
#         # params can be managed as a dictionary
#         return ("Params: %s; params length: %s" % (str(query), len(query)))

#     def GET(self, *path, **query):
#         return ("URI: %s; Parameters %s" % (str(path), str(query)))


# if __name__ == '__main__':
#     conf = {
#         '/':{
#             'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
#             'tools.sessions.on':True
#         }
#     }
#     cherrypy.tree.mount(StringGeneratorWebService(), '/', conf)

#     cherrypy.config.update({'server.socket_host':'0.0.0.0'})
#     cherrypy.config.update({'server.socket_port':8080})

#     cherrypy.engine.start()
#     cherrypy.engine.block()



#  EXAMPLE 7

import random
import string
import cherrypy

class StringGeneratorWebService(object):
    exposed = True
    def GET(self, *path, **query):
        if(len(path)>0 and path[0]=="ciao"):
            return ("URI: %s; Parameters: %s" % (str(path), str(query)))
        else: 
            raise cherrypy.HTTPError(404, "Erroreeeeeeeee")

    # def POST(self, *path, **query):

    # def PUt(self, *path, **query):

    # def DELETE(self, *path, **query):


if __name__=='__main__':
    conf = {
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }
    cherrypy.tree.mount(StringGeneratorWebService(), '/string', conf)
    cherrypy.tree.mount(StringGeneratorWebService(), '/hola', conf)

    cherrypy.config.update({'server.socket_host':'0.0.0.0'})
    cherrypy.config.update({'server.socket_port':8080})

    cherrypy.engine.start()
    cherrypy.engine.block()