from tkinter import *    
from tkinter.ttk import *
import random

root = Tk()
root.title("RPS!")             
root.geometry('200x200')  

choice = StringVar()
outcome = StringVar()
compChoice = ""

choiceEntry = Entry(root, textvariable=choice)
choiceEntry.pack()

label = Label(root, textvariable=outcome)
label.pack()

def play():
    compChoiceRand = random.randint(1,3)
    choice = choiceEntry.get()

    if (compChoiceRand == 1):
        compChoice = "rock"
    elif (compChoiceRand == 2):
        compChoice = "paper"
    elif (compChoiceRand == 3):
        compChoice = "scissors"
    
    if (choice == compChoice):
        outcome.set("Tie!")
    elif (choice == "rock" and compChoice == "paper" or choice == "scissors" and compChoice == "rock" or choice == "paper" and compChoice == "scissors"):
        outcome.set("You win!")
    elif (choice == "paper" and compChoice == "rock" or choice == "rock" and compChoice == "scissors" or choice == "scissors" and compChoice == "paper"):
        outcome.set("You lost!")

btn = Button(root, text = 'Click me !', command = play) 
btn.pack(side="top")

root.mainloop() 