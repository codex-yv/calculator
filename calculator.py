from tkinter import*
from tkinter import ttk
from simpleeval import simple_eval, InvalidExpression
from PIL import Image, ImageTk
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

def resize_image(image_path, size):  
        with Image.open(image_path) as img:
            img = img.resize(size)  
            return ImageTk.PhotoImage(img)
    

win.geometry("350x570")
win.title("CALCULATOR")
win.config(bg="#f2f3f4")
win.iconbitmap("cal.ico")
win.resizable(False,False)

tab=ttk.Notebook(win)
tab.pack(expand=True, fill="both")

calframe=ttk.Frame(tab)
menuframe = ttk.Frame(tab)

tab.add(calframe, text="Calculator")
tab.add(menuframe, text="Menu")



# calculation display area------------------------------------------------

display_label=Label(calframe,text='',font=("Aptos",14),height=4,bg="#f0f3f4",fg="#7b7d7d",bd=4,relief=SUNKEN,anchor='nw')
display_label.pack(side=TOP,fill=X,pady=20,padx=10)
value=StringVar()
display_entry=Entry(calframe,font=("Arial Black",30),bg="#f0f3f4",bd=2,relief=FLAT,textvariable=value)
display_entry.place(x=15,y=55,width=310)
value.set('0')

# square of x button==============

imgx2=PhotoImage(file="x2.png")
button_x2=Button(calframe,image=imgx2,command=square,justify='center',bg="#f7f9f9",relief='raised')
button_x2.place(x=10,y=140,height=70,width=80)

# 1/x button==============

img1x=PhotoImage(file="half.png")
button_12=Button(calframe,image=img1x,command=fraction,justify='center',bg="#f7f9f9",relief='raised')
button_12.place(x=90,y=140,height=70,width=80)

imgbsps=PhotoImage(file="back.png")
button_back=Button(calframe,image=imgbsps,command=backspace,justify='center',bg="#f7f9f9",relief='raised')
button_back.place(x=170,y=140,height=70,width=80)

imgmul=PhotoImage(file="mul.png")
button_mul=Button(calframe,image=imgmul,command=multiply,justify='center',bg="#f7f9f9",relief='raised')
button_mul.place(x=260,y=140,height=70,width=80)


# ------------------row7,8,9,add-----------------------------------------

img7=PhotoImage(file="7.png")
button7=Button(calframe,image=img7,command=seven,justify='center',bg="#f7f9f9",relief='raised')
button7.place(x=10,y=220,height=70,width=80)

img8=PhotoImage(file="8.png")
button8=Button(calframe,image=img8,command=eight,justify='center',bg="#f7f9f9",relief='raised')
button8.place(x=90,y=220,height=70,width=80)

img9=PhotoImage(file="9.png")
button9=Button(calframe,image=img9,command=nine,justify='center',bg="#f7f9f9",relief='raised')
button9.place(x=170,y=220,height=70,width=80)

imgadd=PhotoImage(file="add.png")
button_add=Button(calframe,image=imgadd,command=addd,justify='center',bg="#f7f9f9",relief='raised')
button_add.place(x=260,y=220,height=70,width=80)

# ------------------row4,5,6,sub-----------------------------------------

img4=PhotoImage(file="4.png")
button4=Button(calframe,image=img4,command=four,justify='center',bg="#f7f9f9",relief='raised')
button4.place(x=10,y=300,height=70,width=80)

img5=PhotoImage(file="5.png")
button5=Button(calframe,image=img5,command=five,justify='center',bg="#f7f9f9",relief='raised')
button5.place(x=90,y=300,height=70,width=80)

img6=PhotoImage(file="6.png")
button6=Button(calframe,image=img6,command=six,justify='center',bg="#f7f9f9",relief='raised')
button6.place(x=170,y=300,height=70,width=80)

imgsub=PhotoImage(file="sub.png")
button_sub=Button(calframe,image=imgsub,command=subs,justify='center',bg="#f7f9f9",relief='raised')
button_sub.place(x=260,y=300,height=70,width=80)

# ------------------row 1,2,3,div-----------------------------------------

img1=PhotoImage(file="1.png")
button1=Button(calframe,image=img1,command=one,justify='center',bg="#f7f9f9",relief='raised')
button1.place(x=10,y=380,height=70,width=80)

img2=PhotoImage(file="2.png")
button2=Button(calframe,image=img2,command=two,justify='center',bg="#f7f9f9",relief='raised')
button2.place(x=90,y=380,height=70,width=80)

img3=PhotoImage(file="3.png")
button3=Button(calframe,image=img3,command=three,justify='center',bg="#f7f9f9",relief='raised')
button3.place(x=170,y=380,height=70,width=80)

imgdiv=PhotoImage(file="div.png")
button_div=Button(calframe,image=imgdiv,command=divisionn,justify='center',bg="#f7f9f9",relief='raised')
button_div.place(x=260,y=380,height=70,width=80)

# ------------------row .,0,c,=-----------------------------------------

imgdot=PhotoImage(file="dot.png")
button_dot=Button(calframe,image=imgdot,command=dot,justify='center',bg="#f7f9f9",relief='raised')
button_dot.place(x=10,y=460,height=70,width=80)

img0=PhotoImage(file="0.png")
button2=Button(calframe,image=img0,command=zero,justify='center',bg="#f7f9f9",relief='raised')
button2.place(x=90,y=460,height=70,width=80)

imgdel=PhotoImage(file="delt.png")
button_del=Button(calframe,image=imgdel,command=deletee,justify='center',bg="#f7f9f9",relief='raised')
button_del.place(x=170,y=460,height=70,width=80)

imgequal=PhotoImage(file="eqq.png")
button_div=Button(calframe,image=imgequal,command=equall,justify='center',bg="#f7f9f9",relief='raised')
button_div.place(x=260,y=460,height=70,width=80)



# ===============================================menutab starts from here =====================================
def bmical():
    def bkspc():
        bmibtn.pack(side=LEFT,anchor='nw',padx=5,pady=5)
        container.config(bg="#d4e6f1")
        status_frame.pack_forget()
        contentframe.pack_forget()

    def calculate():
        resultarea=LabelFrame(contentframe,text="Result",font=("Bahnschrift",13),height=270,width=322,fg="#8e44ad",
                              bg="#f7f9f9")
        resultarea.place(y=180,x=5)

        try:
            wgt=float(wgtentry.get())
            hgt=float(hgtentry.get())
            wgttyp=whtget.get()
            hgttyp=hgtget.get()
            def calculatorr(wvalue,wtype,hvalue,htype):
                if wtype=="Kilograms":
                    if htype=='Centimeters':
                        hgtc=float(hvalue/100.0)
                        cal=wvalue/(hgtc**2)

                    elif htype=='Meters':
                        cal=wvalue/(hvalue**2)

                    elif htype=='Feet':
                        hgtc=float(hvalue*0.31)
                        cal=wvalue/hgtc**2

                    elif htype=='Inches':
                        hgtc=float(hvalue*0.025)
                        cal=wvalue/hgtc**2

                    else:
                        pass
                
                elif wtype=='Pound':
                    wgtc=wvalue*0.454
                    if htype=='Centimeters':
                        hgtc=float(hvalue/100)
                        cal=wgtc/hgtc**2

                    elif htype=='Meters':
                        cal=wgtc/hvalue**2

                    elif htype=='Feet':
                        hgtc=float(hvalue*0.31)
                        cal=wgtc/hgtc**2

                    elif htype=='Inches':
                        hgtc=float(hvalue*0.025)
                        cal=wgtc/hgtc**2
                        

                    else:
                        pass
                
                else:
                    pass

                return cal
            
            retval=calculatorr(wgt,wgttyp,hgt,hgttyp)
            retval=str(retval)

            splitter=retval.split('.')
            splitter1=splitter[1]
            splitter2=splitter1[0:1]
            show=splitter[0]+"."+splitter2
            resultlbl=Label(contentframe,text=show,font=("Bahnschrift",45,'bold'),fg="#f39c12",bg="#f7f9f9")
            resultlbl.place(x=80,y=200)
            bmilbl=Label(contentframe,text="BMI",font=("Bahnschrift",15,'bold'),bg="#f7f9f9")
            bmilbl.place(x=200,y=217)
            line=Canvas(contentframe,bg="#839192")
            line.place(x=20,y=300,height=7,width=290)
            infolbl=Label(contentframe,text="Information",font=("Bahnschrift",12),bg='#f7f9f9',fg="#839192")
            infolbl.place(x=120,y=310)

            underlbl=Label(contentframe,text="Underweight",font=("Bahnschrift",8),bg='#f7f9f9',fg="#3498db")
            underlbl.place(x=30,y=360)

            normallbl=Label(contentframe,text="Normal",font=("Bahnschrift",8),bg='#f7f9f9',fg="#2ecc71")
            normallbl.place(x=150,y=360)

            overlbl=Label(contentframe,text="Overweight",font=("Bahnschrift",8),bg='#f7f9f9',fg="#DE3163")
            overlbl.place(x=230,y=360)

            line2=Canvas(contentframe,bg="#3498db")
            line2.place(x=30,y=400,height=7,width=90)

            line3=Canvas(contentframe,bg="#2ecc71")
            line3.place(x=110,y=400,height=7,width=130)

            line4=Canvas(contentframe,bg="#DE3163")
            line4.place(x=220,y=400,height=7,width=90)

            underval=Label(contentframe,text="16.0",font=("Bahnschrift",10),bg='#f7f9f9',fg="#839192")
            underval.place(x=20,y=420)

            normalval=Label(contentframe,text="18.5",font=("Bahnschrift",10),bg='#f7f9f9',fg="#839192")
            normalval.place(x=100,y=420)

            overval=Label(contentframe,text="25.0",font=("Bahnschrift",10),bg='#f7f9f9',fg="#839192")
            overval.place(x=210,y=420)

            overval2=Label(contentframe,text="40.0",font=("Bahnschrift",10),bg='#f7f9f9',fg="#839192")
            overval2.place(x=290,y=420)

            retval=float(retval)
            if retval>=16.0 and retval<18.5:
                bmistate=Label(contentframe,text="Underweight",font=("Bahnschrift",10,'bold'),bg="#f7f9f9",fg="#3498db")
                bmistate.place(x=200,y=245)
            elif retval>=18.5 and retval<25.0:
                bmistate=Label(contentframe,text="Normal",font=("Bahnschrift",10,'bold'),bg="#f7f9f9",fg="#2ecc71")
                bmistate.place(x=200,y=245)
            elif retval>=25.0 and retval<=40.0:
                bmistate=Label(contentframe,text="Overweight",font=("Bahnschrift",10,'bold'),bg="#f7f9f9",fg="#DE3163")
                bmistate.place(x=200,y=245)
            else:
                resultlbll=Label(contentframe,text="Enter the valid parameters.",font=("Bahnschrift",15,'bold'),bg="#f7f9f9",fg="#DE3163")
                resultlbll.place(x=40,y=270)
                resultlbl.place_forget()
                underval.place_forget()
                overval.place_forget()
                overval2.place_forget()
                normalval.place_forget()
                line.place_forget()
                line2.place_forget()
                line3.place_forget()
                line4.place_forget()
                overlbl.place_forget()
                normallbl.place_forget()
                overlbl.place_forget()
                underlbl.place_forget()
                infolbl.place_forget()
                bmilbl.place_forget()

        except (ValueError, ZeroDivisionError):
            pass

        
    bmibtn.pack_forget()
    container.config(bg="white")
    status_frame=Frame(container,bg="#8e44ad",height=50,relief='raised',bd=3)
    status_frame.pack(fill=X,padx=5,pady=5)
    # img_pathh="reply.png"
    # img_size=(100,100)
    # bscimg=resize_image(img_pathh,img_size)
    backspacebtn=Button(status_frame,text="<--",font=("Copperplate Gothic Bold",15,"bold"),fg="white",
                        bg="#8e44ad",command=bkspc)
    backspacebtn.place(x=5,y=8)
    heading=Label(status_frame,text="BMI Calculator",font=("Copperplate Gothic Bold",15),fg="white",bg="#8e44ad",height=2)
    heading.pack()

    contentframe=Frame(container,bg="#f7f9f9",relief='sunken',bd=3)
    contentframe.pack(expand=True,fill=BOTH,padx=5,pady=5)

    wgtlbl=Label(contentframe,text="Select Weight",font=("Bahnschrift",10))
    wgtlbl.place(x=10,y=10)

    wgtopt=['Kilograms','Pound']
    hgtopt=['Centimeters','Meters','Feet','Inches']
    whtget=StringVar()
    wgtbox=ttk.Combobox(contentframe,value=wgtopt,textvariable=whtget)
    wgtbox.current(0)
    wgtbox.place(x=10,y=30)

    hgtlbl=Label(contentframe,text="Select Height",font=("Bahnschrift",10))
    hgtlbl.place(x=10,y=55)

    hgtget=StringVar()
    hgtbox=ttk.Combobox(contentframe,value=hgtopt,textvariable=hgtget)  
    hgtbox.current(0)
    hgtbox.place(x=10,y=75)


    wgtentry=Entry(contentframe,font=("Bahnschrift",12,"bold"),relief='sunken',bd=3)
    wgtentry.place(x=160,y=15,height=40,width=160)

    hgtentry=Entry(contentframe,font=("Bahnschrift",12,"bold"),relief='sunken',bd=3)
    hgtentry.place(x=160,y=65,height=40,width=160)

    calbtn=Button(contentframe,text="Go",font=("Bahnschrift",16,"bold"),height=1,width=10,relief='raised',
                  bd=3,bg='#8e44ad',fg="white",command=calculate)
    calbtn.place(x=100,y=130)
   



container=Frame(menuframe,bg="#d4e6f1")
container.pack(expand=True,fill=BOTH)
img_path="bmi.png"
size=(90,80)
img=resize_image(img_path,size)
bmibtn=Button(container,image=img,command=bmical)
bmibtn.pack(side=LEFT,anchor='nw',padx=5,pady=5)

win.mainloop()