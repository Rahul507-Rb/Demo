from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
import Home01



class Home:
    def __init__(self):
        self.root = Tk()
        self.root.title('Home Window')
        self.root.geometry('800x600')
        
        #HEADINGs
        self.lbl= Label(self.root,text="Welcome New window",font=('Microsoft YaHei UI Light',23,'bold'))
        self.lbl.pack()
        
        # HEADING
        self.heading=Label(self.root,text='Drop Down',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        self.heading.place(x=100,y=100)
        
        # CREATE A DROP DOWN OPTION
        self.lbl2= Combobox(self.root,values=['Physics', 'Math','Chemistry'],width=12,font=('Microsoft YaHei UI Light',23,'bold'))
        self.lbl2.place(x=350,y=100)
        
        # HEADING
        self.heading=Label(self.root,text='Calendar    ',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        self.heading.place(x=100,y=200)
        
        # CREATE A CALENDAR
        self.lbl3 = DateEntry(self.root,font=('Microsoft YaHei UI Light',23,'bold'))
        self.lbl3.place(x=350,y=200)
        
         # BUTTON --- SIGN IN
        self.btn=Button(self.root,width=35,pady=10,text='Back Page',bg='#57a1f8',fg='white',border=0,command=self.signin)
        self.btn.place(x=280,y=350)
        
        
        
        
        
        self.root.mainloop()
        
        
      # BUTTON FUNCTION WORKED AND YOU ADD (COMMAND=SELF.'NAME_FUNCTION') IN BUTTON   
    def signin(self):
 
        self.root.destroy()
        Home01.Page()
        
        
        
if __name__ == '__main__':
      Home()
