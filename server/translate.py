import random
import time
import os
import json

def translate(starttime,iD,la,lo):
    #startime is translation between time of commands and unix time
    with open("pattern.json") as pattern:
           sequence = json.loads(pattern.read())
    buffer = []

    for things in sequence:
        params = things["commands"]["parameters"]
        print(correctLocation(params, la, lo))
        print(ontime(things, starttime))
        print(correctID(params, iD))
        if correctLocation(params, la, lo) and ontime(things, starttime) and correctID(params, iD):
            buffer.append( ( things["time"]+starttime, things["commands"]["command"]) )


    return buffer

def correctLocation(params, la, lo):
    return (params["la"][0] <= la) and (params["la"][1] > la) and (params["lo"][0] <= lo) and (params["lo"][1] > lo)

def ontime(things, starttime):
    return (things["time"] + starttime >= time.time())

def correctID(params, iD):
    return (params["iD"] == iD) or params["iD"]==None