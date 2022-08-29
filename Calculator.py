from sqlite3 import Cursor
from textwrap import fill
from tkinter import *
import customtkinter
import tkinter
import sqlite3
from PIL import Image, ImageTk
import math

root=customtkinter.CTk()
db = sqlite3.connect("myDataBase.db")

Result=""
shown=""
ans=""
ansback=""
flag=False
answer=0

def clear():
    global Result
    global ans
    global shown
    global ansback
    global flag
    global answer
    ansback=""
    shown=""
    ans=""
    Result=""
    answer=0
    flag=False
    info_label.config(text='')
    Result_lable.config(text='0')

def Expression(value):
    global Result
    global shown
    global ans
    global flag
    global ansback
    global answer
    if flag==True:
        if shown=="" and value=='0':
            clear()
        elif value=='/' or value=='+' or value=='-' or value=='*' or value=='%' or value=="\\u00F7" or value=="X" or value=="x":
            shown+=ansback
        else:
            shown=""
            Result=""
        flag=False
        # Result+=value
    if shown=="" and value=='0' and ans=="": 
        clear()
    elif value=="\\u00F7":
        shown+=" " +"\u00F7"+" "
        value="/"
        ans=""
        info_label.config(text=shown)
        Result_lable.config(text='')
        Result+=value
    elif value=="x":
        shown+=" " +value+" "
        value="*"
        ans=""
        info_label.config(text=shown)
        Result_lable.config(text='')
        Result+=value
    elif value=="X":
        shown+=" " +value+" "
        value="*"
        ans=""
        info_label.config(text=shown)
        Result_lable.config(text='')
        Result+=value
    elif value=='+' or value=='-':
        shown+=" " +value+" "
        ans=""
        info_label.config(text=shown)
        Result_lable.config(text='')
        Result+=value
    else:
        if value=="0" and shown!="" and ans=="":
            pass
        else:
            if value=="." and shown=="":
                shown+="0."
                ans+="0"+value
                Result_lable.config(text=ans)
                Result+="0"+value
            else:
                shown+=value
                ans+=value
                Result_lable.config(text=ans)
                Result+=value
# 13
yay=0
History_info=""
Here="not"

def calculate():
    global Result
    global shown
    global ans
    global flag
    global ansback
    global answer
    global History_info
    global yay
    global Here
    flag=True
    info_label.config(text=shown+" = ")
    
    if Result !="":
        try:
            answer=eval(Result)
            answer=round(answer,2)
            ansback=str(answer)
            # info_label.config(text=shown+" = ")
        except:
            clear()
            answer="Math Error"
            info_label.config(text='')
        Result=str(answer)
    let=str(answer)
    if len(let) >13:
        Result_lable.config(text=format(answer,".7e"))
    else:
        Result_lable.config(text=answer)
    if Here!="not" and yay==1:
        History_info="\n"+shown+' = ' + '\n\n' + Result  + "\n--------------------------------------------" +'\n\n'
        yay=0
    else: History_info="\n"+shown+' = ' + '\n\n' + Result  + "\n--------------------------------------------" +'\n' + History_info
    History_Label.config(text=History_info,anchor=NE)
    shown=""
    answer=0
def calculate_custom(value):
    global Result
    global ans
    global ansback
    global flag
    global shown
    global Here
    flag=True
    Answer=0
    Here=""
    if Result!="" and Result_lable!="OverFlow":
        try :
            a=0
            for i in reversed(shown):
                if i==' ':
                    break
                a+=1
            a=len(shown)-1-a+1
            shown = shown[0 : a : ]
            if value==1:
                if shown=="": Answer=float(Result)
                else: Answer=float(ans)
                Answer=Answer**3
                Answer=round(Answer,2)
                ans=str(Answer)
            elif value==2:
                if shown=="": Answer=float(Result)
                else: Answer=float(ans)
                Answer=Answer**2
                Answer=round(Answer,2)
                ans=str(Answer)
            else:
                if shown=="": Answer=float(Result)
                else: Answer=float(ans)
                Answer=math.sqrt(Answer)
                Answer=round(Answer,2)
                ans=str(Answer)  
            # shown=""
            # Result+=Here
            if shown=="":
                Result=ans
                shown=Result
            else:
                j=0
                for i in reversed(Result):
                    if i=="*" or i=="+" or i=="-" or i=="/":
                        break
                    j+=1
                j=len(Result)-1-j+1
                Result = Result[0 : j : ]
                Result+=ans
                shown+=ans
            
            if len(Result) >13:
                Result_lable.config(text=format(Answer,".7e"))
            else:
                Result_lable.config(text=Answer)
            ans=""
            ansback=""
        except:
            clear()
            Result_lable.config(text="OverFlow")
    else:
        clear()
        Result_lable.config(text="Error")

def Delete_last():
    global Result
    global ans
    global shown
    global ansback
    global flag
    if flag==True:
        pass
    else:
        ans=ans[:-1]
        shown=shown[:-1]
        Result=Result[:-1]
        Result_lable.config(text=ans)
        flag=False



# History Section
def History_Button():
    global on
    # return
    on=0
    def clicked(value):
        global on
        on+=value
        if on%2==0:
            # Close History Menu
            History_Label.place(x=1001,y=860)
            MyTrash.place(x=1001,y=860)
            pass
        else:
            # Open History Menu
            History_Label.place(x=-1,y=140)
            MyTrash.place(x=-1,y=140)
            pass

    Special_Char="#1e1e1e"

    history_img = ImageTk.PhotoImage(Image.open("C:/Users/MoemenAdam/Desktop/Vs-Code/Python/history-white.png").resize((24,20),Image.Resampling.LANCZOS))

    MyHistory = customtkinter.CTkButton(master=info_label,image=history_img,hover_color="#555555",width=45,height=45,compound="left",text='',fg_color=Special_Char,command=lambda:clicked(1))
    MyHistory.pack(side=LEFT,pady=0)



# Output Section
labelsbg="#1e1e1e"
info_label=Label(root,bg=labelsbg,fg="white",text='',anchor=E,font=("arial",10))
info_label.pack(fill="both")
Result_lable=Label(root,height=2,text='0',fg="white",bg=labelsbg,anchor=E,font=("arial",30,"bold"),pady=16)
Result_lable.pack(fill="both")


# Input Section
def inputSection():
    Numbers_bg="#0E0E0E"
    Numbers_fg="white"
    Special_Char="#191919"
    leavecolor="#3d3d3d"
    border_width_numbers=2
    border_width_specialchar=0
    # Custome Operations    
    #191919
    
    def HoverActivate(button,color1,color2):
        button.configure(bg=color1)
        def on_enter(e):
            button.configure(bg=color2)

        def on_leave(e):
            button.configure(bg=color1)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.config(cursor="hand2")

    Button1=Button(root,text="C",width=5,height=1,font=("arial",20,"bold"),fg=Numbers_fg,bg=Special_Char,bd=border_width_specialchar,command=lambda:clear())
    Button1.place(x=-8,y=140)
    HoverActivate(Button1,Special_Char,leavecolor)

    Button2=Button(root,text="x\u00b3",width=3,height=1,font=("arial",20,"bold"),fg=Numbers_fg,bg=Special_Char,bd=border_width_specialchar,command=lambda:calculate_custom(1))
    Button2.place(x=75,y=140)
    HoverActivate(Button2,Special_Char,leavecolor)

    Button3=Button(root,text="x\u00b2",width=3,height=1,font=("arial",20,"bold"),fg=Numbers_fg,bg=Special_Char,bd=border_width_specialchar,command=lambda:calculate_custom(2))
    Button3.place(x=130,y=140)
    HoverActivate(Button3,Special_Char,leavecolor)


    Delete_img = ImageTk.PhotoImage(Image.open("C:/Users/MoemenAdam/Desktop/Vs-Code/Python/Studio_Project.png").resize((25,25),Image.Resampling.LANCZOS))

    MyDelete = customtkinter.CTkButton(master=root,fg_color=Special_Char,image=Delete_img,hover_color="#555555",width=58,height=54,compound="left",text='',command=lambda:Delete_last())
    MyDelete.place(x=242,y=140)

    Button4=Button(root,text="\u221ax",width=3,height=1,font=("arial",20,"bold"),fg=Numbers_fg,bg=Special_Char,bd=border_width_specialchar,command=lambda:calculate_custom(3))
    Button4.place(x=186,y=140)
    HoverActivate(Button4,Special_Char,leavecolor)

    Button6=Button(root,text="-",width=3,height=1,font=("arial",20,"bold"),fg=Numbers_fg,bg=Special_Char,bd=border_width_specialchar,command=lambda:Expression("-"))
    Button6.place(x=243,y=192)
    HoverActivate(Button6,Special_Char,leavecolor)

    Button7=Button(root,text="+",width=3,height=1,font=("arial",20,"bold"),fg=Numbers_fg,bg=Special_Char,bd=border_width_specialchar,command=lambda:Expression("+"))
    Button7.place(x=243,y=244)
    HoverActivate(Button7,Special_Char,leavecolor)

    Button8=Button(root,text="x",width=3,height=1,font=("arial",20,"bold"),fg=Numbers_fg,bg=Special_Char,bd=border_width_specialchar,command=lambda:Expression("x"))
    Button8.place(x=243,y=296)
    HoverActivate(Button8,Special_Char,leavecolor)

    Button9=Button(root,text="\u00F7",width=3,height=1,font=("arial",20,"bold"),fg=Numbers_fg,bg=Special_Char,bd=border_width_specialchar,command=lambda:Expression("\\u00F7"))
    Button9.place(x=243,y=348)
    HoverActivate(Button9,Special_Char,leavecolor)

    Button10=Button(root,text="=",width=3,height=3,font=("arial",20,"bold"),fg=Numbers_fg,bg="#333333",bd=border_width_specialchar,command=lambda:calculate())
    Button10.place(x=243,y=400)
    HoverActivate(Button10,"#333333",leavecolor)
    
    # Numbers

    Button11=Button(root,text="7",width=5,height=2,font=("arial",20,"bold"),fg=Numbers_fg,bg=Numbers_bg,bd=border_width_numbers,command=lambda:Expression("7"))
    Button11.place(x=-1,y=192)
    HoverActivate(Button11,Numbers_bg,leavecolor)

    Button12=Button(root,text="8",padx=3,width=4,height=2,font=("arial",20,"bold"),fg=Numbers_fg,bg=Numbers_bg,bd=border_width_numbers,command=lambda:Expression("8"))
    Button12.place(x=94-8,y=192)
    HoverActivate(Button12,Numbers_bg,leavecolor)

    Button13=Button(root,text="9",padx=5,width=4,height=2,font=("arial",20,"bold"),fg=Numbers_fg,bg=Numbers_bg,bd=border_width_numbers,command=lambda:Expression("9"))
    Button13.place(x=169-8,y=192)
    HoverActivate(Button13,Numbers_bg,leavecolor)

    Button14=Button(root,text="4",width=5,height=2,font=("arial",20,"bold"),fg=Numbers_fg,bg=Numbers_bg,bd=border_width_numbers,command=lambda:Expression("4"))
    Button14.place(x=-1,y=276)
    HoverActivate(Button14,Numbers_bg,leavecolor)

    Button15=Button(root,text="5",padx=3,width=4,height=2,font=("arial",20,"bold"),fg=Numbers_fg,bg=Numbers_bg,bd=border_width_numbers,command=lambda:Expression("5"))
    Button15.place(x=94-8,y=276)
    HoverActivate(Button15,Numbers_bg,leavecolor)

    Button16=Button(root,text="6",padx=5,width=4,height=2,font=("arial",20,"bold"),fg=Numbers_fg,bg=Numbers_bg,bd=border_width_numbers,command=lambda:Expression("6"))
    Button16.place(x=169-8,y=276)
    HoverActivate(Button16,Numbers_bg,leavecolor)

    Button17=Button(root,text="1",width=5,height=2,font=("arial",20,"bold"),fg=Numbers_fg,bg=Numbers_bg,bd=border_width_numbers,command=lambda:Expression("1"))
    Button17.place(x=-1,y=360)
    HoverActivate(Button17,Numbers_bg,leavecolor)

    Button18=Button(root,text="2",padx=3,width=4,height=2,font=("arial",20,"bold"),fg=Numbers_fg,bg=Numbers_bg,bd=border_width_numbers,command=lambda:Expression("2"))
    Button18.place(x=94-8,y=360)
    HoverActivate(Button18,Numbers_bg,leavecolor)

    Button19=Button(root,text="3",padx=5,width=4,height=2,font=("arial",20,"bold"),fg=Numbers_fg,bg=Numbers_bg,bd=border_width_numbers,command=lambda:Expression("3"))
    Button19.place(x=169-8,y=360)
    HoverActivate(Button19,Numbers_bg,leavecolor)

    Button20=Button(root,text="0",width=10,height=1,font=("arial",20,"bold"),fg=Numbers_fg,bg=Numbers_bg,bd=border_width_numbers,pady=10,command=lambda:Expression("0"))
    Button20.place(x=-1,y=444)
    HoverActivate(Button20,Numbers_bg,leavecolor)

    Button21=Button(root,text=".",padx=5,width=4,height=1,font=("arial",20,"bold"),fg=Numbers_fg,bg=Special_Char,bd=border_width_numbers,pady=10,command=lambda:Expression("."))
    Button21.place(x=169-8,y=444)
    HoverActivate(Button21,Numbers_bg,leavecolor)

    
    
# Set Basics
def Basics():
    global History_Label
    global MyTrash
    global History_info
    global yay
    root.geometry("300x509")
    root.title("Calculator")
    root.iconbitmap("C:/Users/MoemenAdam/Desktop/Vs-Code/Python/calculator.ico")
    
    History_Button()
    inputSection()
    
    def Trash():
        global yay
        if History_info!="":
            History_Label.config(text='\n\n\n\n\n\n\nEmpty\t\t')
            yay=1
        else:
            History_Label.config(text='Empty')
            

    Trash_img = ImageTk.PhotoImage(Image.open("C:/Users/MoemenAdam/Desktop/Vs-Code/Python/trash.png").resize((25,25),Image.Resampling.LANCZOS))

    
    History_Label = Label(root,text='Empty',font=("arial",15),fg="White",justify='right',bg="#2d2d2d",width=27,height=16)
    History_Label.place(x=1001,y=860) 
    MyTrash = customtkinter.CTkButton(master=root,fg_color="#2d2d2d",image=Trash_img,hover_color="#555555",width=58,height=54,compound="left",text='',command=lambda:Trash())
    MyTrash.place(x=1001,y=860)
    

# Main Function
def Main():
    Basics()
    root.mainloop()
    db.close()
Main()