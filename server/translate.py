import random
import time
import os
import json

def translate(sequence,starttime,iD,la,lo):
    buffer = []
    if la == None or lo == None:
        return buffer

    for command in sequence:
        # Command extraction
        c_time = command["time"]
        c_id = command["commands"]["parameters"]["iD"]
        c_la = command["commands"]["parameters"]["la"]
        c_lo  = command["commands"]["parameters"]["lo"]
        c_state = command["commands"]["command"]
        c_prob = command["commands"]["probability"]
        
        # Check coordinates
        if not (la > c_la[0] and la < c_la[1]):
            continue
        if not (lo > c_lo[0] and lo < c_lo[1]):
            continue

        # Check probability
        #if random.random() > c_prob:
        #    continue

        buffer.append([c_time + starttime, c_state])

    return buffer

