from tkinter import *
import json
import pylab

win= Tk() 
win.geometry("200x150")

L1 = Label(text=" Це порівняльна таблиця",fg='black',bg='white',width=30,height=6)


with open("D:\Git\Repos\VKN\ison.json","r") as f:
    temp = json.load(f)
    temp1 = list(temp.copy())
value=[]
for i in temp:
    value.append(temp[i])

L1.place(x=5,y=30)


pylab.bar(temp1,value)
pylab.show()

win.mainloop()

