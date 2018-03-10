import cherrypy
import json
import time
import translate

class flashserver(object):
    @cherrypy.expose
    def index(self):
        return json.dumps({"status":"ok","currenttime":time.time()})
    
    @cherrypy.expose
    def updatePhone(self,la=None,lo=None):
        if la is None or lo is None:
            return json.dumps({"status":"GPS is NULL","currenttime":time.time()})
        else:
            cherrypy.session['la'] = la
            cherrypy.session['lo'] = lo
            return json.dumps({"status":"ok","currenttime":time.time()})

    @cherrypy.expose
    def getBuffer(self):
       
        #example entry needs to be procedural
       #payload={"nextUpdateAt":time.time()+1,"buffer":[[time.time()+0.25,"on",time.time()+0.5,"off"],[time.time()+0.75,"on",time.time()+1,"off"]],"currenttime":time.time()}
       try:
           cherrypy.session['la']
           cherrypy.session['lo']
       except:
           cherrypy.session['la']=None
           cherrypy.session['lo']=None
       try:
            buffer = translate.translate(self.starttime,cherrypy.session.id,cherrypy.session['la'],cherrypy.session['lo'])
       except:
           buffer=[[]]
       payload={"status":"ok","currenttime":time.time(),"buffer":buffer}
       return json.dumps(payload)

    @cherrypy.expose
    def start(self):
        self.starttime=time.time()
        return json.dumps({"status":"ok"})

    @cherrypy.expose
    def ping(self):
        return json.dumps({"currenttime":time.time()})

    @cherrypy.expose
    def test(self):
        return json.dumps(cherrypy.session['la'])
    

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(flashserver(), '/', conf)


