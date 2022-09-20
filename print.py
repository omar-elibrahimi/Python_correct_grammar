from textblob import TextBlob
from tkinter import *

def  Auto_correct():
    corrected_words = []
    text = Input_text.get(1.0, END).split(" ")
    for i in text:
        corrected_words.append(TextBlob(i))
    Output_text.delete(1.0,END)
    for i in corrected_words:
        Output_text.insert(END, i.correct() + " ")


mainwin = Tk()
mainwin.geometry('1400x520')
mainwin.resizable(False,False)
mainwin.title("autocorrect")
mainwin.config(bg='#82CEC7')


Label(mainwin, text="Enter Text", font='arial 18 bold', bg='#82CEC7').place(x=250, y=90)
Input_text = Text(mainwin, font='arial 13', bg ='white', height=11, wrap=WORD, padx=5, pady=5, width=50, insertbackground='black')
Input_text.place(x=30, y=130)




Label(mainwin, text="Output", font='arial 18 bold', bg='#82CEC7').place(x=1010, y=90)
Output_text = Text(mainwin, font='arial 13', bg ='white', height=11, wrap=WORD, padx=5, pady=5, width=50, insertbackground='black')
Output_text.place(x=750, y=130)

auto_correct_btn = Button(mainwin, text="Correct", bg='#36BCB0', width=40, font='arial 18 bold', pady=3, command=Auto_correct)
auto_correct_btn.place(x=320, y=440)

mainwin.mainloop()