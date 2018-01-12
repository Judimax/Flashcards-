import time
import random

fico= open('network.txt','r')
filler = fico.read()
fico.close
filler= filler.strip("{")
filler= filler.strip("}")
filler= filler.strip("[")
filler= filler.strip("]")
filler = filler.split(":")
print(type(filler))
leito = open('com.txt','w')
leito.write(filler[0])
leito.flush()
i =1
for i in range(len(filler)):
    if filler[i].find("[") != -1:
        
        chaka = filler[i].split("]")
        print(len(chaka))
        snd = "$" + chaka[0]
        leito.write(snd)
        leito.flush()
        if filler[i] != filler[-1]:
            leito.write("\n")
            leito.flush()
            leito.write(chaka[1])
            leito.flush()
print(type(filler))
leito.close()
