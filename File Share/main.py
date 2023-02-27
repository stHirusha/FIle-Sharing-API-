from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
import socket
import os

def on_entry_click(event):
   if sender_id.get() == "Sender ID":
      sender_id.delete(0,'end')
      sender_id.config(fg = "black")   
   
   elif file_name.get() == "File Name":
      file_name.delete(0,'end')
      file_name.config(fg = "black")  

def select_file():
   global filename
   filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Send Image File",filetype=(('file_type','.*txt'),('all files','*.*')))

def sender():
   s = socket.socket()
   host =socket.gethostname()
   port = 8080
   s.bind((host,port))
   s.listen(1)
   print(host)
   print('Waiting for any incomingconnections....')
   conn,addr=s.accept()
   file=open(filename,'rb')
   file_data = file.read(1024)
   conn.send(file_data)
   print('Data has been tranfered....')
   
def recive_file():
   ID = sender_id.get()
   filename_1 = file_name.get()
   
   s= socket.socket()
   port = 8080
   s.connect((ID,port))
   file= open(filename_1,"wb")
   file_data = s.recv(1024)
   file.write(file_data)
   file.close
   print("File has been received....")

def send():
   window = Toplevel(root)
   window.title("Send")
   window.geometry("450x560+20+20")
   window.resizable(False,False)
   window.iconbitmap("send.ico")
   window.config(bg = "#f4fdfe")
   
   background = Image.open("sender.png")
   background = ImageTk.PhotoImage(background)
   Label(window,image=background).place(x=-2,y=0)
   
   Button(window,text="Browse",font=("Acumn Variable Concept",10,"bold"),bd=2,width=15,command=select_file).place(x= 152,y=100)
   Button(window,text="Send",font=("Acumn Variable Concept",10,"bold"),bd=2,width=15,command=sender).place(x= 302,y=100)
   
   background_2 = Image.open("id.png")
   background_2 = ImageTk.PhotoImage(background_2)
   Label(window,image=background_2,bg="#f4fdfe").place(x=110,y=270)
  
   host = socket.gethostname()
   Label(window, text = f"ID: {host}",bg= "white",fg = "black").place(x=175,y=305)
   
   window.mainloop()

def recive():
   global sender_id,file_name,sender_id,file_name
   window = Toplevel(root)
 
   window.title("Recive")
   window.geometry("450x560+20+20")
   window.resizable(False,False)
   window.iconbitmap("recive.ico")
   window.config(bg = "#f4fdfe")
   
   background = Image.open("background_2.png")
   background = ImageTk.PhotoImage(background)
   Label(window,image=background).place(x=-2,y=0)
   
   Label(window,text = "Recive", font=("Acumn Variable Concept",30,"bold"),bg="#f4fdfe").place(x = 13,y = 240)
   
   background_2 = Image.open("profile.png")
   background_2 = ImageTk.PhotoImage(background_2)
   Label(window,image=background_2,bg="#f4fdfe").place(x=15,y=300)

   sender_id = Entry(window, fg="grey",font=("Acumn Variable Concept",15),width = 30)
   sender_id.insert(0,"Sender ID") 
   sender_id.bind('<FocusIn>',on_entry_click)  
   sender_id.place(x= 15,y=400)   
   #sender_id.focus()
   
   file_name = Entry(window, fg="grey",font=("Acumn Variable Concept",15),width= 30)
   file_name.insert(0,"File Name") 
   file_name.bind('<FocusIn>',on_entry_click)  
   file_name.place(x= 15,y=450)  
   
   Button(window,text="Recive",font=("Acumn Variable Concept",10,"bold"),bd=2,width=15,bg="#39fc03",command=recive_file).place(x= 15,y= 500) 
     
   window.mainloop()

root = Tk()
root.title("File-Transfer")
root.geometry("450x560+20+20")
root.resizable(False,False)
root.iconbitmap("share.ico")
root.config(bg = "#f4fdfe")

Label(root,text = "Share-Files", font=("Acumn Variable Concept",30,"bold"),bg="#f4fdfe").place(x = 110,y = 10)

send_image = Image.open("send.png")
send_image = send_image.resize((147,147),Image.ANTIALIAS)
send_image = ImageTk.PhotoImage(send_image)
Button(root,image=send_image,bg="#f4fdfe",bd=0,command=send).place(x=30,y=75)
recive_image = Image.open("recive.png")
recive_image = recive_image.resize((261,175),Image.ANTIALIAS)
recive_image = ImageTk.PhotoImage(recive_image)
Button(root,image=recive_image,bg="#f4fdfe",bd=0,command=recive).place(x=200,y=65)

Label(root,text="Send",font=("Acumn Variable Concept",20),bg="#f4fdfe").place(x=67,y=235)
Label(root,text="Recive",font=("Acumn Variable Concept",20),bg="#f4fdfe").place(x=285,y=235)

background = Image.open("background.jpg")
background = background.resize((478,280),Image.ANTIALIAS)
background = ImageTk.PhotoImage(background)
Label(root,image=background).place(x = -20,y = 290)

root.mainloop()