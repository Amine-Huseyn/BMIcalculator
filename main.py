import tkinter

#window
window = tkinter.Tk()
window.title("BMI CALCULATOR")
window.minsize(width=400, height=400)
window.configure(background="black")

def clickbutton():
        height = myentry2.get()
        weight = myentry.get()
        age = myentry3.get()

        if weight == "" or height == "" or age == "":
            resultlabel.config(text="Please enter your information")
        else:
            try:
                bmi = float(weight) / ((float(height) / 100) ** 2)
                resultstring = result(bmi)
                resultlabel.config(text=resultstring)
            except:
                resultlabel.config(text="Please enter available number!!!",font=("Arial",10,"bold"))
                resultlabel.config( fg="red")

def result(bmi):
    resultstring = f"Your BMI is {round(bmi, 2)}."
    if bmi <= 16:
        resultstring += "You're most thin"
    elif 16 < bmi <= 17:
        resultstring += "You're moderately slim"
    elif 17 < bmi <= 18.5:
        resultstring += "You're mild slim"
    elif 18.5 < bmi <= 25:
        resultstring += "You're good!"
    elif 25 < bmi <= 30:
        resultstring += "As for me we must sport:("
    elif 30 < bmi <= 35:
        resultstring += "STOP! You go to be obese "
    elif 35 < bmi <= 40:
        resultstring += ".....I think we mustn't eat at night:) "
    else:
        resultstring += "RUN TO GYM"
    return resultstring

#label
mylabel= tkinter.Label(text="Enter your weight(kg)", font=("Arial",10,"bold"))
mylabel.config(bg="black",fg="white")
mylabel.place(x=130,y=50)

mylabel= tkinter.Label(text="Enter your age", font=("Arial",10,"bold"))
mylabel.config(bg="black",fg="white")
mylabel.place(x=150,y=170)

mylabel= tkinter.Label(text="Enter your height(cm)", font=("Arial",10,"bold"))
mylabel.config(bg="black",fg="white")
mylabel.place(x=130,y=110)

mylabel= tkinter.Label(text="Results", font=("Arial",13,"bold"))
mylabel.config(bg="black",fg="white")
mylabel.place(x=165,y=230)

#button
mybutton=tkinter.Button(text="Calculate",command=clickbutton)
mybutton.place(x=170,y=300)

#entry
myentry=tkinter.Entry(width=20)
myentry.place(x=140,y=80)

myentry2=tkinter.Entry(width=20)
myentry2.place(x=140,y=140)

myentry3=tkinter.Entry(width=20)
myentry3.place(x=140,y=200)

resultlabel=tkinter.Label(width=30)
resultlabel.place(x=100,y=260)


window.mainloop()