#Welcome to Automatic-shutdown!
#I create this program to set your shutdown time for your computer. I hope you have fun with my program.
#Thank you for support 😉👨🏽‍💻
#CREATED BY BILOTO567


from tkinter import*
import os


#custom functions
def Exit():
    exit()


def WarningMessage():
    os.system('WarningMessage.py')



#define hours 
def Shutdown30():
    f = open('shudown30.bat','x')
    f.write(str("shutdown -s -t 1800"))
    f.close()
    os.system("shudown30.bat")
    os.remove("shudown30.bat")
    exit()

def Shutdown1h():
    f = open('shutdown1H.bat','x')
    f.write(str("shutdown -s -t 3600"))
    f.close()
    os.system("shutdown1H.bat")
    os.remove('shutdown1H.bat')
    exit()



def Shutdown2h():
    f = open('shutdown2H.bat','x')
    f.write(str("shutdown -s -t 7200"))
    f.close()
    os.system("shutdown2H.bat")
    os.remove("shutdown2H.bat")
    exit()



def shutdownUser():
    Time = str(UserInput.get())
    try:
        newTime = int(Time)
    except:
        newTime = "null"

    
    if type(newTime) is int:
        FinalTime = newTime*3600
        setTime = str(FinalTime)
        print(setTime)
        f = open('UserInput.bat','x')
        f.write(str("shutdown -s -t "+setTime))
        f.close()
        os.system('UserInput.bat')
        os.remove('UserInput.bat')
        exit()
    else:
        WarningMessage()





#main program
window = Tk()
window.title("Auto Shutdown")
window.geometry("760x600")
window.configure(bg="#444444")
window.grid()
window.resizable(0,0)
text = Label(master=window, text="Welcome to Auto-Shutdown! \n You can chose you shutdown time from our menu:", font=("Comic Sans MS",24), bg="#0fdbb2")
text.grid()
RecommendedText = Label(master=window, text="Recommended Time:", font=("Impact",38), bg="#24936b")
RecommendedText.grid()
Button30 = Button(master=window, text="30 MINUTES", font=("Comic Sans MS",20), bg="#3569ea", command=Shutdown30)
Button30.grid()
Button1h = Button(master=window, text="1 HOUR", font=("Comic Sans MS",20), bg="#3569ea", command=Shutdown1h)
Button1h.grid()
Button2h = Button(master=window, text="2 HOURS", font=("Comic Sans MS",20), bg="#3569ea", command=Shutdown2h)
Button2h.grid()
UserInputText = Label(master=window, text="How many time do you want?(Hours)", font=("Impact",38), bg="#24936b")
UserInputText.grid(column=0, row=10)
UserInput = Entry()
UserInput.grid()
UserInputButton = Button(master=window, text="OK", font=("Impact",20), bg="#6f0f89", command=shutdownUser)
UserInputButton.grid(column=0, row=20)

window.mainloop()



