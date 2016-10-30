import random
import time
class Flashcards:

        
    def __init__(self):

        self.flashcards = dict()

    def play_a_game(self):
        
        print("\n")
        print("Lets play Flashcards and Your Mind!!!\n")
        answer_i = "default"

        while answer_i != "q":
            print("If you want to quit at any time press q")
            
            for i in self.flashcards.keys():
                print("What is" + i + "?")
                answer_i = input("     ")

                if answer_i == "q":
                    break
                randomizer = 0
                attempts = 0

                while True:

                    if attempts != 0:
                        answer_i = input("What is  " + i + " ? ")
                        
                        if answer_i == "q":
                            break
                        
                    if randomizer == 0:
                        print("Alright lets check\n")
                        print("...")
                        time.sleep(5)
                        if answer_i == self.flashcards[i]:
                            print("Alright you got it!")
                            break
                        else:
                            print("No you didn't get it try again")
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
                            
Archaelogy = Flashcards()

for i in range(7):
    terms = input("Please input terms  ")
    definition = input("Please input definition   ")
    Archaelogy.flashcards[terms] =definition
    answer= input("Are you done with the flashcard  ")
    if answer == "yes":break

then= input("What would you like to do next?")
if then.find("play") != -1:
    Archaelogy.play_a_game()

if then.find("study") != -1:
    Archaelogy.reg_studY()



        
    
    
                  
    
    

        
        
    
    

        


        
