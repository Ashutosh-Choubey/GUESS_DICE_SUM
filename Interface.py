import Dicegenerator
from tkinter import *
value={
    1:'\u00B7',
    2:':',
    3:'''\u00B7\u00B7\u00B7''',
    4:'::',
    5:':\u00B7:',
    6:':::',
}
def diceInterface(a):
    c=d.cal(a)
    D1['text']=value.get(d.number[0],d.number[0])
    D2['text']=value.get(d.number[1],d.number[1])
    sum=d.number[0]+d.number[1]
    D1.focus_displayof()
    D2.focus_displayof()
    if c:
        l2 = Label(root, text=f'RIGHT {sum}', fg='white', bg='green',width=10,font=['bold',50])
        l2.place(x=70,y=350)
        l1['bg']='green'
        root['bg']='green'
    else:
        l3=Label(root,text=f'WRONG {sum}',fg='white',bg='red',width=10,font=['bold',50])
        l3.place(x=70,y=350)
        root['bg']='red'
        l1['bg']='red'
root = Tk()
root['bg']='Black'
root.title("Guess The SUM")
l1=Label(root,text="GUESS SUM",fg='white',width=10,font=['bold',50],bg='Black')
d=Dicegenerator.Dice()
D1 = Label(root, text="❓",width=3,height=2,font=["bold", 45], bg="white", fg="red")
D2 = Label(root, text="❓",width=3,height=2, font=["bold", 45], bg="white", fg="red")
b1=Button(root,text="Above 7",width=8,height=5,font=["bold", 20],command=lambda:diceInterface(1),bg='Yellow')
b2=Button(root,text="Exactly 7",width=8,height=5,font=["bold", 20],command=lambda:diceInterface(3),bg='Blue')
b3=Button(root,text="Below 7",width=8,height=5,font=["bold", 20],command=lambda:diceInterface(2),bg='Brown')
l1.place(x=70,y=0)
D1.place(x=85, y=100)
D2.place(x=315, y=100)
b1.place(x=30,y=450)
b2.place(x=180,y=450)
b3.place(x=330,y=450)
root.geometry("500x700")
root.mainloop()