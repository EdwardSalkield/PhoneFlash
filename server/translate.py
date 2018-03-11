import random
import time
import os
import json
from patternMeUpDaddy import barToCommands

def translate(sequence,starttime,iD,la,lo):
    """#startime is translation between time of commands and unix time
    with open("pattern.json") as pattern:
           sequence = json.loads(pattern.read())"""
    # Making the buffer stream we're gonna return
    buffer = []
    # Steaming on through the sequence of Commands we have
    for things in sequence:
        params = things["commands"]["parameters"]
        # Checking the aspects of the command against the identity its applied to, whether its on time and whether its in the right place...
        if correctLocation(params, la, lo) and ontime(things, starttime) and correctID(params, iD) and random.random()<things["commands"]["probability"]:
            # ... before appending it to the buffer
            buffer.append( ( things["time"]+starttime, things["commands"]["command"]) )
    return buffer

# Helpful helpery things
def correctLocation(params, la, lo):
    return (params["la"][0] <= la) and (params["la"][1] > la) and (params["lo"][0] <= lo) and (params["lo"][1] > lo)

def ontime(things, starttime):
    return (things["time"] + starttime >= time.time())

def correctID(params, iD):
    return (params["iD"] == iD) or params["iD"]==None

# Test output
print( translate (  barToCommands(["lrAlternate","udAlternate"],[[1,-1,1],[1,-1,-1]],120),time.time(),1,3.2,1.2) )