from tkinter import*
from tkinter import ttk
from simpleeval import simple_eval, InvalidExpression

win=Tk()
data=""
def evaluate_expression(expression):
    try:
        # Evaluate the expression using simpleeval
        result = simple_eval(expression)
        return result
    except InvalidExpression as e:
        value.set("Error!")
    except ZeroDivisionError:
        value.set("Error!")


def topp(num_f):
    mod_num=num_f.replace('X','*')
    expr = mod_num
    display_label.config(text=str(evaluate_expression(expr)))

def topp_t1(num_f):
    mod_num=num_f.replace('X','*')
    if mod_num[-1] in ['*','-','+','/']:
        mod_num1=mod_num[:-1]
        expr = mod_num1
        display_label.config(text=str(evaluate_expression(expr)))
    else:
        expr = mod_num
        display_label.config(text=str(evaluate_expression(expr)))


def square_e(num):
    mod_num=num.replace('X','*')
    ans=evaluate_expression(mod_num)
    ans_e=ans**2
    value.set(str(ans_e))
    display_label.config(text=str(ans_e))
    
    

def square():
    num=value.get()
    if '.' in num:
        if num[-1] in ['X','-','+','/','.']:
            modify=num[:-1]
            square_e(modify)
        else:
            square_e(num)
    else:
        if num[-1] in ['X','-','+','/']:
            modify=num[:-1]
            square_e(modify)
        else:
            square_e(num)

def fraction():
    num=int(value.get())
    if num==0:
        display_label.config(text='Error')
    else:
        cal=1/num
        value.set(str(cal))
        display_label.config(text=str(cal))

def backspace():
    num=value.get()
    if num=='0':
        value.set('0')
    else:
        modify=num[0:-1]
        value.set(modify)
        updt=value.get()
        if updt=='':
            value.set('0')
            display_label.config(text='')
        else:
            value.set(modify)
            num1=value.get()
            if num1[-1] in ['X','-','+','/']:

                modify1=num1[:-1]
                topp(modify1)
            else:
                
                topp(num1)


def multiply():
    num=value.get()
    
    if num[-1] in ['1','2','3','4','5','6','7','8','9','0']: 
        modify=num+'X'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)
    elif num[-1] in ['X','/','-','+','.']:
        pass

def seven():
    num=value.get()
    if num=='0':
        value.set('')
        value.set('7')
        num2=value.get()
        topp_t1(num2)
    else:
        modify=num+'7'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)


def eight():
    num=value.get()
    if num=='0':
        value.set('')
        value.set('8')
        num2=value.get()
        topp_t1(num2)
    else:
        modify=num+'8'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)

def nine():
    num=value.get()
    if num=='0':
        value.set('')
        value.set('9')
        num2=value.get()
        topp_t1(num2)
    else:
        modify=num+'9'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)

def addd():
    num=value.get()
    
    if num[-1] in ['1','2','3','4','5','6','7','8','9','0']: 
        modify=num+'+'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)
    elif num[-1] in ['X','/','-','+','.']:
        pass

def four():
    num=value.get()
    if num=='0':
        value.set('')
        value.set('4')
        num2=value.get()
        topp_t1(num2)
    else:
        modify=num+'4'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)

def five():
    num=value.get()
    if num=='0':
        value.set('')
        value.set('5')
        num2=value.get()
        topp_t1(num2)
    else:
        modify=num+'5'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)

def six():
    num=value.get()
    if num=='0':
        value.set('')
        value.set('6')
        num2=value.get()
        topp_t1(num2)
    else:
        modify=num+'6'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)
def subs():
    num=value.get()
    
    if num[-1] in ['1','2','3','4','5','6','7','8','9','0']: 
        modify=num+'-'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)
    elif num[-1] in ['X','/','-','+','.']:
        pass

def one():
    num=value.get()
    if num=='0':
        value.set('')
        value.set('1')
        num2=value.get()
        topp_t1(num2)
    else:
        modify=num+'1'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)

def two():
    num=value.get()
    if num=='0':
        value.set('')
        value.set('2')
        num2=value.get()
        topp_t1(num2)
    else:
        modify=num+'2'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)

def three():
    num=value.get()
    if num=='0':
        value.set('')
        value.set('3')
        num2=value.get()
        topp_t1(num2)
    else:
        modify=num+'3'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)

def divisionn():
    num=value.get()
    
    if num[-1] in ['1','2','3','4','5','6','7','8','9','0']: 
        modify=num+'/'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)
    elif num[-1] in ['X','/','-','+','.']:
        pass

def dot():
    num=value.get()
    
    if num[-1] not in ['.']: 
        modify=num+'.'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)
    elif num[-1] in ['.']:
        pass
   
    

def zero():
    num=value.get()
    if num=='0':
        value.set('')
        value.set('0')
        num2=value.get()
        topp_t1(num2)
    else:
        modify=num+'0'
        value.set(modify)
        num2=value.get()
        topp_t1(num2)

def deletee():
    value.set('0')
    display_label.config(text='')

def equall():
    num=value.get()
    display_label.config(text=num)
    mod_num=num.replace('X','*')
    if mod_num[-1] in ['*','-','+','/']:
        mod_num1=mod_num[:-1]
        expr = mod_num1
        value.set(str(evaluate_expression(expr)))
    else:
        expr = mod_num
        value.set(str(evaluate_expression(expr)))
    

win.geometry("350x550")
win.title("CALCULATOR")
win.config(bg="#f2f3f4")
win.iconbitmap("cal.ico")
win.resizable(False,False)

# calculation display area------------------------------------------------

display_label=Label(win,text='',font=("Aptos",14),height=5,bg="#f0f3f4",fg="#7b7d7d",bd=4,relief=SUNKEN,anchor='nw')
display_label.pack(side=TOP,fill=X,pady=10,padx=10)
value=StringVar()
display_entry=Entry(win,font=("Arial Black",30),bg="#f0f3f4",bd=2,relief=FLAT,textvariable=value)
display_entry.place(x=15,y=63,width=310)
value.set('0')

# square of x button==============

imgx2=PhotoImage(file="x2.png")
button_x2=Button(win,image=imgx2,command=square,justify='center',bg="#f7f9f9",relief='raised')
button_x2.place(x=10,y=140,height=70,width=80)

# 1/x button==============

img1x=PhotoImage(file="half.png")
button_12=Button(win,image=img1x,command=fraction,justify='center',bg="#f7f9f9",relief='raised')
button_12.place(x=90,y=140,height=70,width=80)

imgbsps=PhotoImage(file="back.png")
button_back=Button(win,image=imgbsps,command=backspace,justify='center',bg="#f7f9f9",relief='raised')
button_back.place(x=170,y=140,height=70,width=80)

imgmul=PhotoImage(file="mul.png")
button_mul=Button(win,image=imgmul,command=multiply,justify='center',bg="#f7f9f9",relief='raised')
button_mul.place(x=260,y=140,height=70,width=80)


# ------------------row7,8,9,add-----------------------------------------

img7=PhotoImage(file="7.png")
button7=Button(win,image=img7,command=seven,justify='center',bg="#f7f9f9",relief='raised')
button7.place(x=10,y=220,height=70,width=80)

img8=PhotoImage(file="8.png")
button8=Button(win,image=img8,command=eight,justify='center',bg="#f7f9f9",relief='raised')
button8.place(x=90,y=220,height=70,width=80)

img9=PhotoImage(file="9.png")
button9=Button(win,image=img9,command=nine,justify='center',bg="#f7f9f9",relief='raised')
button9.place(x=170,y=220,height=70,width=80)

imgadd=PhotoImage(file="add.png")
button_add=Button(win,image=imgadd,command=addd,justify='center',bg="#f7f9f9",relief='raised')
button_add.place(x=260,y=220,height=70,width=80)

# ------------------row4,5,6,sub-----------------------------------------

img4=PhotoImage(file="4.png")
button4=Button(win,image=img4,command=four,justify='center',bg="#f7f9f9",relief='raised')
button4.place(x=10,y=300,height=70,width=80)

img5=PhotoImage(file="5.png")
button5=Button(win,image=img5,command=five,justify='center',bg="#f7f9f9",relief='raised')
button5.place(x=90,y=300,height=70,width=80)

img6=PhotoImage(file="6.png")
button6=Button(win,image=img6,command=six,justify='center',bg="#f7f9f9",relief='raised')
button6.place(x=170,y=300,height=70,width=80)

imgsub=PhotoImage(file="sub.png")
button_sub=Button(win,image=imgsub,command=subs,justify='center',bg="#f7f9f9",relief='raised')
button_sub.place(x=260,y=300,height=70,width=80)

# ------------------row 1,2,3,div-----------------------------------------

img1=PhotoImage(file="1.png")
button1=Button(win,image=img1,command=one,justify='center',bg="#f7f9f9",relief='raised')
button1.place(x=10,y=380,height=70,width=80)

img2=PhotoImage(file="2.png")
button2=Button(win,image=img2,command=two,justify='center',bg="#f7f9f9",relief='raised')
button2.place(x=90,y=380,height=70,width=80)

img3=PhotoImage(file="3.png")
button3=Button(win,image=img3,command=three,justify='center',bg="#f7f9f9",relief='raised')
button3.place(x=170,y=380,height=70,width=80)

imgdiv=PhotoImage(file="div.png")
button_div=Button(win,image=imgdiv,command=divisionn,justify='center',bg="#f7f9f9",relief='raised')
button_div.place(x=260,y=380,height=70,width=80)

# ------------------row .,0,c,=-----------------------------------------

imgdot=PhotoImage(file="dot.png")
button_dot=Button(win,image=imgdot,command=dot,justify='center',bg="#f7f9f9",relief='raised')
button_dot.place(x=10,y=460,height=70,width=80)

img0=PhotoImage(file="0.png")
button2=Button(win,image=img0,command=zero,justify='center',bg="#f7f9f9",relief='raised')
button2.place(x=90,y=460,height=70,width=80)

imgdel=PhotoImage(file="delt.png")
button_del=Button(win,image=imgdel,command=deletee,justify='center',bg="#f7f9f9",relief='raised')
button_del.place(x=170,y=460,height=70,width=80)

imgequal=PhotoImage(file="eqq.png")
button_div=Button(win,image=imgequal,command=equall,justify='center',bg="#f7f9f9",relief='raised')
button_div.place(x=260,y=460,height=70,width=80)


win.mainloop()