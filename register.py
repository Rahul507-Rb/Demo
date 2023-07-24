
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import home, database, edit_delete,main
# create root window
# place the widgets
# place the window in a loop

class Main:
    def __init__(self, data = None):
        print('data is ', data)
        self.type = 'Add'
        if data is not None:
            self.type = 'Edit'

        self.data = data

        self.root = Tk()
        self.root.title('Main Window')
        self.root.geometry('600x500')

        self.root.config(bg = '#301934')
        self.root.resizable(False, False)

        self.frame1 = Frame(self.root, width=250, height=500, bg = 'orange')

        self.frame1.place(x = 0, y= 0)

        self.img = Image.open('icon.png').resize((250, 500))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.frame1, image = self.imgTk)
        self.imgLbl.place(x = 0, y = 0)

        self.frame2 = Frame(self.root, width=350, height=500, bg = '#301934')
        self.frame2.place(x = 250, y=  0)

        self.nameLbl = Label(self.frame2, text = 'Name', bg = "#301934", fg = 'white', font = ('sans-serif', 20, 'bold'))
        self.nameLbl.place(x = 20, y = 40)

        self.nameEntry = Entry(self.frame2)
        self.nameEntry.place(x = 180, y = 45)

        self.userLbl = Label(self.frame2, text = 'Username', bg = "#301934", fg = 'white', font = ('sans-serif', 20, 'bold'))
        # self.userLbl.pack()
        self.userLbl.place(x = 20, y = 75)

        self.userentry = Entry(self.frame2)
        self.userentry.place(x = 180, y = 80)

        self.passLbl = Label(self.frame2, text = 'Password', bg = "#301934", fg = 'white', font = ('sans-serif', 20, 'bold'))
        # self.passLbl.pack()
        self.passLbl.place(x = 20, y = 120)

        self.userpass = Entry(self.frame2, show = '*')
        self.userpass.place(x = 180, y = 125)

        self.registerBtn = Button(self.frame2, text = 'Register', command=self.register)
        self.registerBtn.place(x = 90, y = 160)

        if self.type == 'Edit':
            # insert the details in entry widgets
            d = self.data.get('values')
            print('d is ', d)
            self.userentry.insert(0, d[0])
            self.userpass.insert(0, d[1])
            self.nameEntry.insert(0,d[2])

        self.root.mainloop()

    
    def register(self):
        if self.userentry.get() and self.userpass.get()  and self.nameEntry() :
            if self.type == 'Edit':
                res = database.updateUser((self.userentry.get(), self.userpass.get(), self.data.get('text')))
                if res:
                    messagebox.showinfo('Success', 'Details updated successfully.')
                    self.root.destroy()
                    edit_delete.obj ()#.daily()
                else:
                    messagebox.showerror('Alert', 'Something went wrong.')
            else:
                res = database.registerUser((self.userentry.get(), self.userpass.get(), self.nameEntry.get()))
                if res:
                    messagebox.showinfo('Success', 'User registered successfully.')
                else:
                    messagebox.showerror('Alert', 'Something went wrong.')
        else:
            messagebox.showerror('Alert', 'Please enter your details.')

if __name__ == '__main__':
    Main()
