# Typing speed calculator will determine speed of typing as WPMs
# Time module will be used to calculate speed
# Random module will be used to display different kinds of strings

import random as r
from time import *

# function to calculate the errors
def mistake(demoTypingString,userString):   # two parameters; 1st = demo para for typing, 2nd = user input against string
    error = 0
    for i in range(len(demoTypingString)):  # loop through the string
        try:
            if demoTypingString[i] != userString[i]:    # if strings not matched then increment the error
                error = error + 1
        except :
            error  = error + 1
    return error

# function to calculate the speed of the typing
def speed_time(startingTime, endingTime, userInput):
    timeDelay = endingTime - startingTime       # time difference
    timeRound = round(timeDelay,2)  # round off the time
    speed = len(userInput) / timeRound
    return round(speed)



typingstring = ["I am string number one","I am string number two","I am string number three"] # paragraphs for typing
displaystring = r.choice(typingstring)
print(displaystring)
print("***** Typing Speed *****")
print()
print()

time_one = time()   # starting time before the user input
userinput = input("Enter :")    # user will start against the string
time_two = time()   # ending time before the user input

print("Speed : ",speed_time(time_one,time_two,userinput)," w/sec")
print("Error :",mistake(displaystring,userinput))