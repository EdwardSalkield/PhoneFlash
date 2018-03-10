translate(starttime,id,la,lo):
    #startime is translation betweenn time of commands and unix time
    with open("pattern.json","r") as pattern:
           sequence=json.loads(pattern.read())


    return buffer