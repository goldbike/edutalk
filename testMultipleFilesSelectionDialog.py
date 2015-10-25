from tkinter import *
from tkinter.ttk import *
from os import *

from tkinter.filedialog   import askopenfilenames

root = Tk()



def callback():
    fileNames = askopenfilenames()
    for pathName in fileNames:
        print(pathName)
        fileListbox.insert(0, path.split(pathName)[-1])
        fileInfo.insert(INSERT, path.split(pathName)[-1])




fileListbox = Listbox(root)
var = StringVar()
fileInfo = Label(root, textvariable = var)

var.set('test test test test test test test test info')

fileSelectionButton = Button(root, text='File Open', command=callback)

fileListbox.grid(row=0)
fileSelectionButton.grid(row=1)
fileInfo.grid(row=2)



root.mainloop()