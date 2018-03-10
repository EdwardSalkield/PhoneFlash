import cherrypy
import json
import time

class flashserver(object):
    @cherrypy.expose
    def index(self):
        return json.dumps({"status":"ok","currenttime":time.time()})
    
    @cherrypy.expose
    def updatePhone(self,lat=None,long=None):
        if lat is None or long is None:
            return json.dumps({"status":"GPS is NULL","currenttime":time.time(),"lat":lat,"long":long})
        else:
            cherrypy.session['lat'] = lat
            cherrypy.session['long'] = long
            return json.dumps({"status":"ok","currenttime":time.time(),"lat":cherrypy.session['lat'],"long":long})

    @cherrypy.expose
    def getBuffer(self):
        #example entry needs to be procedural
       payload={"nextUpdateAt":time.time()+1,"buffer":[[time.time()+0.25,"on",time.time()+0.5,"off"],[time.time()+0.75,"on",time.time()+1,"off"]],"currenttime":time.time()}
       return json.dumps(payload)

    @cherrypy.expose
    def test(self):
        return cherrypy.session['lat']

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(flashserver(), '/', conf)


