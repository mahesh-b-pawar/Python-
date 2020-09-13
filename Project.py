from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *
import socket 
import requests
import bs4
import matplotlib.pyplot as plt
import numpy as ny
import pandas as pd

	
def f1():
	root.withdraw()
	adst.deiconify()

def f2():
	adst.withdraw()
	root.deiconify()

def f3():
	stViewData.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select rno,name,marks from studentss"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
				msg=msg +" rno= " + str(d[0]) + " name= " + str(d[1]).strip() + " marks= " + str(d[2]) + "\n"
		stViewData.insert(INSERT,msg)
	except DatabaseError as e:
		messagebox.showerror("Galat kiya ",e)
	finally:
		if con is not None:
			con.close()

def f4():
	vist.withdraw()
	root.deiconify()

def f5():
	class IDException(Exception):
		pass
	class NameException(Exception):
		pass
	class MarksException(Exception):
		pass
	con=None
	try:
		con=connect("system/abc123")
		rno=entAddRno.get()
		name=entAddName.get()
		marks=entAddMarks.get()
		rno=rno.strip()
		name=name.strip()
		marks=marks.strip()
		if(len(rno)==0):
			raise IDException("Roll number cannot empty ")
	
		if (rno.isdigit()):
			pass
		else:
			raise IDException("Roll number should only be positive integer")
		r=int(rno)
		if r < 1:
			raise IDException("Roll number should only be positive integer")
		
		if(len(name)==0):
			raise NameException("Name cannot be empty ")
		
		name=name.replace(' ','')
		if (name.isalpha()):
			pass
		else:
			raise NameException("Name should not have numbers and special characters")
		if len(name) < 2 :
			raise NameException("Enter valid name")
	
		if(len(marks)==0):
			raise MarksException("Marks cannot be empty")
		if(marks.count('.')<=1):
			if(marks.isdigit() or marks.find('.')!=-1 ):
				if float(marks)<0 or float(marks)>100 :
					raise MarksException("Marks should only be betweeen 0 to 100")
			else:
				raise MarksException("Improper marks entry")
		else:
			raise MarksException("Improper marks entry")
		args=(rno,name,marks)
		cursor=con.cursor()
		sql="insert into studentss values('%s','%s','%s')"
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("INSERT",str(cursor.rowcount)+" row inserted")
	except IDException as ie :
		messagebox.showerror("GALAT KIYA",ie)
		con.rollback()
	except NameException as ne :
		messagebox.showerror("GALAT KIYA",ne)
		con.rollback()
	except MarksException as me :
		messagebox.showerror("GALAT KIYA",me)
		con.rollback()
	except DatabaseError as e:
		messagebox.showerror("Galat kiya ",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddMarks.delete(0,END)
		entAddRno.focus()

def f6():
	con=None
	try:
		class IDException(Exception):
			pass
		class NameException(Exception):
			pass
		class MarksException(Exception):
			pass
		con=connect("system/abc123")
		nrno=entUpdateRno.get()
		nrno=nrno.strip()
		if(len(nrno)==0):
			raise IDException("Roll number cannot empty ")
	
		if (nrno.isdigit()):
			pass
		else:
			raise IDException("Roll number should only be positive integer")
		r=int(nrno)
		if r < 1:
			raise IDException("Roll number should only be positive integer")
		
		name=entUpdateName.get()
		marks=entUpdateMarks.get()
		name=name.strip()
		marks=marks.strip()
		if(len(name)==0):
			raise NameException("Name cannot be empty ")
		name=name.replace(' ','')
		if (name.isalpha()):
			pass
		else:
			raise NameException("Name should not have numbers and special characters")
		if len(name) < 2 :
			raise NameException("Enter valid name")
	
		if(len(marks)==0):
			raise MarksException("Marks cannot be empty")
		if(marks.count('.')<=1):
			if(marks.isdigit() or marks.find('.')!=-1 ):
				if float(marks)<0 or float(marks)>100 :
					raise MarksException("Marks should only be betweeen 0 to 100")
			else:
				raise MarksException("Improper marks entry")
		else:
			raise MarksException("Improper marks entry")
		args=(name,marks,nrno)
		cursor=con.cursor()
		sql="update studentss set name='%s',marks='%s' where rno='%s'"
		cursor.execute(sql % args)
		con.commit()
		count=cursor.rowcount
		if(count>=1):	
			messagebox.showinfo("UPDATE",str(cursor.rowcount)+" row updated")
		else:
			raise IDException("roll number not found")
	except IDException as ie :
		messagebox.showerror("GALAT KIYA",ie)
		con.rollback()	
	except NameException as ne :
		messagebox.showerror("GALAT KIYA",ne)
		con.rollback()
	except MarksException as me :
		messagebox.showerror("GALAT KIYA",me)
		con.rollback()
	except DatabaseError as e:
		messagebox.showerror("Galat kiya ",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entUpdateRno.delete(0,END)
		entUpdateName.delete(0,END)
		entUpdateMarks.delete(0,END)
		entUpdateRno.focus()
def f7():
	upst.withdraw()
	root.deiconify()

def f8():	
		
	con=None
	try:
		class IDException(Exception):
			pass
		con=connect("system/abc123")
		drno=entDeleteRno.get()
		drno=drno.strip()
		if(len(drno)==0):
			raise IDException("Roll number cannot empty ")
	
		if (drno.isdigit()):
			pass
		else:
			raise IDException("Roll number should only be positive integer")
		
		if int(drno) < 1:
			raise IDException("Roll number should only be positive integer")
		
		args=drno
		cursor=con.cursor()
		sql="delete from studentss where rno='%s' "
		cursor.execute(sql % args)
		con.commit()
		count=cursor.rowcount
		if(count >= 1):
			messagebox.showinfo("DELETE",str(cursor.rowcount)+" row deleted")
		else:
			raise IDException("roll number not found ")
			con.rollback()
		
	except IDException as ie :
		messagebox.showerror("GALAT KIYA",ie)
		con.rollback()	
	except DatabaseError as e:
		messagebox.showerror("Galat kiya ",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()	

def f9():
	dest.withdraw()
	root.deiconify()
	
def f10():
	root.withdraw()
	upst.deiconify()

def f11():
	root.withdraw()
	dest.deiconify()

def f12():
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select marks,name from studentss"
		cursor.execute(sql)
		data=cursor.fetchall()
		data.sort(reverse=True)
		
		Marks=[data[0][0],data[1][0],data[2][0]]
		Names=[data[0][1],data[1][1],data[2][1]]
		x=ny.arange(len(Marks))
		plt.bar(data[0][1],data[0][0],width=0.2,label=(str(data[0][1]).rstrip()))
		plt.bar(data[1][1],data[1][0],width=0.2,label=(str(data[1][1]).rstrip()))
		plt.bar(data[2][1],data[2][0],width=0.2,label=(str(data[2][1]).rstrip()))
		plt.title('Student Analysis')
		plt.xlabel('NAMES',fontsize=20)
		plt.ylabel('MARKS',fontsize=20)
		plt.legend()
		plt.grid()
		plt.show()
	except DatabaseError as e:
		messagebox.showerror("Galat kiya ",e)

	finally:
		if con is not None:
			con.close()

root =Tk() 
root.title("Student management system ")
root.geometry("550x550+200+100")


btnAdd=Button(root,text="Add",font=("Times New Roman",18,'bold'),width=10,command=f1)
btnView=Button(root,text="View",font=("Times New Roman",18,'bold'),width=10,command=f3)
btnUpdate=Button(root,text="Update",font=("Times New Roman",18,'bold'),width=10,command=f10)
btnDelete=Button(root,text="Delete",font=("Times New Roman",18,'bold'),width=10,command=f11)
btnGraph=Button(root,text="Graph",font=("Times New Roman",18,'bold'),width=10,command=f12)
T=Text(root,height=1.2,width=15,font=("Times New Roman",18,'bold'))
try:
		socket.create_connection(("www.google.com",80))
		#print("u r connected ")
		city="Mumbai"
		a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2="&q=" + city
		a3="&appid=c6e315d09197cec231495138183954bd"
		api_address=a1+a2+a3
		res1=requests.get(api_address)
		#print(res1)
		data=res1.json()
		#print(data)
		main=data['main']
		#print(main)
		temp=str(main['temp'])
		msg="Mumbai" + "     " + temp + "`C"
		T.insert(END,msg)
		
except OSError :
		messagebox.showerror("check network ")	

Q=Text(root,height=3,width=25,font=("Times New Roman",25,'bold'))
res=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")

soup= bs4.BeautifulSoup(res.text,'lxml')
quote= soup.find('img')
msgg=quote['alt']

Q.insert(END,msgg)

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
T.pack(pady=10)
Q.pack(pady=10)

adst=Toplevel(root)
adst.title("Add Student ")
adst.geometry("500x550+200+100")
adst.withdraw()
adst.configure(bg='dark green')
lblAddRno=Label(adst,text="Enter rno:",font=("Times New Roman",20,'bold'))
entAddRno=Entry(adst,bd=10,font=("Times New Roman",18,'bold'))

lblAddName=Label(adst,text="Enter name:",font=("Times New Roman",20,'bold'))
entAddName=Entry(adst,bd=10,font=("Times New Roman",18,'bold'))

lblAddMarks=Label(adst,text="Enter marks:",font=("Times New Roman",20,'bold '))
entAddMarks=Entry(adst,bd=10,font=("Times New Roman",18,'bold'))

btnAddSave=Button(adst,text="SAVE",font=("Times New Roman",18,'bold'),command=f5)
btnAddBack=Button(adst,text="BACK",font=("Times New Roman",18,'bold'),command=f2)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddMarks.pack(pady=10)
entAddMarks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)


vist=Toplevel(root)
vist.title("View Students ")
vist.geometry("500x500+200+100")
vist.withdraw()
vist.configure(bg='dark green')
stViewData=scrolledtext.ScrolledText(vist,width=50,height=20)
btnViewBack=Button(vist,text="BACK",font=("Times New Roman",18,'bold'),command=f4)
stViewData.pack(pady=10)
btnViewBack.pack(pady=10)



upst=Toplevel(root)
upst.title("Update Student ")
upst.geometry("500x550+200+100")
upst.withdraw()
upst.configure(bg='dark green')
lblUpdateRno=Label(upst,text="Enter rno:",font=("Times New Roman",20,'bold'))
entUpdateRno=Entry(upst,bd=10,font=("Times New Roman",18,'bold'))

lblUpdateName=Label(upst,text="Enter name:",font=("Times New Roman",20,'bold'))
entUpdateName=Entry(upst,bd=10,font=("Times New Roman",18,'bold'))

lblUpdateMarks=Label(upst,text="Enter marks:",font=("Times New Roman",20,'bold'))
entUpdateMarks=Entry(upst,bd=10,font=("Times New Roman",18,'bold'))

btnUpdateSave=Button(upst,text="SAVE",font=("Times New Roman",18,'bold'),command=f6)
btnUpdateBack=Button(upst,text="BACK",font=("Times New Roman",18,'bold'),command=f7)

lblUpdateRno.pack(pady=10)
entUpdateRno.pack(pady=10)
lblUpdateName.pack(pady=10)
entUpdateName.pack(pady=10)
lblUpdateMarks.pack(pady=10)
entUpdateMarks.pack(pady=10)
btnUpdateSave.pack(pady=10)
btnUpdateBack.pack(pady=10)

dest=Toplevel(root)
dest.title("Delete Student ")
dest.geometry("500x500+200+100")
dest.withdraw()
dest.configure(bg='dark green')
lblDeleteRno=Label(dest,text="Enter rno:",font=("Times New Roman",20,'bold'))
entDeleteRno=Entry(dest,bd=10,font=("Times New Roman",18,'bold'))

btnDeleteSave=Button(dest,text="SAVE",font=("Times New Roman",18,'bold italic'),command=f8)
btnDeleteBack=Button(dest,text="BACK",font=("Times New Roman",18,'bold italic'),command=f9)

lblDeleteRno.pack(pady=10)
entDeleteRno.pack(pady=10)
btnDeleteSave.pack(pady=10)
btnDeleteBack.pack(pady=10)



root.configure(bg='dark green')
root.mainloop()

