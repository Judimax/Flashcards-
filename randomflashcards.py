import random
import time
import os
import sys
import Image

class Flashcards:

        
    def __init__(self):

        self.flashcards = dict()


    def play_a_game(self):
        
        print("\n")
        print("Lets play Flashcards and Your Mind!!!\n")
        answer_i = "skip"

        while answer_i != "q":
            
            print("If you want to quit at any time press q")
            keys = self.flashcards.keys()
            random.shuffle(keys)
            for i in keys:
                
                randomizer = 0
                attempts = 0

                "remember to do if else version to, show how you know how to shorten code bullet_points"
                for j in range(len(self.flashcards[i])):
                    time.sleep(.5)
                    '''if len(self.flashcards[i][j]) == 0:

                        break
                    answer_i = input("What is  " + i + " ? ")'''
                            
                    if answer_i == "q":
                        return
                    elif answer_i == "skip":
                        print('alright')
                        print(i)
                        print(len(self.flashcards[i][j]))
                        pass
                            
                          
                    elif randomizer == 0:
                        print("Alright lets check\n")
                        print("...")
                        time.sleep(5)
                        if answer_i == self.flashcards[i][j]:
                            print("Alright you got it in" + attempts + "tries!,")
                            break
                        else:
                            if attempts % 2 == 0:
                                print("No you didn't get it try again")
                            else:
                                print("Are you sure? try again")
                            attempts += 1
                            
    def studY(self):
        while True:
                          
            query = input("Please type in term  ")
            a=0
            
            for i in self.flashcards.keys():

                if i == query:
                    print(self.flashcards[i])
                    a=1
                    break
            if a==0:
                print("Could not find search term, would you like to try another?")

    def add(self,term = None):
        try:
            while True:
                answer = input("Do you want to add again?")
                if answer == "no":
                    print(str(self.flashcards))
                    return
                terms = str(input("Please input terms  "))
                definition = str(input("Please input definition   "))             
                if True: definition = definition.split(",")
                self.flashcards[terms] = definition
                
        except:
            print("Place quotes")
            self.add()

    def save(self,ginit):

        self.flashcards = self.flashcards
        final = open(ginit,"w")
        for i,j in self.flashcards.items():
            i += "$"
            final.write(i)
            final.flush()
            j = j.split(",")
            # turn all def -> list for play method
            for defs in j:
                if defs != j[-1]:
                    final.write(str(defs) + ',')
                else:
                    final.write(str(defs))
                final.flush()
            final.write("\n")
            final.flush()
        final.close()

    def load(self,ok):
        
        final = open(ok,"r")
        flash = final.read().splitlines()
        for i in flash:
            i  = i.split("$")
            print(i)
            # turn all def -> list for play method
            i[1] = i[1].split(',')
            print(type(i[1]))
            print("\n")
            self.flashcards[i[0]]= i[1]
        final.close()
        return 


def main():
        Archaelogy = Flashcards()
        Archaelogy.load('network.txt')
        gisher = ""

        
        while True:
                        
            then= input("What would you like to do next?")
            if then.find("play") != -1:
                Archaelogy.play_a_game()

            if then.find("study") != -1:
                Archaelogy.reg_studY()

            if then.find("add") != -1:
                Archaelogy.add()

            if then.find("save") != -1:
                gisher = input("save as")
                Archaelogy.save(gisher)
                                        
            if then.find("load") != -1:
                gisher = input("which file")
                Archaelogy.load(gisher)




main()


        
    
    
                  
    
    

        
        
    
    

        


        
