import cherrypy
import json
import time
import translate
import copy
from patternMeUpDaddy import barToCommands


class flashserver(object):
    # Initialise Server
    commands = []
    starttime = 0
    controllerping = 0
    locations=[[],[]]
    
    @cherrypy.expose
    def index(self):
        return json.dumps({"status":"ok","currenttime":time.time()})
    
    @cherrypy.expose
    def updatePhone(self, la=1, lo=1):
        print("La and Lo")
        print(la)
        print(lo)
        if la is None or lo is None:
            print("NULL GPS")
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
            print("Locations")
            print(self.locations)
            return json.dumps({"status":"ok","currenttime":time.time(),"locations":self.locations})

    @cherrypy.expose
    def getBuffer(self):
       
        #example entry needs to be procedural
       #payload={"nextUpdateAt":time.time()+1,"buffer":[[time.time()+0.25,"on",time.time()+0.5,"off"],[time.time()+0.75,"on",time.time()+1,"off"]],"currenttime":time.time()}
       
       #gets agregated gps data

        #checking the song has started
       try:
            self.starttime
       except:
           buffer = [[]]
           status = "song not started"

       #checking valid gps
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
       print("Commands:")
       print(self.commands)
       buffer = translate.translate(self.commands ,self.starttime,cherrypy.session.id,cherrypy.session['la'],cherrypy.session['lo'])
       print("CommandsAfter:")
       print(self.commands)
       status = "ok"
       #except:
       #    buffer = [[]]
       #    status = "translation error"

          

       payload={"status":status,"currenttime":time.time(),"buffer":buffer,"nextUpdateAt":time.time()+180}
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
    def beat(self, beat, ping):
        #self.controllerping = ping
        
        #self.starttime = self.starttime -float(ping)/2
        return json.dumps({"currenttime":time.time()})

    @cherrypy.expose
    def start(self):
        with open("bars.json") as bars:
            sequence = json.loads(bars.read())
        bars=sequence["bars"]
        bpm = sequence["bpm"]
        self.commands=copy.deepcopy(barToCommands(bars,self.locations,bpm))
        self.starttime=time.time()
        print(self.commands)

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
