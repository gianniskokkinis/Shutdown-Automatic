from tkinter import *

def Exit():
    exit()


WarningWindow = Tk()
WarningWindow.title("No number input")
WarningWindow.geometry("400x200")
WarningWindow.grid()
WarningWindow.resizable(0,0)
WarningWindow.configure(bg='#444444')
FirstwarningText = Label(text="WARNING", font=("Comic Sans MS",30), bg="red")
FirstwarningText.grid()
warningText = Label(text="Please enter numbers to entry...", font=("Comic Sans MS",19), bg="#3696a3")
warningText.grid()
okButton = Button(text="OK", font=("Comic Sans MS",25), command=Exit)
okButton.grid()

WarningWindow.mainloop()
