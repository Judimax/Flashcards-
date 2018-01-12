from __future__ import print_function

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import time
import os
import sys


class Flashcards:

        
    def __init__(self):

        self.flashcards = dict()


    def add_pictures(self):

        for i in range(len(self.flashcards.keys())):
            if str(self.flashcards.values()[i]).find("tdddddd") != -1:
                print(self.flashcards.keys()[i],end = ',')
                print(self.flashcards.values()[i],end = ',')

    def put_in_picture(self,defs):
        print("////////////////////////////////////")
        print("/                                  /")
        print("/                                  /")
        print("/                                  /")
        print("/                                  /")
        print("/"          +str(defs)+  "         /")
        print("/                                  /")
        print("/                                  /")
        print("/                                  /")
        print("/                                  /")
        print("/                                  /")
        print("////////////////////////////////////")      
                
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
                    if len(self.flashcards[i][j]) == 0:

                        break
                    try:
                        answer_i = input("What is  " + i + " ? ")
                    except:
                        answer_i = 'skip'
                            
                    if answer_i == "q":
                        return
                    
                    elif answer_i == "skip":
                        randomizer += 1
                        if randomizer % 17 == 0:
                            print("hey gotta study man I can't keep giving answers like this")
                        print('alright')
                        print(i)
                        if self.flashcards[i][j].find('PNG') != -1:
                            
                            img = mpimg.imread('flashcardpictures/' +self.flashcards[i][j])
                            plt.imshow(img)
                            plt.show()
                        else:
                           self.put_in_picture(self.flashcards[i][j])
                        pass
                            
                          
                    elif randomizer == 0:
                        print("Alright lets check\n")
                        print("...")
                        time.sleep(5)
                        if self.flashcards[i][j].find('PNG') != -1:
                            img = mpimg.imread('flashcardpictures/' +flashcards[i][j])
                            plt.imshow(img)
                            plt.show()
                        elif answer_i == self.flashcards[i][j]:
                            print("Alright you got it in" + attempts + "tries!,")
                            break
                        else:
                            if attempts % 2 == 0:
                                print("No you didn't get it try again")
                            else:
                                print("Are you sure? try again")
                            attempts += 1
                            
    def reg_studY(self):
        pr = ""
        while pr != 'no':
                          
            query = input("Please type in term  ")
            a=0
            
            for i in self.flashcards.keys():

                if i == query:
                    print(self.flashcards[i],end  = "\n")
                    time.sleep(2)
                    a=1
                    break
            pr = str(input("Well would you like to search for another"))
                
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

        try:
            final = open(ginit,"w")
            for i,j in self.flashcards.items():
                i += "$"
                final.write(i)
                final.flush()
                for defs in j:
                    if defs != j[-1]:
                        final.write(str(defs) + ',')
                    else:
                        final.write(str(defs))
                    final.flush()
                final.write("\n")
                final.flush()
            final.close()
        except:
            print('error')
            print(self.flashcards)

    def load(self,ok):
        
        final = open(ok,"r")
        flash = final.read().splitlines()
        for i in flash:
            i  = i.split("$")
            print(i)
            # turn all def -> list for play method
            i[1] = i[1].split(',')
            #print(type(i[1]))
            print("\n",end = "\n")
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

            if then.find("image") != -1:
                Archaelogy.add_pictures()

            elif then.find("i") != -1:
                sys.exit()




main()


        
    
    
                  
    
    

        
        
    
    

        


        
