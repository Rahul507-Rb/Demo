from tkinter import *
#import socket 
#from geopy.geocoders import Nominatim
#from timezonefinder import TimezoneFinder
#from datetime import *
#import requests
#import pytz
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter.font
import home,main,login,mon


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
        self.heading=Label(self.frame1,text='Weather Forcast',fg='white',bg='#00bfff',font=('Lato',23,'bold'))
        self.heading.place(x=10,y=10)
        
         # IMAGE ICON
        self.img1 = Image.open('images/icon.png').resize((150,150))
        self.imgtk1 = ImageTk.PhotoImage(self.img1)
        self.imgLbl1 = Label(self.frame1,image=self.imgtk1,width=150,height=150,bg='#00bfff')
        self.imgLbl1.place(x=100,y=100)
        
        # IMAGE SEARCH
        self.img2 = Image.open('images/search.png').resize((450,400))
        self.imgtk2 = ImageTk.PhotoImage(self.img2)
        self.imgLbl2 = Label(self.frame1,image=self.imgtk2,width=320,height=150,bg='#00bfff')
        self.imgLbl2.place(x=700,y=-100)
        
        self.img3 = Image.open('images/icon.png').resize((30,40))
        self.imgtk3 = ImageTk.PhotoImage(self.img3)
        self.imgLbl3 = Label(self.frame1,image=self.imgtk3,width=30,height=30,bg='black')
        #self.btn=Button(self.frame2,width=25,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=self.signin)

        self.imgLbl3.place(x=720,y=20)
        
        # text typing
        self.textfield = Entry(self.frame1,justify='center',width=15,bg='#203243',border=0,fg='white',font=('Microsoft YaHei UI Light',15,'bold'))
        self.textfield.place(x=760,y=22)
        
        #img_btn
        self.img10 = Image.open('images/rectangle.png').resize((20,30))
        self.click_btn9 =ImageTk.PhotoImage(self.img10)
        self.img_label = Label(image=self.click_btn9)
        self.button = Button(self.frame1,image=self.click_btn9,width=30,bg='white',pady=2,borderwidth=0) .place(x=940,y=20)
        # clock
        self.clock=Label(self.frame1,text='2:30 PM',fg='white',bg='#00bfff',font=('Lato',23,'bold'))
        self.clock.place(x=400,y=100)
        
        # time zone
        self.time_zone=Label(self.frame1,text='Asia',fg='white',bg='#00bfff',font=('Lato',23,'bold'))
        self.time_zone.place(x=300,y=100)
        
        self.lon_lat=Label(self.frame1,text='13.33./23.4.44.4',fg='white',bg='#00bfff',font=('Lato',23,'bold'))
        self.lon_lat.place(x=300,y=200)
        
         # BUTTON --- SIGN IN
        self.btn=Button(self.frame1,width=25,pady=7,text='Next Page',bg='black',fg='white',border=0,command=self.signin)
        self.btn.place(x=600,y=300)
        
         # BUTTON --- SIGN IN
        self.btn=Button(self.frame1,width=25,pady=7,text='Back Page',bg='black',fg='white',border=0,command=self.signback)
        self.btn.place(x=800,y=300)
        
    
        
         
        # FRAME PART 2
        self.frame2=Frame(self.root,bg='#00bfff',width=1000,height=150)
        self.frame2.place(x=0,y=350)
        # IMAGE 
        self.img2 = Image.open('images/rectangle.png').resize((150,150))
        self.click_btn =ImageTk.PhotoImage(self.img2)
        #self.img_label = Label(image=self.click_btn)
        self.button = Button(self. frame2,image=self.click_btn,width=150,bg='#00bfff',pady=7,borderwidth=0,command=self.signin) .place(x=50,y=15)
        self.button1 = Button(self.frame2,image=self.click_btn,width=150,bg='#00bfff',pady=7,borderwidth=0,command=self.signin).place(x=200,y=15)
        self.button2 = Button(self.frame2,image=self.click_btn,width=150,bg='#00bfff',pady=7,borderwidth=0,command=self.signin).place(x=350,y=15)
        self.button3 = Button(self.frame2,image=self.click_btn,width=150,bg='#00bfff',pady=7,borderwidth=0,command=self.signin).place(x=500,y=15)
        self.button4 = Button(self.frame2,image=self.click_btn,width=150,bg='#00bfff',pady=7,borderwidth=0,command=self.signin).place(x=650,y=15)
        self.button5 = Button(self.frame2,image=self.click_btn,width=150,bg='#00bfff',pady=7,borderwidth=0,command=self.signin).place(x=800,y=15)
        

       
        
        # HEADING ---- SIGN IN 
         # BUTTON --- SIGN IN
        self.btn1=Button(self.frame2,width=7,pady=7,text='Mon',bg='black',fg='#00bfff',font=('Lato',16,'bold'),border=0,command=self.mon).place(x=70, y=50)
        self.btn2=Button(self.frame2,width=7,pady=7,text='Tue',bg='black',fg='#00bfff',font=('Lato',16,'bold'),border=0,command=self.signin).place(x=230,y=50)
        self.btn3=Button(self.frame2,width=7,pady=7,text='Wed',bg='black',fg='#00bfff',font=('Lato',16,'bold'),border=0,command=self.signin).place(x=380,y=50)
        self.btn4=Button(self.frame2,width=7,pady=7,text='Thu',bg='black',fg='#00bfff',font=('Lato',16,'bold'),border=0,command=self.signin).place(x=530,y=50)
        self.btn5=Button(self.frame2,width=7,pady=7,text='Fri',bg='black',fg='#00bfff',font=('Lato',16,'bold'),border=0,command=self.signin).place(x=680,y=50)
        self.btn6=Button(self.frame2,width=7,pady=7,text='Sat',bg='black',fg='#00bfff',font=('Lato',16,'bold'),border=0,command=self.signin).place(x=830,y=50)
      
   
                
        self.root.mainloop()
        
        
    # time zone and clock
    #def getweather(self):
    #    self.city = self.textfield.get()
    #    
    #    self.geoloactor = Nominatim(user_agent = "geopiExercises")
    #    self.location = self.geoloactor.geocode(self.city)
    #    self.obj = self.TimezoneFinder()
    #    
    #    self.result = self.obj.timezone_at(lng =self.location.longitude,lat =self. location.latitude)
    #    
    #    self.timezone.config(text = self.result)
    #    self.long_lat.config(text=f"{round(self.location.latitude,4)}°N,{round(self.location.latitude)}°E")

        
      # BUTTON FUNCTION WORKED AND YOU ADD (COMMAND=SELF.'NAME_FUNCTION') IN BUTTON   
    def signback(self):
 
        self.root.destroy()
        main.Main()
    def signin(self):
 
        self.root.destroy()
        home.Home()
    def mon(self):
 
        self.root.destroy()
        mon.Page()
        

        
if __name__ == '__main__':
      Page()
