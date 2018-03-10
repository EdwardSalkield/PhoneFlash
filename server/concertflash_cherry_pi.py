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
            cherrypy.session['la'] = float(la)
            cherrypy.session['lo'] = float(lo)
            return json.dumps({"status":"ok","currenttime":time.time()})

    @cherrypy.expose
    def getBuffer(self):
       
        #example entry needs to be procedural
       #payload={"nextUpdateAt":time.time()+1,"buffer":[[time.time()+0.25,"on",time.time()+0.5,"off"],[time.time()+0.75,"on",time.time()+1,"off"]],"currenttime":time.time()}
       try:
           cherrypy.session['la']
           cherrypy.session['lo']
           try:
                self.starttime
                try:
                    buffer = translate.translate(self.starttime,cherrypy.session.id,cherrypy.session['la'],cherrypy.session['lo'])
                    status = "ok"
                except:
                    buffer = [[]]
                    status = "GPS ERROR"
           except:
                buffer = [[]]
                status = "song not started"

       except:
           cherrypy.session['la']=None
           cherrypy.session['lo']=None
           buffer = [[]]
           status = "GPS ERROR"
          

       payload={"status":status,"currenttime":time.time(),"buffer":buffer,"nextUpdateAt":time.time()+1}
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

    @cherrypy.expose
    def stop(self):
        del self.starttime
        return json.dumps({"status":"ok"})
    

if __name__ == '__main__':
   cherrypy.config.update({'server.socket_host': '0.0.0.0',
                           'server.socket_port': 8080,
                           'server.ssl_certificate':'/etc/nginx/ssl/nginx.crt',
                           'server.ssl_private_key':'/etc/nginx/ssl/nginx.key',
                           'tools.sessions.on' : True,
                           'tools.sessions.timeout': 10
                           })



   cherrypy.quickstart(flashserver())


