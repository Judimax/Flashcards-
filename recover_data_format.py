import time
import random

print('do not complete delete copy file might not transfer correctly!!!!!')
print("For admin Alphatron flashcards program, if a developer see if yours can coop")
print('basically a translator\n')
'''for i in range(27):
    print('\n')
time.sleep(5)
for i in range(27):
    print('do not completely delete copy file might not transfer correctly!!!!!')
    time.sleep(.5)
time.sleep(5)'''

ficos= str(input("give me the file"))
fico = open(ficos,'r')
filler = fico.read()
fico.close()
filler= filler.strip("{")
filler= filler.strip("}")
filler= filler.strip("[")
filler= filler.strip("]")
filler= filler.strip('"')
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
