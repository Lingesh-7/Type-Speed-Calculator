from tkinter import *
from tkinter import messagebox
import time


def check():
    # pass
    correct_words=[]
    # wrong_words=[]
    text_words=str(text_entry.get()).split()
    print(text_words)
    passages_words=str(passage()).replace('\n',' ').split()
    print(passages_words)
    for i in passages_words:
        for j in text_words:
            if i == j:
                correct_words.append(i)
            # elif i!=j:
            #     wrong_words.append(j)
            
    print(f"Correct words {len(correct_words)}\n ")
    sum_=0
    for i in correct_words:
        sum_+=len(i)
    # print(f"Correct Characters {sum_}\n ")

    wpm=(sum_/5)/1
    cpm=wpm*5

    # words_.destroy()
    # text_entry.delete(0,END)
    
    return(wpm,cpm)

    # wpm_label=Label(text=f"Your WPM and CPM is {wpm} and {cpm}\n ",font=("arial",35))
    # wpm_label.grid(column=5,row=6)

def timer():
    t=60
    while t>=0:
        time_show=Label(text=f"{t}",font=('arial',20))
        time_show.grid(column=5,row=5)
        window.update()
        time.sleep(1)
        if t==0:
            wpm,cpm=check()
            with open("typewriteScore.txt",'a') as f:
                f.write(f"WPM:{wpm} and CPM:{cpm}\n")
            messagebox.showinfo("Times'up",f"Your WPM and CPM is {wpm} and {cpm}")
        t-=1

def passage():
    
    with open("test1sp.txt","r") as f:

        w=f.read().split("\n\n")
        # print(w)
        f.close()
    return w[0]




window=Tk()
window.title("Type Speed Test⌛")
window.minsize(650,560)

title_=Label(text="Type Speed Test⌛",font=("arial",40))

title_.grid(column=5,row=1)

disc_=Label(text="How fast are your fingers? \nDo the one-minute typing test to find out! Press the space bar after each word. \nAt the end, you'll get your typing speed in CPM and WPM. \nGood luck!",font=("arial",15))
disc_.grid(column=5,row=2)

with open("typewriteScore.txt",'r') as f:
    last_=f.readlines()

Current_wpm_cpm=Label(text=f"Current:{last_[-1]}",font=('arial',15))
Current_wpm_cpm.grid(column=5,row=3)


words_=Label(text=f"\n\nSample text:\n\n{passage()}",font=("arial",14))
words_.grid(column=5,row=4)




text_entry=Entry( width=40, font=('arial', 20),justify=CENTER)
text_entry.grid(column=5,row=6)

timer()

window.mainloop()

