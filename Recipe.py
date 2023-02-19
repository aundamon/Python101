from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('สูตรอาหาร')
GUI.geometry('500x500')

L1=Label(GUI,text='สูตรอาหาร',font=('Cordia New',24),fg='red')
L1.place(x=180,y=20)

def Button1():
    text='เนื้ออกไก่,หอมหัวใหญ่,น้ำพริกเผา,น้ำตาลทราย,ซอสปรุงรส,น้ำมันพืช,ใบกระเพรา'
    messagebox.showinfo('วัตถุดิบประกอบด้วย',text)

FB1=Frame(GUI)
FB1.place(x=150,y=80)
B1=ttk.Button(FB1,text='ไก่ผัดพริกเผา',command=Button1)
B1.pack(ipadx=20,ipady=20)

def Button2():
    text='ปลาหมึก,กระเทียม,พริก,เกลือ,นำ้ปลา,ต้นหอม,ผักชี'
    messagebox.showinfo('วัตถุดิบประกอบด้วย',text)

FB2=Frame(GUI)
FB2.place(x=150,y=160)
B2=ttk.Button(FB2,text='ปลาหมึกผัดพริกเกลือ',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text='วุ้นเส้น,หมูสับ,น้ำกระเทียมดอง,มะนาว,นำ้ปลา,พริก,ต้นหอม,ขึ้นฉ่าย,มะเขือเทศ,หอมหัวใหญ่'
    messagebox.showinfo('วัตถุดิบประกอบด้วย',text)

FB3=Frame(GUI)
FB3.place(x=150,y=240)
B3=ttk.Button(FB3,text='ยำวุ้นเส้นหมูสับ',command=Button3)
B3.pack(ipadx=20,ipady=20)

def Button4():
    text='หมูกรอบ,กระเทียม,พริก,ต้นหอม,เกลือ,พริกไทย,นำ้ตาลทราย,ซอสปรุงรส'
    messagebox.showinfo('วัตถุดิบประกอบด้วย',text)

FB4=Frame(GUI)
FB4.place(x=150,y=320)
B4=ttk.Button(FB4,text='หมูกรอบผัดพริกเกลือ',command=Button4)
B4.pack(ipadx=20,ipady=20)

GUI.mainloop()
