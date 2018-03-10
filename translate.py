import random

def translate(starttime,iD,la,lo):
    #startime is translation between time of commands and unix time

    with open("pattern.json","r") as pattern:

           sequence = json.loads(pattern.read())

    buffer = []

    for things in sequence:
        params = things.commands.parameters
        if (random.random() < things.commands.probability):
            if correctLocation(params, la, lo) and afterStartTime(things, starttime) and correctID(params, iD):
                buffer.append( ( things.time+starttime, things.commands.command ) )


    return buffer

def correctLocation(params, la, lo):
    return (params.la[0] <= la) and (params.la[1] > la) and (params.lo[0] <= lo) and (params.lo[1] > lo)

def afterStartTime(things, starttime):
    return (things.time > starttime)

def correctID(params, iD):
    return (params.iD == iD)
