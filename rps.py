from tkinter import *    
from tkinter.ttk import *
import random

root = Tk()
root.title("RPS!")    
root.geometry('228x200') 
root.resizable(0,0) 

choice = ""
outcome = StringVar()
compChoice = ""

def setRock():
    choice = "rock"
    compChoiceRand = random.randint(1,3)

    if (compChoiceRand == 1):
        compChoice = "rock"
    elif (compChoiceRand == 2):
        compChoice = "paper"
    elif (compChoiceRand == 3):
        compChoice = "scissors"
    
    if (choice == compChoice):
        outcome.set("Tie!")
    elif (choice == "rock" and compChoice == "paper"):
        outcome.set("You win!")
    elif (choice == choice == "rock" and compChoice == "scissors"):
        outcome.set("You lost!")

def setPaper():
    choice = "paper"
    compChoiceRand = random.randint(1,3)

    if (compChoiceRand == 1):
        compChoice = "rock"
    elif (compChoiceRand == 2):
        compChoice = "paper"
    elif (compChoiceRand == 3):
        compChoice = "scissors"
    
    if (choice == compChoice):
        outcome.set("Tie!")
    elif (choice == choice == "paper" and compChoice == "scissors"):
        outcome.set("You win!")
    elif (choice == "paper" and compChoice == "rock"):
        outcome.set("You lost!")

def setScissors():
    choice = "scissors"
    compChoiceRand = random.randint(1,3)

    if (compChoiceRand == 1):
        compChoice = "rock"
    elif (compChoiceRand == 2):
        compChoice = "paper"
    elif (compChoiceRand == 3):
        compChoice = "scissors"
    
    if (choice == compChoice):
        outcome.set("Tie!")
    elif (choice == choice == "scissors" and compChoice == "rock"):
        outcome.set("You win!")
    elif (choice == "scissors" and compChoice == "paper"):
        outcome.set("You lost!")

rock = Button(root, text="Rock", command=setRock)
rock.grid(row=0, column=0)

paper = Button(root, text="Paper", command=setPaper)
paper.grid(row=0, column=1)

scissors = Button(root, text="Scissors", command=setScissors)
scissors.grid(row=0, column=2)

label = Label(root, textvariable=outcome)
label.grid(row=1, column=1)

root.mainloop() 