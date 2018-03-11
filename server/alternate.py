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
    commands.append({   "time":time+3*beatTime,
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
    commands.append({   "time":time+3*beatTime,
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
    commands.append({   "time":time+3*beatTime,
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
    commands.append({   "time":time+3*beatTime,
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
