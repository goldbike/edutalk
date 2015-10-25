from tkinter import *
from tkinter.ttk import *

from tkinter.filedialog   import askopenfilename



def callback():
    name= askopenfilename() 
    print (name)
    
errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)

root = Tk()



root.mainloop()