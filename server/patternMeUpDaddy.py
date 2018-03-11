import alternate
import onBeat
import fade

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
        # Toggles the left and right half of the audience on and off
        if p == "lrAlternate":
            commands += alternate.lrAlternate(midpoint, i,  beatTime, barTime)
        # Same as lrAlternate, except top and bottom
        elif p == "udAlternate":
            commands += alternate.udAlternate(midpoint, i,  beatTime, barTime)
        # All participating devices on for a quarter beat at the start of each beat
        elif p == "flashOB":
            commands += onBeat.flashOB(i, beatTime, barTime)
        # Toggles lights off and on on beat
        elif p == "toggleOB":
            commands += onBeat.toggleOB(i, beatTime, barTime)
        # Identical to toggleOB, except in double time
        elif p == "toggleOB2":
            commands += onBeat.toggleOB2(i,  beatTime, barTime)
        # Test/hype building/space filling instruction. All dark for a bar
        elif p == "dark":
            commands += fade.dark(i, beatTime, barTime)
        elif p == "light":
            commands += fade.light(i, beatTime, barTime)
    #print(commands)
    return commands
