import time
import translate
from patternMeUpDaddy import barToCommands

comamnds=barToCommands(["lrAlternate","udAlternate"],[[1,-1,1],[1,-1,-1]],120)
starttime=time.time()

buffer = translate.translate(comamnds,starttime,1,1,2)
print(buffer)