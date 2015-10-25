from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Lecture Uploader")
frame = Frame(root)

year = 2015

def setYear(event):
    year = comboYear.get()
    print(year)



labelYear = Label(frame, text = "  Year  ")
comboYear = Combobox(frame, textvariable = "year")
comboYear['values'] = ('2011', '2012')
comboYear.current(0)
comboYear.bind("<<ComboboxSelected>>", setYear)

labelSemester = Label(frame, text = "  Semester  ")
comboSemester = Combobox(frame, textvariable = "semester")
comboSemester['values'] = ('01', '02')
comboSemester.current(0)

labelLecture = Label(frame, text = "  Lecture  ")
comboLecture = Combobox(frame, textvariable = "lecture")
comboLecture['values'] = ('2D게임프로그래밍', '종합설계기획', '종합설계(II)')
comboLecture.current(0)




labelYear.grid(row = 0, column = 0, sticky=E)
comboYear.grid(row = 0, column = 1, sticky=E)
labelSemester.grid(row = 0, column = 2, sticky=E)
comboSemester.grid(row = 0, column = 3, sticky=E)
labelLecture.grid(row = 0, column = 4, sticky=E)
comboLecture.grid(row = 0, column = 5, sticky=E)


frame.pack(padx=10, pady=10)

root.mainloop()