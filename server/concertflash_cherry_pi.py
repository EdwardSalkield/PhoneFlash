import cherrypy
import json
import time




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
            #adds locations to list of locations
            try:
                self.locations[0].append(float(la))
                self.locations[1].append(float(lo))
            except:
               self.locations=[[],[]]
               self.locations[0].append(float(la))
               self.locations[1].append(float(lo))
            return json.dumps({"status":"ok","currenttime":time.time(),"locations":self.locations})

    @cherrypy.expose
    def getBuffer(self):
       
        #example entry needs to be procedural
       #payload={"nextUpdateAt":time.time()+1,"buffer":[[time.time()+0.25,"on",time.time()+0.5,"off"],[time.time()+0.75,"on",time.time()+1,"off"]],"currenttime":time.time()}
       
       #gets agregated gps data

        #checking the song has started
       try:
            if (time.time()-self.starttime)%0.0472440944881<0.01:
                state = True
            else:
                state =False
            
       except:
                state = False
                status = "song not started"

       """#checking valid gps
       try:
           cherrypy.session['la']
           cherrypy.session['lo']
       except:
           cherrypy.session['la']=None
           cherrypy.session['lo']=None
           buffer = [[]]
           status = "GPS ERROR"
       #checking messy code soject 
       #try:
       buffer = translate.translate(self.commands ,self.starttime,cherrypy.session.id,cherrypy.session['la'],cherrypy.session['lo'])
       status = "ok"
       #except:
       #    buffer = [[]]
       #    status = "translation error"
       """
       status="ok"
       #payload={"status":status,"currenttime":time.time(),"buffer":buffer,"nextUpdateAt":time.time()+180}
       payload = {"buffer":state}
       return json.dumps(payload)


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

    @cherrypy.expose
    def beat(self, beat, ping=-1):
        if float(ping) >0:  
            self.starttime = self.starttime -float(ping)/2
        return json.dumps({"currenttime":time.time()})

    @cherrypy.expose
    def start(self):
       """ with open("bars.json") as bars:
            sequence = json.loads(bars.read())
        bars=sequence["bars"]
        bpm = sequence["bpm"]
        self.commands=barToCommands(bars,self.locations,bpm)"""
       self.starttime=time.time()

       return json.dumps({"currenttime":time.time()})

    

if __name__ == '__main__':
    cherrypy.config.update({
              'server.socket_host': '0.0.0.0',
              'server.socket_port': 8080,
              'server.ssl_certificate':'/etc/nginx/ssl/nginx.crt',
              'server.ssl_private_key':'/etc/nginx/ssl/nginx.key',
              'tools.sessions.on': True,
              'tools.sessions.timeout': 10
    })
    cherrypy.quickstart(flashserver())