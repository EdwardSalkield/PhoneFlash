#def fadeIn():
#def fadeOut():

def dark(bar, beatTime, barTime):
    commands = []

    time = barTime*bar
    #RHS on off commands
    commands.append({   "time":time,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
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
                                "la":[-90,90],
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
                                "la":[-90,90],
                                "lo":[-180, 180]
                            },
                            "command":'off',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+3*beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[-180,180]
                            },
                            "command":'off',
                            "probability":1
                        }
                    })

    return commands
