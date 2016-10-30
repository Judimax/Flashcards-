from random import *
class Flashcards:

        
    def __init__(self):

        self.flashcards = dict()

    def play_a_game(self):

        print("Lets play Flashcards and Your Mind!!!")      
        for i in self.flashcards.keys():
            print("What is" + i + "?")


        


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



        
    
    
while True:
                  
    query = input("Please type in term  ")
    a=0
    
    for i in Archaelogy.flashcards.keys():

        if i == query:
            print(Archaelogy.flashcards[i])
            a=1
            break
    if a==0:
        print("Could not find search term, would you like to try another?")

                  
    
    

        
        
    
    

        


        
