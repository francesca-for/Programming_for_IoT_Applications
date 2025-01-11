import cherrypy
import json
class Votes:         
    exposed=True         
    def GET(self,*uri,**params):
        dict=json.load(open("driverOfDay.json")) #Read JSON file
        all_pilots=dict["drivers"]
        total_votes=0
        votes_best_pilot=0
        for pilot in all_pilots:
            #total_votes=total_votes+pilot["votes"]
            total_votes+=pilot["votes"]
            if pilot["votes"]>votes_best_pilot:
                best_pilot=pilot["name"]                                     
                votes_best_pilot=pilot["votes"]                         
        perc=votes_best_pilot/total_votes*100                 
        msg={"most voted driver": best_pilot,                             
             "percentage of votes": perc
            }                 
        return json.dumps(msg)                 
    
    def PUT(self,*uri,**params):                 
        dict=json.load(open("driverOfDay.json"))        
        body=json.loads(cherrypy.request.body.read())
        pilots=dict["drivers"]                 
        voted_driver=body["vote"][0]
        found=False              
        '''
        for  pilot_position in range(len(pilots)):
            if pilots[pilot_position]["name"]==voted_driver:
                pilots[pilot_position]["votes"]=pilots[pilot_position]["votes"]+1
                dict["drivers"]=pilots
                found=True
        '''
        for pilot_position , pilot in enumerate(pilots):                         
            if pilot["name"]==voted_driver:                             
                pilot["votes"]=pilot["votes"]+1                                                                
                dict["drivers"][pilot_position]=pilot                               
                found=True                
        
        if found==False:                         
            raise cherrypy.HTTPError(404,"Wrong name of driver")
        json.dump(dict,open("driverOfDay.json","w"))                 
        return json.dumps(dict)
    
if __name__=="__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }
    cherrypy.tree.mount(Votes(),'/',conf)
    cherrypy.config.update({'server.socket_port':8080})
    cherrypy.engine.start()
    cherrypy.engine.block()