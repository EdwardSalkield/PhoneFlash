
def barToCommands(patterns,locations,bpm):
    # Finding the middle of the room to establish the boundary everyone is divided by
    """sumOfLongitudes = 0
    for elem in locations:
        sumOfLongitudes = elem[1] + sumOfLongitudes
    midpoint = sumOfLongitudes/len(locations)"""
    midpoint=[0,0]
    midpoint[0]=sum(locations[0])/float(len(locations[0]))
    midpoint[1]=sum(locations[1])/float(len(locations[1]))
    

    barTime = 240/bpm # Length of a bar
    beatTime = barTime/4 # Length of a beat

   # Making the list of commands
    commands=[]
    for i, p in enumerate(patterns):
        if p == "lrAlternate":
            commands = lrAlternate(midpoint, i, commands, beatTime,barTime)
        elif p == "udAlternate":
            commands = udAlternate(midpoint, i, commands, beatTime,barTime)
    #print(commands)
    return commands


def lrAlternate(midpoint, bar,commands , beatTime,barTime):
    
    time = barTime*bar
    #RHS on off commands
    commands.append({   "time":time,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[midpoint[1], 180] 
                            },
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[midpoint[1], 180]
                            },
                            "command":'off',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+2*beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[midpoint[1], 180] 
                            },
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+3*barTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[midpoint[1], 180]
                            },
                            "command":'off',
                            "probability":1
                        }
                    })
    #LHS on off commands
    commands.append({   "time":time,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[-180, midpoint[1]]
                            },
                            "command":'off',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[-180, midpoint[1]]
                            },
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+2*beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[-180,midpoint[1]]
                            },
                            "command":'off',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+3*barTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[-180, midpoint[1]]
                            },
                            "command":'on',
                            "probability":1
                        }
                    })
    
    return commands


def udAlternate(midpoint, bar,commands , beatTime,barTime):
    time = barTime*bar

    #back on off commands
    commands.append({   "time":time,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,midpoint[0]],
                                "lo":[-180, 180]
                            },
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,midpoint[0]],
                                "lo":[-180, 180]
                            },
                            "command":'off',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+2*beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,midpoint[0]],
                                "lo":[-180, 180]
                            },
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+3*barTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,midpoint[0]],
                                "lo":[-180, 180]
                            },
                            "command":'off',
                            "probability":1
                        }
                    })
    #front on off commands
    commands.append({   "time":time,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[midpoint[0],90],
                                "lo":[-180, 180]
                            },
                            "command":'off',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[midpoint[0],90],
                                "lo":[-180, 180]
                            },
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+2*beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[midpoint[0],90],
                                "lo":[-180, 180]
                            },
                            "command":'off',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+3*barTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[midpoint[0],90],
                                "lo":[-180, 180]
                            },
                            "command":'on',
                            "probability":1
                        }
                    })
    
    return commands

"""def flashOB():

def toggleOB():

def fadeIn():

def fadeOut():

def starsInEdsEyes():"""

barToCommands(["lrAlternate","udAlternate"],[[1,-1,1],[1,-1,-1]],120)
# Translates a list of patterns into a list of commands