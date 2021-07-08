from tkinter import *
import tkinter as tk
from tkinter import messagebox
import PIL
from PIL import ImageTk as itk
from PIL import Image
import mysql.connector
mysql=mysql.connector.connect(host="localhost",user="Naveenvisal",passwd="2404",database="pdbms")
myc=mysql.cursor()
flag1=0
flag2=0
flag3=0
flag4=0
flg=0
cname1="h"
'''from tkinter import PhotoImage
from tkinter import Frame,Label,Button'''
'''window = tk.Tk() 
labelFrame=tk.Tk()
same=True
n=1
def Employee():
        window.destroy()
        Button(labelFrame, text="naveen sve",bg='black',fg='white').place(relx=0.07,rely=0.25)
        
def Student():
        window.destroy()

       Label(labelFrame, text="shokan",bg='black',fg='white').place(relx=0.07,rely=0.25)'''
def home():
        window = tk.Tk()
        global flag1
        flag1=1
        same=True
        n=1
        def Login():
                global flag1
                if flag1==1 and flag1!=0:
                        window.destroy()
                        flag1=flag1+1
                        
                n=5
                lab=tk.Tk()
                global flag2
                flag2=1
                cname=StringVar()
                pwd=StringVar()
                def enter():
                         global cname1
                         cname1=str(cname.get())
                         pwd1=str(pwd.get())
                         myc.execute("select username from users")
                         p=[]
                         for i in myc:
                                p.append(i[0])
                         myc.execute("select password from users")
                         k=[]
                         for i in myc:
                                 k.append(i[0])
                         if cname1 in p:
                                if pwd1 in k:
                                        global flag2
                                        if flag2==1 and flag2!=0:
                                                lab.destroy()
                                                flag2=flag2+1
                                        ent=tk.Tk()
                                        global flag3
                                        flag3=1
                                        def search():
                                                global flag3
                                                if flag3==1 and flag3!=0:
                                                        ent.destroy()
                                                        flag3=flag3+1
                                                sch=tk.Tk()
                                                addr=StringVar()
                                                def search1():
                                                        adr1=str(addr.get())
                                                        ldis=tk.Tk()
                                                        l=["Landno","Area","Location","Value"]
                                                        for i in range(0,len(l)):
                                                                k=i+1
                                                                p=Label(ldis,text=l[i],font="arial 18 bold")
                                                                p.grid(padx=40,pady=20,column=k,row=0)
                                                        myc.execute("select landno,larea,lloc,lamount from bland where lloc = %s",(adr1,))
                                                        c=1
                                                        for i in myc:
                                                                for j in range(len(l)):
                                                                        k=j+1
                                                                        btn_column = Label(ldis, text=i[j],font="arial 14")
                                                                        btn_column.grid(padx=40,pady=20,column=k,row=c)
                                                                c=c+1
                                                        ldis.mainloop()
                                                def back1():
                                                        sch.destroy()
                                                        enter()
                                                n=5
                                                background_image =Image.open("db1.jpg")
                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                if same:
                                                        newImageSizeHeight = int(imageSizeHeight*n) 
                                                else:
                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                img = itk.PhotoImage(background_image)
                                                Canvas2 = tk.Canvas(sch)
                                                Canvas2.create_image(780,340,image=img)      
                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                Label(sch,text="Search ",relief="solid",width=40,font="arial 19 bold").place(x=80,y=90)
                                                Label(sch,text="Enter address :",bg="light green",font="arial 14 bold").place(x=80,y=180)
                                                Entry(sch,textvar=addr,width=20,font="arial 13").place(x=240,y=182)
                                                Button(sch,text="search",bg='blue',font="arial 12 bold", fg='black',command=search1).place(x=150,y=240)
                                                Button(sch,text="back",bg='blue',font="arial 12 bold", fg='black',command=back1).place(x=230,y=240)
                                                sch.mainloop()
                                                
                                        def buy():
                                                global flag3
                                                if flag3==1 and flag3!=0:
                                                        ent.destroy()
                                                        flag3=flag3+1
                                                bland=tk.Tk()
                                                global flag4
                                                flag4=1
                                                lno=StringVar()
                                                def buy1():
                                                        lno1=int(lno.get())
                                                        myc.execute("select landno from bland")
                                                        q=[]
                                                        for i in myc:
                                                                q.append(i[0])
                                                        if lno1 in q:
                                                                global flag4
                                                                if flag4==1 and flag4!=0:
                                                                        bland.destroy()
                                                                        flag4=flag4+1
                                                                buyt=tk.Tk()
                                                                lam=StringVar()
                                                                pmd=StringVar()
                                                                def buy2():
                                                                        lam1=str(lam.get())
                                                                        lamt1=float(lam1)
                                                                        pmthd1=str(pmd.get())
                                                                        myc.execute("select lamount from bland where landno=%s",(lno1,))
                                                                        for i in myc:
                                                                                amount=i[0]
                                                                                if lamt1>amount or lamt1==amount:
                                                                                        global cname1
                                                                                        myc.execute("select custid from customers where cname=%s",(cname1,))
                                                                                        for i in myc:
                                                                                                cid=i[0]
                                                                                        myc.execute("select landno,larea,lloc,lamount from bland where landno = %s",(lno1,))
                                                                                        for i in myc:
                                                                                                sql="insert into cland values(%s,%s,%s,%s,%s)"
                                                                                                val=(cid,lno1,i[1],i[2],lamt1)
                                                                                                myc.execute(sql,val)
                                                                                        myc.execute("delete from bland where landno=%s",(lno1,))
                                                                                        mysql.commit()
                                                                                        tk.messagebox.showinfo("WELCOME","You Buyed Land Successfully")
                                                                                        buyt.destroy()
                                                                                        enter()       
                                                                                                
                                                                                else:
                                                                                        tk.messagebox.showinfo("SORRY","Invalid amount")
                                                                                        buyt.destroy()
                                                                                        buy1()
                                                                def back3():
                                                                        buyt.destroy()
                                                                        buy()
                                                                n=5
                                                                background_image =Image.open("db1.jpg")
                                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                                if same:
                                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                                else:
                                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                                img = itk.PhotoImage(background_image)
                                                                Canvas2 = tk.Canvas(buyt)
                                                                Canvas2.create_image(780,340,image=img)      
                                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                                Label(buyt,text="BUY LAND %s"%(lno1),relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                                Label(buyt,text="%-20s%-20s%-20s%-20s"%("Landno","Area","Location","Amount"),font="arial 14 bold").place(x=80,y=220)

                                                                myc.execute("select landno,larea,lloc,lamount from bland where landno = %s",(lno1,))
                                                                for i in myc:
                                                                        Label(buyt,text="%-35s%-35s%-25s%-25s"%(i[0],i[1],i[2],i[3]),font="arial 12").place(x=80,y=250)   

                                                                Label(buyt,text="Enter amount :",bg="light green",font="arial 14 bold").place(x=80,y=320)
                                                                Entry(buyt,textvar=lam,width=20,font="arial 13").place(x=240,y=322)
                                                                Label(buyt,text="Enter pmethod :",bg="light green",font="arial 14 bold").place(x=80,y=360)
                                                                Entry(buyt,textvar=pmd,width=20,font="arial 13").place(x=240,y=362)
                                                                Button(buyt,text="buy",bg='blue',font="arial 12 bold", fg='black',command=buy2).place(x=150,y=400)
                                                                Button(buyt,text="back",bg='blue',font="arial 12 bold", fg='black',command=back3).place(x=230,y=400)
                                                                buyt.mainloop() 
                                                        
                                                        else:
                                                                tk.messagebox.showinfo("Sorry","Invalid Landno!!!")
                                                                bland.destroy()
                                                                buy()
                                                def back2():
                                                        bland.destroy()
                                                        enter()
                                                n=5
                                                background_image =Image.open("db1.jpg")
                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                if same:
                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                else:
                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                img = itk.PhotoImage(background_image)
                                                Canvas2 = tk.Canvas(bland)
                                                Canvas2.create_image(780,340,image=img)      
                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                Label(bland,text="BUY LAND",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                Label(bland,text="Enter landno :",bg="light green",font="arial 14 bold").place(x=80,y=220)
                                                Entry(bland,textvar=lno,width=20,font="arial 13").place(x=240,y=222)
                                                Button(bland,text="Buy",bg='blue',font="arial 12 bold", fg='black',command=buy1).place(x=150,y=280)
                                                Button(bland,text="back",bg='blue',font="arial 12 bold", fg='black',command=back2).place(x=230,y=280)
                                                bland.mainloop()
                                                
                                        def sell():
                                                global flag3
                                                if flag3==1 and flag3!=0:
                                                        ent.destroy()
                                                        flag3=flag3+1
                                                sel=tk.Tk()
                                                global flg
                                                flg=1
                                                lno=StringVar()
                                                loc=StringVar()
                                                ar=StringVar()
                                                amt=StringVar()
                                                def sell2():
                                                        global flg
                                                        myc.execute("select landno from bland")
                                                        li=[]
                                                        for i in myc:
                                                                li.append(i[0])
                                                        lno1=int(lno.get())
                                                        loc1=str(loc.get())
                                                        ar1=float(ar.get())
                                                        amt1=float(amt.get())
                                                        if lno1 in li:
                                                                tk.messagebox.showinfo("Sorry","Landno Already exists!!!")
                                                                sel.destroy()
                                                                sell()
                                                        else:
                                                                sel.destroy()
                                                                sel2=tk.Tk()
                                                                doc=StringVar()
                                                                pay=StringVar()
                                                                def reg():
                                                                        global cname1
                                                                        myc.execute("select custid from customers where cname=%s",(cname1,))
                                                                        for i in myc:
                                                                                cid=i[0]
                                                                        
                                                                        amt2=amt1+amt1*0.1
                                                                        sql="insert into bland values(%s,%s,%s,%s,%s,%s)"
                                                                        val=(lno1,ar1,loc1,amt1,cid,amt2)
                                                                        myc.execute(sql,val)
                                                                        doc1=str(doc.get())
                                                                        pay1=float(pay.get())
                                                                        sql1="insert into registration values(%s,%s)"
                                                                        val1=(doc1,pay1)
                                                                        myc.execute(sql1,val1)
                                                                        myc.execute("select cphno,caddr from customers where cname=%s",(cname1,))
                                                                        for i in myc:
                                                                                lph=i[0]
                                                                                lad=i[1]
                                                                        sql2="insert into landowners values(%s,%s,%s,%s)"
                                                                        val2=(cid,cname1,lph,lad)
                                                                        myc.execute(sql2,val2)
                                                                        mysql.commit()
                                                                        tk.messagebox.showinfo("Welcome","You have successfully registered and sold the land")
                                                                        sel2.destroy()
                                                                        enter()
                                                                def back5():
                                                                        sel2.destroy()
                                                                        sell()
                                                                        
                                                                n=5
                                                                background_image =Image.open("db1.jpg")
                                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                                if same:
                                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                                else:
                                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                                img = itk.PhotoImage(background_image)
                                                                Canvas2 = tk.Canvas(sel2)
                                                                Canvas2.create_image(780,340,image=img)      
                                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                                Label(sel2,text="REGISTRATION",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                                Label(sel2,text="Regdocs:",bg="light green",font="arial 14 bold").place(x=80,y=220)
                                                                Entry(sel2,textvar=doc,width=20,font="arial 13").place(x=240,y=222)
                                                                Label(sel2,text="Payment:",bg="light green",font="arial 14 bold").place(x=80,y=260)
                                                                Entry(sel2,textvar=pay,width=20,font="arial 13").place(x=240,y=262)
                                                                Button(sel2,text="register",bg='blue',font="arial 12 bold", fg='black',command=reg).place(x=150,y=340)
                                                                Button(sel2,text="back",bg='blue',font="arial 12 bold", fg='black',command=back5).place(x=260,y=340)
                                                                sel2.mainloop()
                                                def back4():
                                                        sel.destroy()
                                                        enter()
                                                n=5
                                                background_image =Image.open("db1.jpg")
                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                if same:
                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                else:
                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                img = itk.PhotoImage(background_image)
                                                Canvas2 = tk.Canvas(sel)
                                                Canvas2.create_image(780,340,image=img)      
                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                Label(sel,text="ENTER LAND DETAILS",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                Label(sel,text="land no:",bg="light green",font="arial 14 bold").place(x=80,y=220)
                                                Entry(sel,textvar=lno,width=20,font="arial 13").place(x=240,y=222)
                                                Label(sel,text="location:",bg="light green",font="arial 14 bold").place(x=80,y=260)
                                                Entry(sel,textvar=loc,width=20,font="arial 13").place(x=240,y=262)
                                                Label(sel,text="area:",bg="light green",font="arial 14 bold").place(x=80,y=300)
                                                Entry(sel,textvar=ar,width=20,font="arial 13").place(x=240,y=302)
                                                Label(sel,text="amount:",bg="light green",font="arial 14 bold").place(x=80,y=340)
                                                Entry(sel,textvar=amt,width=20,font="arial 13").place(x=240,y=342)
                                                Button(sel,text="sell",bg='blue',font="arial 12 bold", fg='black',command=sell2).place(x=150,y=380)
                                                Button(sel,text="back",bg='blue',font="arial 12 bold", fg='black',command=back4).place(x=230,y=380)
                                                sel.mainloop()
                                        def agents():
                                                global flag3
                                                if flag3==1 and flag3!=0:
                                                        ent.destroy()
                                                        flag3=flag3+1
                                                ag=tk.Tk()
                                                def back6():
                                                        ag.destroy()
                                                        enter()
                                                n=2
                                                background_image =Image.open("da2.jpg")
                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                if same:
                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                else:
                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                img = itk.PhotoImage(background_image)
                                                Canvas2 = tk.Canvas(ag)
                                                Canvas2.create_image(780,340,image=img)      
                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                Label(ag,text="AGENT DETAILS",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                Label(ag,text="%-20s%-20s%-20s%-20s    "%("Agentid","Name","Phone No","Address"),font="arial 16 bold").place(x=80,y=220)
                                                myc.execute("select agentid,aname,aphno,aaddr from agents")
                                                b=250
                                                for i in myc:
                                                        Label(ag,text="%-30s%-30s%-25s%-25s"%(i[0],i[1],i[2],i[3]),font="arial 14",bg="light blue").place(x=80,y=b)
                                                        b=b+30
                                                Button(ag,text="back",bg='blue',font="arial 12 bold", fg='black',command=back6).place(x=380,y=740)
                                                ag.mainloop()
                                        def brokers():
                                                global flag3
                                                if flag3==1 and flag3!=0:
                                                        ent.destroy()
                                                        flag3=flag3+1
                                                br=tk.Tk()
                                                def back7():
                                                        br.destroy()
                                                        enter()
                                                n=2
                                                background_image =Image.open("da2.jpg")
                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                if same:
                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                else:
                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                img = itk.PhotoImage(background_image)
                                                Canvas2 = tk.Canvas(br)
                                                Canvas2.create_image(780,340,image=img)      
                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                Label(br,text="BROKER DETAILS",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                Label(br,text="%-20s%-20s%-20s%-20s     "%("Brokerid","Name","Phone No","Address"),font="arial 16 bold").place(x=80,y=220)
                                                myc.execute("select brokerid,bname,bphno,baddr from brokers")
                                                b=250
                                                for i in myc:
                                                        Label(br,text="%-30s%-30s%-25s%-25s"%(i[0],i[1],i[2],i[3]),font="arial 14",bg="light blue").place(x=80,y=b)
                                                        b=b+30
                                                Button(br,text="back",bg='blue',font="arial 12 bold", fg='black',command=back7).place(x=380,y=740)
                                                br.mainloop()
                                        def customers():
                                                global flag3
                                                if flag3==1 and flag3!=0:
                                                        ent.destroy()
                                                        flag3=flag3+1
                                                cu=tk.Tk()
                                                def back8():
                                                        cu.destroy()
                                                        enter()
                                                n=2
                                                background_image =Image.open("da2.jpg")
                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                if same:
                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                else:
                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                img = itk.PhotoImage(background_image)
                                                Canvas2 = tk.Canvas(cu)
                                                Canvas2.create_image(780,340,image=img)      
                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                Label(cu,text="CUSTOMERS DETAILS",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                Label(cu,text="%-20s%-20s%-20s%-20s%-20s          "%("Customerid","Name","Phone No","Address","Gmailid"),font="arial 16 bold").place(x=80,y=220)
                                                myc.execute("select custid,cname,cphno,caddr,gmailid from customers")
                                                b=250
                                                for i in myc:
                                                        Label(cu,text="%-35s%-27s%-26s%-28s%-20s"%(i[0],i[1],i[2],i[3],i[4]),font="arial 14",bg="light blue").place(x=80,y=b)
                                                        b=b+30
                                                Button(cu,text="back",bg='blue',font="arial 12 bold", fg='black',command=back8).place(x=380,y=740)
                                                cu.mainloop()
                                                
                                                
                                                
                                                
                                        def avail():
                                                global flag3
                                                if flag3==1 and flag3!=0:
                                                        ent.destroy()
                                                        flag3=flag3+1
                                                av=tk.Tk()
                                                def back9():
                                                        av.destroy()
                                                        enter()
                                                n=2
                                                background_image =Image.open("da2.jpg")
                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                if same:
                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                else:
                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                img = itk.PhotoImage(background_image)
                                                Canvas2 = tk.Canvas(av)
                                                Canvas2.create_image(780,340,image=img)      
                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                Label(av,text="AVAILABLE LAND DETAILS",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                Label(av,text="%-20s%-20s%-20s%-20s       "%("Landno","Area","Location","Amount"),font="arial 16 bold").place(x=80,y=220)
                                                myc.execute("select landno,larea,lloc,lamount from bland")
                                                b=250
                                                for i in myc:
                                                        Label(av,text="%-30s%-30s%-25s%-25s"%(i[0],i[1],i[2],i[3]),font="arial 14",bg="light blue").place(x=80,y=b)
                                                        b=b+30
                                                Button(av,text="back",bg='blue',font="arial 12 bold", fg='black',command=back9).place(x=380,y=740)
                                                av.mainloop()
                                        def bought():
                                                global flag3
                                                if flag3==1 and flag3!=0:
                                                        ent.destroy()
                                                        flag3=flag3+1
                                                bo=tk.Tk()
                                                def back10():
                                                        bo.destroy()
                                                        enter()
                                                n=2
                                                background_image =Image.open("da2.jpg")
                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                if same:
                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                else:
                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                img = itk.PhotoImage(background_image)
                                                Canvas2 = tk.Canvas(bo)
                                                Canvas2.create_image(780,340,image=img)      
                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                Label(bo,text="BOUGHT LAND DETAILS",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                Label(bo,text="%-20s%-20s%-20s%-20s       "%("Landno","Area","Location","Amount"),font="arial 16 bold").place(x=80,y=220)
                                                global cname1
                                                myc.execute("select custid from customers where cname=%s",(cname1,))
                                                for i in myc:
                                                        cid=i[0]
                                                myc.execute("select landno,larea,lloc,lamountpaid from cland where custid=%s",(cid,))
                                                b=250
                                                for i in myc:
                                                        Label(bo,text="%-30s%-30s%-25s%-25s"%(i[0],i[1],i[2],i[3]),font="arial 14",bg="light blue").place(x=80,y=b)
                                                        b=b+30
                                                Button(bo,text="back",bg='blue',font="arial 12 bold", fg='black',command=back10).place(x=380,y=740)
                                                bo.mainloop()
                                        def sold():
                                                global flag3
                                                if flag3==1 and flag3!=0:
                                                        ent.destroy()
                                                        flag3=flag3+1
                                                so=tk.Tk()
                                                def back11():
                                                        so.destroy()
                                                        enter()
                                                n=2
                                                background_image =Image.open("da2.jpg")
                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                if same:
                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                else:
                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                img = itk.PhotoImage(background_image)
                                                Canvas2 = tk.Canvas(so)
                                                Canvas2.create_image(780,340,image=img)      
                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                Label(so,text="SOLD LAND DETAILS",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                Label(so,text="%-20s%-20s%-20s%-20s       "%("Landno","Area","Location","Amount"),font="arial 16 bold").place(x=80,y=220)
                                                global cname1
                                                myc.execute("select custid from customers where cname=%s",(cname1,))
                                                for i in myc:
                                                        cid=i[0]
                                                myc.execute("select landno,larea,lloc,lvalue from bland where lownerid=%s",(cid,))
                                                b=250
                                                for i in myc:
                                                        Label(so,text="%-30s%-30s%-25s%-25s"%(i[0],i[1],i[2],i[3]),font="arial 14",bg="light blue").place(x=80,y=b)
                                                        b=b+30
                                                Button(so,text="back",bg='blue',font="arial 12 bold", fg='black',command=back11).place(x=380,y=740)
                                                so.mainloop()
                                                
                                                
                                        def profile():
                                                global flag3
                                                if flag3==1 and flag3!=0:
                                                        ent.destroy()
                                                        flag3=flag3+1
                                                pf=tk.Tk()
                                                def back12():
                                                        pf.destroy()
                                                        enter()
                                                n=2
                                                background_image =Image.open("sverm.jpg")
                                                [imageSizeWidth, imageSizeHeight] = background_image.size
                                                newImageSizeWidth = int(imageSizeWidth*n)
                                                if same:
                                                         newImageSizeHeight = int(imageSizeHeight*n) 
                                                else:
                                                        newImageSizeHeight = int(imageSizeHeight/n) 
                                                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                                img = itk.PhotoImage(background_image)
                                                Canvas2 = tk.Canvas(pf)
                                                Canvas2.create_image(780,340,image=img)      
                                                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                                Canvas2.pack(expand=True,fill=tk.BOTH)
                                                global cname1
                                                myc.execute("select custid from customers where cname=%s",(cname1,))
                                                for i in myc:
                                                        cid=i[0]
                                                myc.execute("select cname,cphno,caddr,gmailid from customers where custid=%s",(cid,))
                                                for i in myc:
                                                        name=i[0]
                                                        phno=i[1]
                                                        adr=i[2]
                                                        gmail=i[3]
                                                myc.execute("select password from users where username=%s",(name,))
                                                for i in myc:
                                                        pwd=i[0]
                                                Label(pf,text="PROFILE",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                                                Label(pf,text="Name :",bg="light green",font="arial 14 bold").place(x=80,y=240)
                                                Label(pf,text=name,width=20,font="arial 13").place(x=200,y=242) 
                                                Label(pf,text="Gmailid :",bg="light green",font="arial 14 bold").place(x=80,y=280)
                                                Label(pf,text=gmail,width=20,font="arial 13").place(x=200,y=282)
                                                Label(pf,text="Password :",bg="light green",font="arial 14 bold").place(x=80,y=320)
                                                Label(pf,text=pwd,width=20,font="arial 13").place(x=200,y=322)
                                                Label(pf,text="Address :",bg="light green",font="arial 14 bold").place(x=80,y=360)
                                                Label(pf,text=adr,width=20,font="arial 13").place(x=200,y=362)
                                                Label(pf,text="Phoneno :",bg="light green",font="arial 14 bold").place(x=80,y=400)
                                                Label(pf,text=phno,width=20,font="arial 13").place(x=200,y=402)
                                                Button(pf,text="back",bg='blue',font="arial 12 bold", fg='black',command=back12).place(x=380,y=480)
                                                pf.mainloop()
                                        def logout():
                                                tk.messagebox.showinfo("Welcome","You have successfully logged out")
                                                ent.destroy()
                                                home()
                                        n=1
                                        background_image =Image.open("sverm.jpg")
                                        [imageSizeWidth, imageSizeHeight] = background_image.size
                                        newImageSizeWidth = int(imageSizeWidth*n)
                                        if same:
                                                 newImageSizeHeight = int(imageSizeHeight*n) 
                                        else:
                                                newImageSizeHeight = int(imageSizeHeight/n) 
                                        background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                                        img = itk.PhotoImage(background_image)
                                        Canvas3 = tk.Canvas(ent)
                                        Canvas3.create_image(780,340,image=img)      
                                        Canvas3.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                                        Canvas3.pack(expand=True,fill=tk.BOTH)
                                        Label(ent,text="WELCOME %-10s "%(cname1),relief="solid",width=40,font="arial 28 bold",bg="light green",fg="black").place(x=350,y=400)
                                        menu=Menu(ent,font="arial 17 bold",bg="red",fg="black")
                                        ent.config(menu=menu)
                                        s1=Menu(menu)
                                        menu.add_cascade(label="SEARCH",menu=s1)
                                        s1.add_command(label="search land",command=search)
                                        s2=Menu(menu)
                                        menu.add_cascade(label="BUY",menu=s2)
                                        s2.add_command(label="buy land",command=buy)
                                        s3=Menu(menu)
                                        menu.add_cascade(label="SELL",menu=s3)
                                        s3.add_command(label="sell land",command=sell)
                                        s4=Menu(menu)
                                        menu.add_cascade(label="COMPANY DETAILS",menu=s4)
                                        s4.add_command(label="Agents",command=agents)
                                        s4.add_command(label="Brokers",command=brokers)
                                        s4.add_command(label="Customers",command=customers)
                                        s5=Menu(menu)
                                        menu.add_cascade(label="LAND DETAILS",menu=s5)
                                        s5.add_command(label="Available lands",command=avail)
                                        s5.add_command(label="Bought land",command=bought)
                                        s5.add_command(label="Sold land",command=sold)
                                        s6=Menu(menu)
                                        menu.add_cascade(label="MY ACCOUNT",menu=s6)
                                        s6.add_command(label="Profile",command=profile)
                                        s6.add_command(label="Logout",command=logout)
                                        
                                        ent.mainloop()
                                        
                                        
                                else:
                                        tk.messagebox.showinfo("Sorry","WRONG PASSWORD")
                                        lab.destroy()
                                        Login()
                                        
                                        
                         else:
                                tk.messagebox.showinfo("Sorry","INVALID USERNAME")
                                lab.destroy()
                                Login()
                                
                                        
                background_image =Image.open("db1.jpg")
                [imageSizeWidth, imageSizeHeight] = background_image.size
                newImageSizeWidth = int(imageSizeWidth*n)
                if same:
                         newImageSizeHeight = int(imageSizeHeight*n) 
                else:
                        newImageSizeHeight = int(imageSizeHeight/n) 
                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                img = itk.PhotoImage(background_image)
                Canvas2 = tk.Canvas(lab)
                Canvas2.create_image(780,380,image=img)      
                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                Canvas2.pack(expand=True,fill=tk.BOTH)
                Label(lab,text="Log In",relief="solid",width=40,font="arial 19 bold").place(x=80,y=150)
                Label(lab,text="Username :",bg="light green",font="arial 14 bold").place(x=80,y=240)
                Entry(lab,textvar=cname,width=20,font="arial 13").place(x=200,y=242)
                Label(lab,text="Password :",bg="light green",font="arial 14 bold").place(x=80,y=280)
                Entry(lab,textvar=pwd,width=20,font="arial 13").place(x=200,y=282)
                Button(lab,text="login",bg='blue',font="arial 12 bold", fg='black',command=enter).place(x=180,y=340)
                lab.mainloop()
        def Signup():
                window.destroy()
                n=5
                lab2=tk.Tk()
                cname=StringVar()
                gmail=StringVar()
                pwd=StringVar()
                adr=StringVar()
                phno=StringVar()
                def save():
                        myc.execute("select username from users")
                        c=[]
                        cname1=str(cname.get())
                        for i in myc:
                                c.append(i[0])
                        if cname1 in c:
                                Signup.destroy()
                                tk.messagebox.showinfo("Sorry","Already user exists!!!")
                                Signup()
                        else:
                                myc.execute("select count(custid) from customers")
                                for i in myc:
                                         cid3=i[0]
                                pwd1=str(pwd.get())
                                sql="insert into users values(%s,%s)"
                                val=(cname1,pwd1)
                                myc.execute(sql,val)
                                cid3=cid3+1
                                adr1=str(adr.get())
                                gmail1=str(gmail.get())
                                phno1=str(phno.get())
                                sql2="insert into customers values(%s,%s,%s,%s,%s)"
                                val2=(cid3,cname1,phno1,adr1,gmail1)
                                myc.execute(sql2,val2)
                                mysql.commit()
                                tk.messagebox.showinfo("WELCOME","You have successfully signed up")
                                lab2.destroy()
                                home()
                                        
                background_image =Image.open("db2.jpg")
                [imageSizeWidth, imageSizeHeight] = background_image.size
                newImageSizeWidth = int(imageSizeWidth*n)
                if same:
                         newImageSizeHeight = int(imageSizeHeight*n) 
                else:
                        newImageSizeHeight = int(imageSizeHeight/n) 
                background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
                img = itk.PhotoImage(background_image)
                Canvas2 = tk.Canvas(lab2)
                Canvas2.create_image(780,380,image=img)      
                Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
                Canvas2.pack(expand=True,fill=tk.BOTH)
                Label(lab2,text="SignUp",relief="solid",width=40,font="arial 19 bold").place(x=90,y=150)
                Label(lab2,text="Username :",bg="light green",font="arial 14 bold").place(x=80,y=240)
                Entry(lab2,textvar=cname,width=20,font="arial 13").place(x=200,y=242)
                Label(lab2,text="Gmailid :",bg="light green",font="arial 14 bold").place(x=80,y=280)
                Entry(lab2,textvar=gmail,width=20,font="arial 13").place(x=200,y=282)
                Label(lab2,text="Password :",bg="light green",font="arial 14 bold").place(x=80,y=320)
                Entry(lab2,textvar=pwd,width=20,font="arial 13").place(x=200,y=322)
                Label(lab2,text="Address :",bg="light green",font="arial 14 bold").place(x=80,y=360)
                Entry(lab2,textvar=adr,width=20,font="arial 13").place(x=200,y=362)
                Label(lab2,text="Phoneno :",bg="light green",font="arial 14 bold").place(x=80,y=400)
                Entry(lab2,textvar=phno,width=20,font="arial 13").place(x=200,y=402)
                Button(lab2,text="signup",bg='blue',font="arial 12 bold", fg='black',command=save).place(x=180,y=460)
                lab2.mainloop()
        def quitt():
                tk.messagebox.showinfo("WELCOME","Do you wanna quit")
                window.destroy()
                
        background_image =Image.open("sverm.jpg")
        [imageSizeWidth, imageSizeHeight] = background_image.size

        newImageSizeWidth = int(imageSizeWidth*n)
        if same:
                 newImageSizeHeight = int(imageSizeHeight*n) 
        else:
                newImageSizeHeight = int(imageSizeHeight/n) 
            
        background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
        img = itk.PhotoImage(background_image)
        Canvas1 = tk.Canvas(window)
        Canvas1.create_image(780,340,image=img)      
        Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
        Canvas1.pack(expand=True,fill=tk.BOTH)

        headingFrame1 = Frame(window,bg="#333945",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

        headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
        headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

        headingLabel = Label(headingFrame2, text="Welcome to NAVEEN SVE REAL ESTATE", fg='black',font="Times 18 bold")
        headingLabel.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.5)

        btn1 = Button(window,text="Login",bg='white', fg='black',font="arial 12",command=Login)
        btn1.place(relx=0.25,rely=0.3, relwidth=0.2,relheight=0.1)

        btn2 = Button(window,text="SignUp",bg='white', fg='black',font="arial 12", command=Signup)
        btn2.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)

        btn3 = Button(window,text="quit",bg='blue', fg='black',font="arial 12", command=quitt)
        btn3.place(relx=0.45,rely=0.8, relwidth=0.1,relheight=0.05)
        window.mainloop()
        
home()





