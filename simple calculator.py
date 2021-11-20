#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.geometry("330x550")
root.resizable(0,0)
fontype=("arial",22)
num=StringVar()
def square():
        global entry
        result=str(eval(f"{entry}**2"))
        num.set(result)
        
def squareroot():
        global entry
        result=str(eval(f"{entry}**0.5"))
        num.set(result)
def btnclick(item):
    global entry
    entry=entry+str(item)
    num.set(entry)
    
def equal():
    global entry
    result=str(eval(entry))
    num.set(result)
    entry=""
def clear():
    global entry
    entry=""
    num.set("")
entry=""
enter=Entry(root,bg="white",fg="black",border=0,text=num,font=fontype,justify="right").place(height=100,width=329)
btn_clr=Button(root,text="C",padx=16,pady=8,font=fontype,border=0,command=clear).place(x=1,y=100)
btn_sqr=Button(root,text="x\u00b2",padx=16,pady=8,font=fontype,border=0,command=square).place(x=82.5,y=100)
btn_sqrroot=Button(root,text="\u221ax",padx=16,pady=8,font=fontype,border=0,command=squareroot).place(x=165,y=100)
btn_dividet=Button(root,text="÷",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick("/")).place(x=255,y=100)
btn_7=Button(root,text="7",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(7)).place(x=1,y=187.5)
btn_8=Button(root,text="8",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(8)).place(x=82.5,y=187.5)
btn_9=Button(root,text="9",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(9)).place(x=165,y=187.5)
btn_x=Button(root,text="x",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick("*")).place(x=255,y=187.5)
btn_4=Button(root,text="4",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(4)).place(x=1,y=275)
btn_5=Button(root,text="5",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(5)).place(x=82.5,y=275)
btn_6=Button(root,text="6",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(6)).place(x=165,y=275)
btn_sub=Button(root,text="-",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick("-")).place(x=255,y=275)
btn_1=Button(root,text="1",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(1)).place(x=1,y=362.5)
btn_2=Button(root,text="2",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(2)).place(x=82.5,y=362.5)
btn_2=Button(root,text="3",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(3)).place(x=165,y=362.5)
btn_add=Button(root,text="+",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick("+")).place(x=255,y=362.5)
btn_dot=Button(root,text=".",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(".")).place(x=1,y=450)
btn_0=Button(root,text="0",padx=16,pady=8,font=fontype,border=0,command=lambda:btnclick(0)).place(x=82.5,y=450)
btn_equal=Button(root,text="=",padx=70,pady=8,font=fontype,border=0,bg="lightblue",command=equal).place(x=165,y=450)
lbl=Label(root,text="Made by Parveen Kumar and Rakesh Malik",fg="magenta").place(x=38,y=520)
root.mainloop()


# In[ ]:





# In[ ]:




