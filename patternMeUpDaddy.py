
list locations
int bpm

# Translates a list of patterns into a list of commands
def translate(patterns):
    for i, p in enumerate(patterns):
        if p == "lrAlternate":
            lrAlternate(p, i)
        elif ...


def lrAlternate(location, bar):
    

    # Finding the middle of the room to establish the boundary everyone is divided by
    sumOfLongitudes = 0
    for elem in locations:
        sumOfLongitudes = elem[1] + sumOfLongitudes
    midpoint = sumOfLongitudes/len(locations)
    
    
    barTime = 240/bpm # Length of a bar
    beatTime = barTime/4 # Length of a beat
    time = barTime*bar
    commands = []

    if location[1] > midpoint:
        commands = [{   "time":time,
                        "commands":{
                            "parameters":{
                                "id":null,
                                "la":[-90,90],
                                "lo":[midpoint, 180]), 
                                'on', 1), 
                                (time+beatTime, (null,[-90,90],[midpoint, 180]), 'off', 1), (time+2*beatTime, (null,[-90,90],[midpoint, 180]), 'on', 1), (time+3*beatTime, (null,[-90,90],[midpoint, 180]), 'off', 1),]
    else:
        commands = [(time, (null,[-90,90],[-180, midpoint]), 'off', 1), (time+beatTime, (null,[-90,90],[-180, midpoint]), 'on', 1), (time+2*beatTime, (null,[-90,90],[-180, midpoint]), 'off', 1), (time+3*beatTime, (null,[-90,90],[-180, midpoint]), 'on', 1),]

    return commands


def udAlternate(location):
    
    # Finding the middle of the room to establish the boundary everyone is divided by
    sumOfLatitudes = 0
    for elem in locations:
        sumOfLatitudes = elem[0] + sumOfLatitudes
    midpoint = sumOfLatitudes/len(locations)
    
    barTime = 240/bpm # Length of a bar
    beatTime = barTime/4 # Length of a beat
    commands = []

    if location[0] > midpoint:
        commands = [(time, (null,la,lo), on, 1), (time+beatTime, (null,la,lo), off, 1), (time+2*beatTime, (null,la,lo), on, 1), (time+3*beatTime, (null,la,lo), off, 1),]
    else:
        commands = [(time, (null,la,lo), off, 1), (time+beatTime, (null,la,lo), on, 1), (time+2*beatTime, (null,la,lo), off, 1), (time+3*beatTime, (null,la,lo), on, 1),]

    return commands

def flashOB():

def toggleOB():

def fadeIn():

def fadeOut():

def starsInEdsEyes():
