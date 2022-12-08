from tkinter import*
import string
win=Tk()
win.geometry("400x400")

def cat():
    S=str(e1.get())
    E=str.maketrans(dict.fromkeys(string.punctuation)) 
    E3=S.translate(E)
    e2.insert(0,E3)


L1 = Label(text="введіть рядок",fg='black',bg='white',width=20)
e1 = Entry(fg='black',bg='white',width=24)
e2 = Entry(fg='black',bg='white',width=20)
button = Button(text='Delete',width=24,height=1,background='black',foreground='white',command=cat)


L1.place(x=5,y=30)
e1.place(x=5,y=50)
e2.place(x=200,y=30)
button.place(x=135,y=100)
win.mainloop()



