from tkinter import *  
from tkinter.font import BOLD
import math

root = Tk()
display = IntVar()
expression = "" 

class Calc:
    def __init__(self, master):
        frame = Frame(master, width=379, height=600, bg='#262626')
        frame.pack()

        self.entry = Entry(frame, font=("Segoe UI", 36, BOLD), fg='white',bg='#262626', bd=0, textvariable=display, justify='right' )
        self.entry.place(x=5, y=15, width=368, height=185)

        self.label = Label(frame, text="Standard", font=("Segoe UI", 16),fg='white', bg='#262626', justify='right')
        self.label.place(x=5, y=10, width=368)

        self.label = Label(frame, text="       MC             MR             M+              M-             MS",
        font=("Segoe UI", 10, BOLD), fg='white', bg='#262626')
        self.label.place(x=5, y=170)

    # Numericals
        self.num_0 = Button(frame, relief=FLAT, font=("Segoe UI", 16, BOLD), bg='#121212', text='0', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("0"))
        self.num_1 = Button(frame, relief=FLAT, font=("Segoe UI", 16, BOLD), bg='#121212', text='1', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("1"))
        self.num_2 = Button(frame, relief=FLAT, font=("Segoe UI", 16, BOLD), bg='#121212', text='2', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("2"))
        self.num_3 = Button(frame, relief=FLAT, font=("Segoe UI", 16, BOLD), bg='#121212', text='3', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("3"))
        self.num_4 = Button(frame, relief=FLAT, font=("Segoe UI", 16, BOLD), bg='#121212', text='4', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("4"))
        self.num_5 = Button(frame, relief=FLAT, font=("Segoe UI", 16, BOLD), bg='#121212', text='5', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("5"))
        self.num_6 = Button(frame, relief=FLAT, font=("Segoe UI", 16, BOLD), bg='#121212', text='6', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("6"))
        self.num_7 = Button(frame, relief=FLAT, font=("Segoe UI", 16, BOLD), bg='#121212', text='7', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("7"))
        self.num_8 = Button(frame, relief=FLAT, font=("Segoe UI", 16, BOLD), bg='#121212', text='8', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("8"))
        self.num_9 = Button(frame, relief=FLAT, font=("Segoe UI", 16, BOLD), bg='#121212', text='9', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("9"))

    # Operators
        self.operator_1 = Button(frame, relief=FLAT,font=("Segoe UI", 16), bg='#1c1c1c',text='+/_', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("-"))
        self.operator_2 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='.', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("."))
        self.operator_3 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='=', fg='white',
         activebackground='#262626', activeforeground='white', command=self.equalpress)
        self.operator_4 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='+', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("+"))
        self.operator_5 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='-', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("-"))
        self.operator_6 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='×', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("*"))
        self.operator_7 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='CE', fg='white',
         activebackground='#262626', activeforeground='white', command=self.clear)
        self.operator_8 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='C', fg='white',
         activebackground='#262626', activeforeground='white', command=self.clear)
        self.operator_9 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='<---', fg='white',
         activebackground='#262626', activeforeground='white', command=self.backspace)
        self.operator_10 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='÷', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("/"))
        self.operator_11 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='%', fg='white',
         activebackground='#262626', activeforeground='white', command=self.percent)
        self.operator_12 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='√x', fg='white',
         activebackground='#262626', activeforeground='white', command=self.sqrt)
        self.operator_13 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='x²', fg='white',
         activebackground='#262626', activeforeground='white', command=self.pow)
        self.operator_14 = Button(frame, relief=FLAT, font=("Segoe UI", 16), bg='#1c1c1c', text='1/x', fg='white',
         activebackground='#262626', activeforeground='white', command=lambda:self.showtext("1/x"))

    # Placing
        self.num_0.place(x=98, y=533, width=90, height=63)
        self.num_1.place(x=5, y=467, width=90, height=63)
        self.num_2.place(x=98, y=467, width=90, height=63)      
        self.num_3.place(x=191, y=467, width=90, height=63)
        self.num_4.place(x=5, y=401, width=90, height=63)
        self.num_5.place(x=98, y=401, width=90, height=63)
        self.num_6.place(x=191, y=401, width=90, height=63)
        self.num_7.place(x=5, y=335, width=90, height=63) 
        self.num_8.place(x=98, y=335, width=90, height=63) 
        self.num_9.place(x=191, y=335, width=90, height=63)

        self.operator_1.place(x=5, y=533, width=90, height=63)
        self.operator_2.place(x=191, y=533, width=90, height=63)
        self.operator_3.place(x=284, y=533, width=90, height=63)
        self.operator_4.place(x=284, y=467, width=90, height=63)
        self.operator_5.place(x=284, y=401, width=90, height=63)    
        self.operator_6.place(x=284, y=335, width=90, height=63)
        self.operator_7.place(x=5, y=269, width=90, height=63)
        self.operator_8.place(x=98, y=269, width=90, height=63) 
        self.operator_9.place(x=191, y=269, width=90, height=63)
        self.operator_10.place(x=284, y=269, width=90, height=63)
        self.operator_11.place(x=5, y=203, width=90, height=63)
        self.operator_12.place(x=98, y=203, width=90, height=63)
        self.operator_13.place(x=191, y=203, width=90, height=63)
        self.operator_14.place(x=284, y=203, width=90, height=63)

    # Functions
    def clear(self):
        global expression
        expression = ""
        display.set("0") 

    def backspace(self):
        self.entry.delete(0, last=1)

    def showtext(self, text):
        global expression

        expression = expression + str(text)
        display.set(expression)

    def equalpress(self): 
        try: 
  
            global expression 
            total = str(eval(expression))
            display.set(total) 
        
        except: 
  
            display.set(" error ") 
            expression = "" 
    
    def pow(self):  
        global expression
        
        total = str(int(expression) * int(expression))
        display.set(total)
    
    def sqrt(self):
        global expression

        total = str(math.sqrt(int(expression)))
        display.set(total)

    def percent(self):
        global expression

        total = str(int(expression)/100)
        display.set(float(total))

c = Calc(root)
root.title("Calculator")
root.mainloop()

