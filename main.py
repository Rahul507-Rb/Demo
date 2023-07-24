from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import login,Home01,home,database,register,edit_delete,main


class Main:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Sign Up window")
        self.root.geometry('1000x500')
        self.root.config(bg='white')
        self.root.resizable(False,False)
        
        
       
        # FRAME PART 1 
        self.frame1=Frame(self.root,bg='white',width=500,height=500)
        self.frame1.place(x=0,y=0)
        
        # IMAGE 
        self.img = Image.open('images/icon.png').resize((350,500))
        self.imgtk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.frame1,image=self.imgtk,width=550,height=550,bg='white')
        self.imgLbl.place(x=0,y=0)
        
        # FRAME PART 2
        self.frame2=Frame(self.root,bg='white',width=500,height=500)
        self.frame2.place(x=500,y=0)
        
        
        # HEADING ---- SIGN IN 
        self.heading=Label(self.frame2,text='Sign Up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
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

        self.sign_up= Button(self.frame2,width=6,text='LogIn',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=self.login)
        self.sign_up.place(x=260,y=380)
        
        

        # MAINLOOP
        self.root.mainloop()
       
    
        
        
    
     
     # BUTTON FUNCTION WORKED AND YOU ADD (COMMAND=SELF.'NAME_FUNCTION') IN BUTTON   
    def signin(self):
        print('button clicked')
        if self.userentry.get() and self.userpass.get():
            print('data is given')
            
            
            # DATABASE TO CONNECT
            resn = database.loginAdmin((self.userentry.get(), self.userpass.get()))
            if resn :
                self.root.destroy()
                Home01.Page()
            else:
                messagebox.showwarning("Alert",'invalid username and password')
        else:
            print('enter detail')
            messagebox.showerror('Alert','Enter detail')
            
            
    # LOGIN 
    def login(self):
 
        self.root.destroy()
        login.Main()
           

if __name__=='__main__':
     Main()