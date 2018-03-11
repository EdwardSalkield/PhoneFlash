
def flashOB(bar, beatTime, barTime):
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
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+(beatTime/4),
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
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+beatTime+(beatTime/4),
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
    #LHS on off commands
    commands.append({   "time":time+2*beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[-180, 180]
                            },
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+2*beatTime+(beatTime/4),
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
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+3*beatTime+(beatTime/4),
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

    return commands





def toggleOB(bar, beatTime, barTime):
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
                            "command":'on',
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
                            "command":'on',
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


def toggleOB2(bar, beatTime, barTime):
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
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+(beatTime/2),
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
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+beatTime+(beatTime/2),
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
    #LHS on off commands
    commands.append({   "time":time+2*beatTime,
                        "commands":{
                            "parameters":{
                                "iD":None,
                                "la":[-90,90],
                                "lo":[-180, 180]
                            },
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+2*beatTime+(beatTime/2),
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
                            "command":'on',
                            "probability":1
                        }
                    })
    commands.append({   "time":time+3*beatTime+(beatTime/2),
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

    return commands
