# My improved version of the Codecademy 8 Ball

import random
import re
import sys

control = 1
theBall = {
            1:"Yes - definitely",
            2:"It is decidedly so",
            3:"Without a doubt",
            4:"Reply hazy, try again",
            5:"Ask again later",
            6:"Better not tell you now",
            7:"My sources say no",
            8:"Outlook not so good",
            9:"Very doubtful"
}

def getUserName():
  while True:
    user_name = input("Please enter your name: ")
    if not re.match("^[A-Za-z ]*$", user_name):
        print ("Error! Make sure you only use letters in your name")
    else:
        return user_name
        break

def getQuestion():
    while True:
        theQ = input("Please enter your question: ")
        if not re.match("^[A-Za-z \?]*$", theQ):
            print ("Error! Make sure your question only contains letters")
        else:
            return theQ
            break

def doquit():
    while True:
        QT = input("Would you like to answer another question (y/n)? ")
        if QT == "y" or QT == "Y":
            print("Great!")
            return 1
            break
        elif QT == "n" or QT == "N":
            print("Well that's sad")
            return 0
            break
        else:
            print("Error! You did not enter y or n")

print("Welcome to the Magic 8 Ball!")
print("Ask the Magic 8 Ball a yes/no question")
print("But first.... ")

pName = getUserName()


# The loop
while (control > 0):
    random_number = random.randint(1, 9)
    resp = theBall[random_number]
    playerQ = getQuestion()
    print(pName + " asks: " + playerQ)
    print("Magic 8-Ball's Answer: " + resp)
    print("\n")
    control = doquit()
    

print("Thank you for playing " + pName )
sys.exit()

