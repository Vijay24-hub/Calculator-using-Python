"""
author: Vijay
"""
from tkinter import * 
import tkinter.font as font
import parser
from math import factorial

root=Tk()
root.title('Vision-Calculator')


# adding input widget to the calculator
input=Entry(root, width=60)
input.grid(row=0, columnspan=6, sticky=N+E+W+S, padx=15, pady=15)
myfont=font.Font(size=12, family='Helvetica')
equalto=font.Font(size=18, family='monospace')

# adding buttons to the calculator 
Button(root, text='7', height=2, width=2, font=myfont, border=None, command= lambda: get_variables(7)).grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='8', height=2, width=2, font=myfont,command= lambda: get_variables(8)).grid(row=2, column=1, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='9', height=2, width=2, font=myfont,command= lambda: get_variables(9)).grid(row=2, column=2, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='➗', height=2, width=2, font=myfont, fg='#4169e1', command= lambda: get_opearation('/')).grid(row=2, column=3, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='⌫', height=2, width=2, font=myfont, bg='#dae4ee', command= lambda: undo()).grid(row=2, column=4, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='AC', height=2, width=2, font=myfont, bg='#dae4ee',command= lambda: clear_all()).grid(row=2, column=5, sticky=N+S+E+W, padx=5, pady=5)

Button(root, text='4', height=2, width=2, font=myfont,command= lambda: get_variables(4)).grid(row=3, column=0, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='5', height=2, width=2, font=myfont,command= lambda: get_variables(5)).grid(row=3, column=1, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='6', height=2, width=2, font=myfont,command= lambda: get_variables(6)).grid(row=3, column=2, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='✖️', height=2, width=2, font=myfont, fg='#4169e1',command= lambda: get_opearation('*')).grid(row=3, column=3, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='%', height=2, width=2, font=myfont, bg='#e5edf1', command= lambda: get_opearation('%')).grid(row=3, column=4, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='!', height=2, width=2, font=myfont, bg='#e5edf1',command= lambda: fact()).grid(row=3, column=5, sticky=N+S+E+W, padx=5, pady=5)

Button(root, text='1', height=2, width=2, font=myfont,command= lambda: get_variables(1)).grid(row=4, column=0, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='2', height=2, width=2, font=myfont,command= lambda: get_variables(2)).grid(row=4, column=1, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='3', height=2, width=2, font=myfont,command= lambda: get_variables(3)).grid(row=4, column=2, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='➖', height=2, width=2, font=myfont, fg='#4169e1',command= lambda: get_opearation('-')).grid(row=4, column=3, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='(', height=2, width=2, font=myfont, bg='#e5edf1',command= lambda: get_opearation('(')).grid(row=4, column=4, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text=')', height=2, width=2, font=myfont, bg='#e5edf1',command= lambda: get_opearation(')')).grid(row=4, column=5, sticky=N+S+E+W, padx=5, pady=5)

Button(root, text='•', height=2, width=2, font=myfont,command= lambda: get_variables('.')).grid(row=5, column=0, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='0', height=2, width=2, font=myfont,command= lambda: get_variables(0)).grid(row=5, column=1, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='00', height=2, width=2, font=myfont,command= lambda: get_variables('00')).grid(row=5, column=2, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='➕', height=2, width=2, font=myfont, fg='#4169e1',command= lambda: get_opearation('+')).grid(row=5, column=3, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='π', height=2, width=2, font=myfont, bg='#e5edf1',command= lambda: get_opearation('*3.14')).grid(row=5, column=4, sticky=N+S+E+W, padx=5, pady=5)
Button(root, text='exp', height=2, width=2, font=myfont, bg='#e5edf1',command= lambda: get_opearation('**')).grid(row=5, column=5, sticky=N+S+E+W, padx=5, pady=5)

Button(root, text='=', height=0, font=equalto, bg='#dae4ee',command= lambda: calculate()).grid( columnspan=6, sticky=N+S+E+W, padx=5, pady=5)

# mapping the digits
i=0
def get_variables(num):
    global i
    input.insert(i, num)
    i+=1

# mapping the opearators
def get_opearation(opearator):
    global i    
    length=len(opearator)
    input.insert(i,opearator)
    i+=length

# mapping the AllClear
def clear_all():
    input.delete(0,END)

# mapping the undo 
def undo():
    entire_string=input.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        input.insert(0,new_string)
    else:
        clear_all()
        input.insert(0,"Error")

# mapping '=' button
def calculate():
    entire_string=input.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clear_all()
        input.insert(0,result)
    except Exception:
        clear_all()
        input.insert(0,"Error")

# mapping factorial button
def fact():
    entire_string=input.get()
    try:
        result=factorial(int(entire_string))
        clear_all()
        input.insert(0,result)
    except Exception:
        clear_all()
        input.insert(0,"Error")

root.mainloop()
