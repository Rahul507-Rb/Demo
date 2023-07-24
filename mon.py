from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter.font
import home,main,login,Home01


class Page:
    def __init__(self):
        self.root = Tk()
        self.root.title('Home Window')
        self.root.geometry('1000x500')
        self.root.resizable(False,False)
        
         # FRAME PART 1
        self.frame1=Frame(self.root,bg='#00bfff',width=1000,height=350)
        self.frame1.place(x=0,y=0)
        
         # HEADING ---- SIGN IN 
        self.heading=Label(self.frame1,text='Monday Forcast',fg='white',bg='#00bfff',font=('Lato',23,'bold'))
        self.heading.place(x=10,y=10)
        
         # IMAGE ICON
        self.img1 = Image.open('icon.png').resize((150,150))
        self.imgtk1 = ImageTk.PhotoImage(self.img1)
        self.imgLbl1 = Label(self.frame1,image=self.imgtk1,width=150,height=150,bg='#00bfff')
        self.imgLbl1.place(x=100,y=100)
        
        # IMAGE SEARCH
        self.img2 = Image.open('search.png').resize((450,400))
        self.imgtk2 = ImageTk.PhotoImage(self.img2)
        self.imgLbl2 = Label(self.frame1,image=self.imgtk2,width=320,height=150,bg='#00bfff')
        self.imgLbl2.place(x=700,y=-100)
        
        self.img3 = Image.open('icon.png').resize((30,40))
        self.imgtk3 = ImageTk.PhotoImage(self.img3)
        self.imgLbl3 = Label(self.frame1,image=self.imgtk3,width=30,height=30,bg='black')
        #self.btn=Button(self.frame2,width=25,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=self.signin)

        self.imgLbl3.place(x=720,y=20)
        
         # BUTTON --- SIGN IN
        self.btn=Button(self.frame1,width=25,pady=7,text='Next Page',bg='black',fg='white',border=0,command=self.signin)
        self.btn.place(x=600,y=300)
         # BUTTON --- SIGN IN
        self.btn=Button(self.frame1,width=25,pady=7,text='Back Page',bg='black',fg='white',border=0,command=self.signback)
        self.btn.place(x=800,y=300)
        
        
        self.root.mainloop()
        
      # BUTTON FUNCTION WORKED AND YOU ADD (COMMAND=SELF.'NAME_FUNCTION') IN BUTTON   
    def signback(self):
 
        self.root.destroy()
        Home01.Page()
    def signin(self):
 
        self.root.destroy()
        home.Home()
        
        
if __name__ == '__main__':
      Page()

        