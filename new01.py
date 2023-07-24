from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import login,Home01,home,database

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Sign In window")
        self.root.geometry('1000x500')
        self.root.config(bg='white')
        self.root.resizable(False,False)
        
        
        # FRAME PART 2
        self.frame2=Frame(self.root,bg='white',width=500,height=500)
        self.frame2.place(x=500,y=0)
        
         # HEADING ---- SIGN IN 
        self.heading=Label(self.frame2,text='Sign In',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        self.heading.place(x=150,y=100)
        
        
        # USERNAME
        self.username=Label(self.frame2,text='UserName :',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',15,'bold'))
        self.username.place(x=10,y=180)
        # USER INPUT
        self.userentry = Entry(self.frame2,font=('Microsoft YaHei UI Light',15,'bold'))
        self.userentry.place(x=150,y=180)
        
       
       
        # PASSWORD
        self.userpass=Label(self.frame2,text='Password  :',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',15,'bold'))
        self.userpass.place(x=10,y=250)
        # USER INPUT
        self.userpass = Entry(self.frame2,show='*',font=('Microsoft YaHei UI Light',15,'bold'))
        self.userpass.place(x=150,y=250)
        
         # BUTTON --- SIGN IN
        self.btn=Button(self.frame2,width=25,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=self.signin)
        self.btn.place(x=130,y=330)
        
        # BUTTON LOGIN
        self.label=Label(self.frame2,text="Already have an Account ?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        self.label.place(x=120,y=380)

        self.sign_up= Button(self.frame2,width=6,text='LogIn',border=0,bg='white',cursor='hand2',fg='#57a1f8')
        self.sign_up.place(x=260,y=380)
        
        if self.type == 'Edit':
            d = self.data.get('values')
            print('d is',d)
            self.userentry.insert(0,d[0])
            self.userpass.insert(0,d[1])
        
        
          # MAINLOOP
        self.root.mainloop()
        
        # REGISTER DATA
    def register(self):
        if  self.userentry.get() and self.userpass.get():
            if self.type == 'Edit':
              res = database.registeruser((self.userentry.get(),self.userpass.get(),self.data.get('text')))
              
            
            res = database.registeruser((self.userentry.get(),self.userpass.get()))
            if res :
                messagebox.showinfo('success')
            else:
                messagebox.showerror('Alert')
        else:
            messagebox.showerror('Enter detail')
        
        
         # LOGIN 
    def signin(self):
 
        self.root.destroy()
        home.Home()
           
        
if __name__=='__main__':
     Main()
