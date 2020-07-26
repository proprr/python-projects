from tkinter import Tk, StringVar
from tkinter.ttk import Entry, Button

root = Tk()

textContent = StringVar()
charContent = StringVar()
res = ""
output = ""

root.geometry('520x250')
root.title('Text2Cum')
root.resizable(0,0)

textEntry = Entry(root, textvariable=textContent, width=35)
textEntry.grid(row=0, column=0)

charEntry = Entry(root, textvariable=charContent, width=5)
charEntry.grid(row=0, column=1)

def writeToFile():
    output = open("output.txt", 'w+')
    res = textEntry.get().replace(charEntry.get(), "cum")
    output.write(res)

cumSubmit = Button(root, text="Cum!", command=writeToFile).grid(row=0, column=2)

root.mainloop()