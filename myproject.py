from tkinter import *
import sqlite3
import os
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import messagebox as msg
from scrolling_area import Scrolling_Area, Table
import ttkcalendar
import tkSimpleDialog

class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def body(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection

root=Tk()
root.title('Project')
root.geometry('1920x1080')
frame=Frame(root,width=1920,height=1080)
frame.place(x=0,y=0)

#-------------------------------------MAIN-----------------------------------------------#
def main(root,frame):
    img8=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\edit.jpg'))
    L=Label(frame,image=img8)
    L.place(x=0,y=0) 
    L1=Label(frame,text='ASSIGMENT AND MATERIAL SYSTEM',bg='white',fg='black',font=('courier',20))
    L1.place(x=200,y=50)
    B1=Button(frame,text='Admin',font=('algerian',12,'bold'),bg='white',fg='black',width=12,bd=8,command=lambda:Admin(root,frame))
    B1.place(x=880,y=170)
    B2=Button(frame,text='Faculty',font=('algerian',12,'bold'),bg='white',fg='black',width=12,bd=8,command=lambda:faculty(root,frame))
    B2.place(x=1070,y=170)
    B3=Button(frame,text='student',font=('algerian',12,'bold'),bg='white',fg='black',width=12,bd=8,command=lambda:Student(root,frame))
    B3.place(x=1260,y=170)
    frame.mainloop()
    
def back11(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\edit.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    main(root,frame)

#---------------------------------------FACULTY----------------------------------------------#    

def faculty(root,frame):
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\down2.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    
    def back2(root,frame):
        frame.destroy()
        frame=Frame(root,width=1920,height=1080)
        frame.place(x=0,y=0)
        img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\edit.jpg'))
        L=Label(frame,image=img)
        L.place(x=0,y=0)
        main(root,frame)
        
    B4=Button(frame,text='Register',font=('courier',20,'bold'),bg='pink',fg='black',width=15,bd=10,command=lambda:Faculty_Registration(root,frame))
    B4.place(x=150,y=200)
    B5=Button(frame,text='Login',font=('courier',20,'bold'),bg='pink',fg='black',width=15,bd=10,command=lambda:Login(root,frame))
    B5.place(x=150,y=300)
    B50=Button(frame,text='Back',font=('courier',20,'bold'),bg='pink',fg='black',width=15,bd=10,command=lambda:back2(root,frame))
    B50.place(x=150,y=400)
    frame.mainloop()

#----------------------------------------FACULTY REGISTRATION----------------------------------------#

def Faculty_Registration(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\projectimage.png'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    
    def Back(root,frame):
        frame.destroy()
        faculty(root,frame)
        frame.mainloop()
        
    def data():
        txt1=E1.get()
        txt2=E2.get()
        txt3=E3.get()
        txt4=E4.get()
        txt5=Branch.get()
        txt6=E6.get()
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)

        
        conn=sqlite3.connect('Project.db')
        conn.execute('''Create table if not exists projectdata
                    (Name Text primary key not null,
                     Email text not null,
                     Password text,
                     Address text,
                     Branch text,
                     Mobile_No int(10));''')
        conn.execute("INSERT INTO projectdata(Name,Email,Password,Address,Branch,Mobile_No)VALUES('%s','%s','%s','%s','%s','%d')"%(txt1,txt2,txt3,txt4,txt5,int(txt6)))
        conn.commit()
        conn.close()

    L=Label(frame,text='Faculty Registration',bg='light blue',fg='black',width=50,font=('algerian',40))
    L.place(x=0,y=10)
    
    L1=Label(frame,text='Name',font=('algerian',25,'bold'),borderwidth=4,fg='black',bg='honeydew2',width=15)
    L1.place(x=100,y=150)
    E1=Entry(frame,bd=4,width=4,font=("verdana",13,'bold'))             
    E1.place(x=500,y=150,width=300,height=40)
    
    L2=Label(frame,text='Email ID',font=('algerian',25,'bold'),borderwidth=4,fg='black',bg='honeydew2',width=15)
    L2.place(x=100,y=230)
    E2=Entry(frame,bd=4,width=4,font=("verdana",13,'bold'))
    E2.place(x=500,y=230,width=300,height=40)
    
    L3=Label(frame,text='Password',font=('algerian',25,'bold'),borderwidth=4,fg='black',bg='honeydew2',width=15)
    L3.place(x=100,y=310)
    E3=Entry(frame,bd=4,show='*',width=4,font=("verdana",13,'bold'))
    E3.place(x=500,y=310,width=300,height=40)
    
    L4=Label(frame,text='Address',font=('algerian',25,'bold'),borderwidth=4,fg='black',bg='honeydew2',width=15)
    L4.place(x=100,y=390)
    E4=Entry(frame,bd=4,width=4,font=("verdana",13,'bold'))
    E4.place(x=500,y=390,width=300,height=40)
    
    L5=Label(frame,text='Branch',font=('algerian',25,'bold'),borderwidth=4,fg='black',bg='honeydew2',width=15)
    L5.place(x=100,y=470)
    Branch=StringVar()
    E5=OptionMenu(frame,Branch,'EC','CS','EE','Civil')
    E5.place(x=500,y=470,width=300,height=40)
    
    L6=Label(frame,text='Mobile No.',font=('algerian',25,'bold'),borderwidth=4,fg='black',bg='honeydew2',width=15)
    L6.place(x=100,y=550)
    E6=Entry(frame,bd=4,width=4,font=("verdana",13,'bold'))
    E6.place(x=500,y=550,width=300,height=40)
    
    B=Button(frame,text='Register',font=('algerian',12,'bold'),bg='light blue',fg='black',width=15,command=data,bd=10)
    B.place(x=160,y=650)
    
    B=Button(frame,text='Back',font=('algerian',12,'bold'),bg='light blue',fg='black',width=15,command=lambda: Back(root,frame),bd=10)
    B.place(x=500,y=650)
    frame.mainloop()

#-------------------------------------------FACULTY LOGIN-----------------------------------------#    
def Login(root,frame):
    
    def Back1(root,frame):
            frame.destroy()
            faculty(root,frame)

    def Loginsuccess(root,frame):
        txt00=E7.get()
        txt01=E8.get()
        conn=sqlite3.connect('Project.db')
        cursor=conn.execute('select Email,Password from projectdata')
        for row in cursor:
            print(row)
            if row[0]==txt00 and row[1]==txt01:
                ans=msg.askquestion('Login success','Do you want to proceed')
                conn.commit()
                conn.close()
                if ans=='yes':

                    upload(root,frame)
                else:
                    Login(root,frame)
                return
        else:
            msg.showwarning('Login failed','Invalid user name or password')
            conn.commit()
            conn.close()
            Login(root,frame)
                    
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\down1.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)   
    L=Label(frame,text="Faculty Login",bg='light blue',fg='black',width=65,font=("algerian",30))
    L.place(x=0,y=10)
    
    L7=Label(frame,text='Email ID',font=('algerian',18),fg='black',bg='gray93',bd=12,width=20)
    L7.place(x=550,y=350)
    E7=Entry(frame,bd=5,width=4,font=("verdana",18,"bold"))
    E7.place(x=900,y=350,width=300,height=42)
    
    L8=Label(frame,text='Password',font=('algerian',18),fg='black',bg='gray93',bd=12,width=20)
    L8.place(x=550,y=430)
    E8=Entry(frame,show='*',bd=5,width=4,font=("verdana",18,"bold"))
    E8.place(x=900,y=430,width=300,height=42)
    
    B7=Button(frame,text='SUBMIT',bg='grey',fg='white',font=('arial',12,'bold'),width=20,command=lambda:Loginsuccess(root,frame),bd=15)
    B7.place(x=600,y=600)
    
    B8=Button(frame,text='BACK',bg='grey',fg='white',font=('arial',12,'bold'),width=20,command=lambda:faculty(root,frame),bd=15)
    B8.place(x=900,y=600)
    root.mainloop()
#---------------------------------------------FACULTY UPLOAD-------------------------------------------------------#

def upload(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img2=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\colours.jpg'))
    L=Label(frame,image=img2)
    L.place(x=0,y=0)
    
    B9=Button(frame,text='Upload Question',font=('courier',12,'bold'),bg='grey',fg='white',width=25,bd=15,command=lambda:upload_question(root,frame))
    B9.place(x=350,y=150)
    
    B10=Button(frame,text='Upload Material',font=('courier',12,'bold'),bg='grey',fg='white',width=25,bd=15,command=lambda:Upload_Material(root,frame))
    B10.place(x=450,y=250)
    
    B11=Button(frame,text='View Answer',font=('courier',12,'bold'),bg='grey',fg='white',width=25,bd=15,command=lambda:View_Answer(root,frame))
    B11.place(x=550,y=350)
    
    B12=Button(frame,text='Logout',font=('courier',12,'bold'),bg='grey',fg='white',width=25,bd=15,command=lambda:faculty_Logout(root,frame))
    B12.place(x=650,y=450)    
    root.mainloop()
    
def faculty_Logout(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\edit.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    main(root,frame)   
#-----------------------------------------UPLOAD QUESTION--------------------------------------------------------#    

def upload_question(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img2=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\394751.jpg'))
    L=Label(frame,image=img2)
    L.place(x=0,y=0)

    def getdate(frame):
        cd = CalendarDialog(frame)
        result = cd.result
        selected_date.set(result.strftime("%d-%m-%Y"))
        print(E04.get())

    def select_file():
        global picture_file
        picture_file = filedialog.askopenfilename()
        
        #insert_picture(picture_file)
        #insert_picture(conn, picture_file)
        #conn.close()
    
    def insert_picture():
        global picture_file
        conn = sqlite3.connect('faculty_upload.db')
        txt1=E13.get()
        txt2=Branch.get()
        txt3=E15.get()
        txt4=E04.get()
        txt5=E05.get()
        print(txt1)
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        with open(picture_file, 'rb') as input_file:
            ablob = input_file.read()
            base=os.path.basename(picture_file)
            afile, ext = os.path.splitext(base)
            conn.execute('''Create table if not exists upload_ques
                        (Unit_Name Text primary key not null,
                         Branch text,
                         Year text,
                         Date text,
                         Faculty_name text,
                         PICTURE Blob,
                         TYPE Text,
                         FILE_NAME Text);''')
            conn.execute('''INSERT INTO upload_ques values(?, ?, ?, ?, ?, ?, ?, ?)''',[txt1,txt2,txt3,txt4,txt5,sqlite3.Binary(ablob), ext, afile])
        msg.showinfo('sucessfully updated')     
        conn.commit()

   
    '''def show_img(root,frame,var1):
            frame.destroy()
            frame1=Frame(root, width=2000,height=1000)
            frame1.place(x=0,y=0)
            conn = create_or_open_db('picture_db.db')
            cur = conn.cursor()
            filename = extract_picture(cur,var1)
            print(filename)
            cur.close()
            conn.close()
            
            img=ImageTk.PhotoImage(Image.open(filename))
            #img = PhotoImage(file=filename)
            L1=Label(frame1,image=img)
            L1.place(x=900,y=170)
            #L1.pack()
            frame1.mainloop()'''     
        
        
    L=Label(frame,text='Upload Questions',bg='white',fg='red',width=50,font=('algerian',40))
    L.place(x=0,y=10)
    
    L13=Label(frame,text=' Unit Name',font=('algerian',25,'bold'),borderwidth=3,width=15)
    L13.place(x=100,y=100)
    E13=Entry(frame,bd=5,width=4,font=("verdana",15,"bold"))             
    E13.place(x=500,y=100,width=300,height=40)
    
    L14=Label(frame,text='Branch',font=('algerian',25,'bold'),borderwidth=3,width=15)
    L14.place(x=100,y=180)
    Branch=StringVar()
    E14=OptionMenu(frame,Branch,'EC','CS','EE','Civil')
    E14.place(x=500,y=180,width=300,height=40)
    
    L15=Label(frame,text='Year',font=('algerian',25,'bold'),borderwidth=3,width=15)
    L15.place(x=100,y=260)
    E15=Entry(frame,bd=5,width=4,font=("verdana",15,"bold"))
    E15.place(x=500,y=260,width=300,height=40)

    L17=Label(frame,text='Date',font=('algerian',25,'bold'),borderwidth=3,width=15)
    L17.place(x=100,y=340)
    selected_date=StringVar()
    date=StringVar()
    E04=Entry(frame,textvariable=selected_date,bd=5,width=4,font=("verdana",15,"bold"))
    E04.place(x=500,y=340,width=300,height=40)
    b1=Button(frame,text='select date',font=('arial',10,'bold'),bg='white',fg='black',width=8,bd=6,command=lambda:getdate(frame))
    b1.place(x=805,y=340)
    

    L18=Label(frame,text='Faculty Name',font=('algerian',25,'bold'),borderwidth=3,width=15)
    L18.place(x=100,y=420)
    E05=Entry(frame,bd=5,width=4,font=("verdana",15,"bold"))
    E05.place(x=500,y=420,width=300,height=40)
    
    L16=Label(frame,text='Select Question',font=('algerian',25,'bold'),borderwidth=3,width=15)
    L16.place(x=100,y=500)
    def file_search(root,frame):
        filepath=filedialog.askopenfilename()
        return filepath
    
    b67=Button(frame,text='select file',font=('arial',12,'bold'),bg='white',fg='black',width=18,bd=15,command=lambda:select_file())
    b67.place(x=500,y=500)
    B13=Button(frame,text='Upload',font=('arial',12,'bold'),bg='brown',fg='black',width=15,command=lambda:insert_picture(),bd=15)
    B13.place(x=200,y=650)
    B14=Button(frame,text='Back',font=('arial',12,'bold'),bg='brown',fg='black',width=15,command=lambda:upload(root,frame),bd=15)
    B14.place(x=500,y=650)
    root.mainloop()
    

def Upload_Material(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img2=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\books.jpg'))
    L=Label(frame,image=img2)
    L.place(x=0,y=0)

    def data21():
        txt17=E17.get()
        txt18=E18.get()
        txt19=E19.get()
        print(txt17)
        print(txt18)
        print(txt19)

    L=Label(frame,text='Upload Material',bg='white',fg='red',width=15,font=('arial',40))
    L.place(x=500,y=50)
    
    L17=Label(frame,text='Material Name',font=('bold',15))
    L17.place(x=200,y=350)
    E17=Entry(frame,bd=5,font=5)             
    E17.place(x=400,y=350,width=200,height=30)
    
    L18=Label(frame,text='Description',font=('bold',15))
    L18.place(x=200,y=400)
    E18=Entry(frame,bd=5,font=8)
    E18.place(x=400,y=400,width=200,height=30)
    
    L19=Label(frame,text='Select Material',font=('bold',15))
    L19.place(x=200,y=450)
    E19=Entry(frame,bd=5,font=5)
    E19.place(x=400,y=450,width=200,height=30)

    B15=Button(frame,text='Upload',font=('arial',10,'bold'),bg='red',fg='black',width=10,command=data21,bd=10)
    B15.place(x=200,y=600)
    B16=Button(frame,text='Back',font=('arial',10,'bold'),bg='red',fg='black',width=10,command=lambda:upload(root,frame),bd=10)
    B16.place(x=450,y=600)
    root.mainloop()
    
def View_Answer(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img2=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\books.jpg'))
    L=Label(frame,image=img2)
    L.place(x=0,y=0)
    
    B05=Button(frame,text='Back',font=('arial',10,'bold'),bg='brown',fg='black',width=10,command=lambda:upload(root,frame),bd=10)
    B05.place(x=450,y=700)
    frame.mainloop()
    
#-----------------------------------------STUDENT--------------------------------------------------#        

def Student(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\login.png'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    
    B17=Button(frame,text='Register',font=('courier',20,'bold'),bg='white',fg='black',width=15,bd=12,command=lambda:Student_registration(root,frame))
    B17.place(x=400,y=270)
    
    B18=Button(frame,text='Login',font=('courier',20,'bold'),bg='white',fg='black',width=15,bd=12,command=lambda:Login1(root,frame))
    B18.place(x=400,y=370)
    
    B18=Button(frame,text='Back',font=('courier',20,'bold'),bg='white',fg='black',width=15,bd=12,command=lambda:main(root,frame))
    B18.place(x=400,y=470)
    root.mainloop()
#-------------------------------------------STUDENT REGISTRATION---------------------------------------------#    

def Student_registration(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\124499.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    
    def Back4(root,frame):
        frame.destroy()
        Student(root,frame)
        
    def datas():
        txt7=E7.get()
        txt8=E8.get()
        txt9=E9.get()
        txt10=E10.get()
        txt11=Branch.get()
        txt44=E44.get()
        txt12=E12.get()
        print(txt7)
        print(txt8)
        print(txt9)
        print(txt10)
        print(txt11)
        print(txt44)
        print(txt12)

        conn=sqlite3.connect('MyProject.db')
        conn.execute('''Create table if not exists projectdatas
                    (Name Text primary key not null,
                     Email text not null,
                     Password text,
                     Address text,
                     Branch text,
                     year int,
                     Mobile_No int(10));''')
        conn.execute("INSERT INTO projectdatas(Name,Email,Password,Address,Branch,Year,Mobile_No)VALUES('%s','%s','%s','%s','%s','%d','%d')"%(txt7,txt8,txt9,txt10,txt11,int(txt44),int(txt12)))
        conn.commit()
        conn.close()
        
    L=Label(frame,text='Student Registration',bg='light blue',fg='red',width=50,font=('algerian',40))
    L.place(x=0,y=10)
    
    L7=Label(frame,text='Name',font=('algerian',20),fg='black',bg='gray93',bd=12,width=20)
    L7.place(x=100,y=200)
    E7=Entry(frame,bd=4,width=4,font=("verdana",15,"bold"))             
    E7.place(x=500,y=200,width=300,height=40)
    
    L8=Label(frame,text='Email',font=('algerian',20),fg='black',bg='gray93',bd=12,width=20)
    L8.place(x=100,y=280)
    E8=Entry(frame,bd=4,width=4,font=("verdana",15,"bold"))
    E8.place(x=500,y=280,width=300,height=40)
    
    L9=Label(frame,text='Password',font=('algerian',20),fg='black',bg='gray93',bd=12,width=20)
    L9.place(x=100,y=360)
    E9=Entry(frame,bd=4,show='*',width=4,font=("verdana",15,"bold"))
    E9.place(x=500,y=360,width=300,height=40)
    
    L10=Label(frame,text='Address',font=('algerian',20),fg='black',bg='gray93',bd=12,width=20)
    L10.place(x=100,y=440)
    E10=Entry(frame,bd=4,width=4,font=("verdana",15,"bold"))
    E10.place(x=500,y=440,width=300,height=40)

    L11=Label(frame,text='Branch',font=('algerian',20),fg='black',bg='gray93',bd=12,width=20)
    L11.place(x=100,y=520)
    Branch=StringVar()
    E11=OptionMenu(frame,Branch,'EC','CS','EE','Civil')
    E11.place(x=500,y=520,width=300,height=40)

    L44=Label(frame,text='Year',font=('algerian',20),fg='black',bg='gray93',bd=12,width=20)
    L44.place(x=100,y=600)
    E44=Entry(frame,bd=4,width=4,font=("verdana",15,"bold"))
    E44.place(x=500,y=600,width=300,height=40)
    
    L12=Label(frame,text='Mobile number',font=('algerian',20),fg='black',bg='gray93',bd=12,width=20)
    L12.place(x=100,y=680)
    E12=Entry(frame,bd=4,width=4,font=("verdana",15,"bold"))
    E12.place(x=500,y=680,width=300,height=40)
    
    B19=Button(frame,text='Register',font=("verdana",12,'bold'),bg='light blue',fg='black',width=12,bd=15,command=datas)
    B19.place(x=1350,y=600)
    B20=Button(frame,text='Back',font=('verdana',12,'bold'),bg='light blue',fg='black',width=12,bd=15,command=lambda:Back4(root,frame))
    B20.place(x=1350,y=700)
    root.mainloop()
    
#---------------------------------------------STUDENT LOGIN---------------------------------------------------#
def Login1(root,frame):
    
    def Back2(root,frame):
            frame.destroy()
            Student(root,frame)

    def Loginsuccess1(root,frame):
        txt00=E7.get()
        txt01=E8.get()
        conn=sqlite3.connect('MyProject.db')
        cursor=conn.execute('select Email,Password from projectdatas')
        for row in cursor:
            print(row)
            if row[0]==txt00 and row[1]==txt01:
                    ans=msg.askquestion('Login success','Do you want to proceed')
                    conn.commit()
                    conn.close()
                    if ans=='yes':
                        student_upload(root,frame)
                    else:
                        Login1(root,frame)
                    return
        else:
            msg.showwarning('Login failed','Invalid user name or password')
            conn.commit()
            conn.close()
            Login1(root,frame)
                    
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\down5.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)   
    L=Label(frame,text="Student Login",bg='white',fg='black',width=65,font=("algerian",30))
    L.place(x=0,y=10)
    
    L7=Label(frame,text='Email ID',font=('algerian',20),fg='black',bg='gray93',bd=12,width=20)
    L7.place(x=100,y=150)
    E7=Entry(frame,bd=5,width=4,font=("verdana",18,"bold"))
    E7.place(x=550,y=150,width=350,height=42)
    
    L8=Label(frame,text='Password',font=('algerian',20),fg='black',bg='gray93',bd=12,width=20)
    L8.place(x=100,y=250)
    E8=Entry(frame,show='*',bd=5,width=4,font=("verdana",18,"bold"))
    E8.place(x=550,y=250,width=350,height=42)
    
    B5=Button(frame,text='SUBMIT',bg='grey',fg='white',font=('arial',15,'bold'),width=18,command=lambda:Loginsuccess1(root,frame),bd=10)
    B5.place(x=200,y=400)
    
    B6=Button(frame,text='BACK',bg='grey',fg='white',font=('arial',15,'bold'),width=18,command=lambda:Back2(root,frame),bd=10)
    B6.place(x=600,y=400)
    frame.mainloop()
#----------------------------------------------------STUDENT UPLOAD----------------------------------------------#    
def student_upload(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img2=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\old-books.jpg'))
    L=Label(frame,image=img2)
    L.place(x=0,y=0)
    '''conn=sqlite3.connect('faculty_upload.db')
    cursor=conn.execute('select PICTURE,TYPE,FILE_NAME')'''
    B9=Button(frame,text='view Question',font=('courier',12,'bold'),bg='brown',fg='white',width=25,bd=12,command=lambda:view_question(root,frame))
    B9.place(x=70,y=100)
    
    B10=Button(frame,text='Upload Answer',font=('courier',12,'bold'),bg='brown',fg='white',width=25,bd=12,command=lambda:upload_answer(root,frame))
    B10.place(x=70,y=200)
    
    B11=Button(frame,text='Logout',font=('courier',12,'bold'),bg='brown',fg='white',width=25,bd=12,command=lambda:student_logout(root,frame))
    B11.place(x=70,y=300)    
    root.mainloop()
#--------------------------------------------------VIEW QUESTION-------------------------------------------#
def extract_picture(cursor):
   from datetime import datetime as dt
   now=dt.now()
   x1=now.strftime('%d-%m-%Y')
   sql = ("SELECT Faculty_name,PICTURE,TYPE,FILE_NAME FROM 'upload_ques' where Date ='%s'"%x1)
   #param = {'ID': picture_id}
   x=cursor.execute(sql)
   fac_name,ablob, ext, afile = x.fetchone()
   filename = afile + ext
   print('her1')
   print(filename)
   with open(filename, 'wb') as output_file:
      output_file.write(ablob)
   return filename

def show_image(frame,root):
        conn=sqlite3.connect('faculty_upload.db')
        file=extract_picture(conn)
        frame1=Frame(root,width=100,height=100)
        frame1.place(x=100,y=100)
        img=ImageTK.PhotoImage(Image.open(file))
        lb=Label(frame,image=img)
        lb.image=img
        lb.place(x=100,y=100)
        conn.commit()

        
def view_question(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img2=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\books.jpg'))
    L=Label(frame,image=img2)
    L.place(x=0,y=0)
    L=Label(frame,text='View Question',bg='white',fg='red',width=15,font=('arial',40))
    L.place(x=500,y=50)
    #show_img(frame,root)
    B04=Button(frame,text='Back',font=('arial',10,'bold'),bg='brown',fg='black',width=10,command=lambda:student_upload(root,frame),bd=10)
    B04.place(x=450,y=700)
    show_image(cursor)
    frame.mainloop()
    
#----------------------------------------------------UPLOAD ANSWERS--------------------------------------------#    
def upload_answer(root,frame):
    
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img2=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\down2.jpg'))
    L=Label(frame,image=img2)
    L.place(x=0,y=0)
    conn=sqlite3.connect('Myproject.db')
    conn.execute('''Create table if not exists upload_answers1
                    (Unit_Name TEXT primary key not null,
                     Branch TEXT,
                     Year int,
                     Faculty_name TEXT,
                     Student_name TEXT,
                     answer TEXT);''')

    def data2():
        txt33=E33.get()
        txt55=Branch.get()
        txt66=E66.get()
        txt77=E77.get()
        txt88=E88.get()
        
        print(txt33)
        print(txt55)
        print(txt66)
        print(txt77)
        print(txt88)
        txt7=T7.get('1.0','end')
        print(txt7)

        conn=sqlite3.connect('student_upload.db')
        conn.execute("INSERT INTO upload_answers1(Unit_Name,Branch,Year,Faculty_name,Student_name,answer)VALUES('%s','%s','%d','%s','%s','%s')"%(txt33,txt55,int(txt66),txt77,txt88,txt7))
        conn.commit()
        conn.close()
        
    L=Label(frame,text='Upload Answers',bg='white',fg='red',width=50,font=('algerian',40))
    L.place(x=0,y=15)
    
    L33=Label(frame,text=' Unit Name',font=('algerian',25,'bold'),borderwidth=3,width=15)
    L33.place(x=80,y=100)
    E33=Entry(frame,bd=5,width=4,font=("verdana",13,'bold'))             
    E33.place(x=500,y=100,width=250,height=40)
    
    L55=Label(frame,text='Branch',font=('algerian',25,'bold'),borderwidth=3,width=15)
    L55.place(x=80,y=180)
    Branch=StringVar()
    E55=OptionMenu(frame,Branch,'EC','CS','EE','Civil')
    E55.place(x=500,y=180,width=250,height=40)
    
    L66=Label(frame,text='Year',font=('algerian',25,'bold'),borderwidth=4,width=15)
    L66.place(x=80,y=260)
    E66=Entry(frame,bd=5,width=4,font=("verdana",13,'bold'))
    E66.place(x=500,y=260,width=250,height=40)

    L77=Label(frame,text='Faculty name',font=('algerian',25,'bold'),borderwidth=4,width=15)
    L77.place(x=80,y=340)
    E77=Entry(frame,bd=5,width=4,font=("verdana",13,'bold'))
    E77.place(x=500,y=340,width=250,height=40)

    L88=Label(frame,text='Student name',font=('algerian',25,'bold'),borderwidth=4,width=15)
    L88.place(x=80,y=420)
    E88=Entry(frame,bd=5,width=4,font=("verdana",13,'bold'))
    E88.place(x=500,y=420,width=250,height=40)
    
    L1=Label(frame,text='Answer',font=('algerian',25,'bold'),borderwidth=4,width=15)
    L1.place(x=80,y=500)
    T7=Text(frame,height=10,width=50,bg='white',bd=5)
    T7.place(x=500,y=500)
    
    B13=Button(frame,text='Upload',font=('arial',15,'bold'),bg='brown',fg='black',width=12,command=data2,bd=10)
    B13.place(x=200,y=700)
    B14=Button(frame,text='Back',font=('arial',15,'bold'),bg='brown',fg='black',width=12,command=lambda:student_upload(root,frame),bd=10)
    B14.place(x=500,y=700)
    frame.mainloop()

def student_logout(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\edit.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    main(root,frame)
    
#--------------------------------------------ADMIN---------------------------------------------------------#

def Admin(root,frame):
    def admin_login(root,frame):
        Login=E20.get()
        Password=E21.get()
        a='priyanshi'
        b='priyanshi'

        if(Login==a and Password==b):
            msg.showwarning('info','correct login')
            view(root,frame)
        else:
            msg.showwarning('info','invalid login')
            Admin(root,frame)      
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\lapy.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    
    B21=Button(frame,text='Login',font=("verdana",12,'bold'),bg='grey',fg='white',width=12,bd=15,command=lambda:admin_login(root,frame))
    B21.place(x=120,y=380)
    
    B22=Button(frame,text='Back',font=('verdana',12,'bold'),bg='grey',fg='white',width=12,bd=15,command=lambda:back11(root,frame))
    B22.place(x=420,y=380)
    
    L20=Label(frame,text='Email ID',font=("algerian",20,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=15)
    L20.place(x=80,y=200)
    E20=Entry(frame,bd=4,width=4,font=("verdana",13,'bold'),bg='white',fg='black')
    E20.place(x=400,y=200,width=250,height=35)
    
    L21=Label(frame,text='Password',font=("algerian",20,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=15)
    L21.place(x=80,y=300)
    E21=Entry(frame,show='*',bd=4,font=("verdana",13,'bold'),bg='white',fg='black')
    E21.place(x=400,y=300,width=250,height=35)
    frame.mainloop()

def view(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\wp2036900.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    B21=Button(frame,text='Faculty details',font=('courier',15,'bold'),bg='pink',fg='black',width=20,bd=15,command=lambda:view_faculty(root,frame))
    B21.place(x=100,y=100)
    
    B22=Button(frame,text='Student details',font=('courier',15,'bold'),bg='pink',fg='black',width=20,bd=15,command=lambda:view_student(root,frame))
    B22.place(x=100,y=200)

    B23=Button(frame,text='Back',font=('courier',15,'bold'),bg='pink',fg='black',width=20,bd=15,command=lambda:back01(root,frame))
    B23.place(x=100,y=300)
    frame.mainloop()

def back01(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\Priyanshi\\Desktop\\gui images\\edit.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    main(root,frame)
    
def view_faculty(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080,background='pink')
    frame.place(x=0,y=0)
    conn=sqlite3.connect('Project.db')
    cursor=conn.execute('select * from projectdata')
    scrolling_area = Scrolling_Area(frame, height=700)
    scrolling_area.place(x=0,y=10)
    
    table = Table(scrolling_area.innerframe,
                  ["Name","Email","Password","Address","Branch","Mobile_No"],
                  column_minwidths=[250,250,250,250,240,250],height=900)
    table.pack(expand=True, fill=X)

    table.on_change_data(scrolling_area.update_viewport)
  
    conn = sqlite3.connect("Project.db")
    cur = conn.cursor()
    cur.execute("SELECT * from projectdata")

    data=[]
    for row in cur:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)
          
    conn.commit()
    
    B02=Button(frame,text='Back',font=('courier',12,'bold'),bg='grey',fg='white',width=15,bd=15,command=lambda:view(root,frame))
    B02.place(x=720,y=660)
    conn.close()

def view_student(root,frame):
    frame.destroy()
    frame=Frame(root,width=1920,height=1080,background='light green')
    frame.place(x=0,y=0)
    conn=sqlite3.connect('MyProject.db')
    cursor=conn.execute('select * from projectdatas')
    scrolling_area = Scrolling_Area(frame, height=700)
    scrolling_area.place(x=0,y=10)
    
    table = Table(scrolling_area.innerframe,
                  ["Name","Email","Password","Address","Branch","Year","Mobile_No"],
                  column_minwidths=[220,230,220,230,190,180,220],height=900)
    table.pack(expand=True, fill=X)

    table.on_change_data(scrolling_area.update_viewport)
  
    conn = sqlite3.connect("MyProject.db")
    cur = conn.cursor()
    cur.execute("SELECT * from projectdatas")

    data=[]
    for row in cur:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)  
    conn.commit()
    
    B03=Button(frame,text='Back',font=('courier',12,'bold'),bg='grey',fg='white',width=15,bd=15,command=lambda:view(root,frame))
    B03.place(x=720,y=660)
    conn.close()
    
    
main(root,frame)
root.mainloop()
