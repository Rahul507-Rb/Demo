

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import database, register,edit_delete,main

class daily():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Today tasks')

        self.root.resizable(height=False,width=False)
        
        self.root.geometry('1200x400')
        
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=25, width="1200", height="500")

       # self.tr = Treeview(self.fr, columns=('id','name', 'username','password', 'edit', 'delete'), show='headings')
        self.tr = Treeview(self.fr, columns=('name', 'username','edit', 'delete'), show='headings')

       # self.tr.heading('id', text="ID")
        
        self.tr.heading('name', text="User's Name")
        
        self.tr.heading('username', text="Username")
        
       # self.tr.heading('password', text="password")
        
        
        
        
        self.tr.heading('edit', text="edit")

        self.tr.heading('delete', text="delete")

        data = database.getUsers()
        print('all users are ', data)

        for i in data:
            print(i)
           # self.tr.insert('', 0, text = i[0], values=(i[3],i[1], i[0],i[2], 'Edit', 'Delete'))
            self.tr.insert('', 0, text = i[0], values=(i[1],i[2], 'Edit', 'Delete'))


        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.pack()
        self.root.mainloop() 

    
        
    def actions(self,e):
        # print("i am e",e)
        # get the values of the selected rows\\
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'cols {col}')
        # print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )

        x = self.tr.item(tt)
        print("i am gup",gup, col)
        if col == '#6':
            res = messagebox.askyesno("Delete", "Do You Realy Want to delete this item.")
            if res:
                a = database.delUser(gup)
                if a:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    daily()
                else:
                    messagebox.showerror('Alert', 'Data deleted successfully.')

        
        if col == '#5':
            # self.root.destroy()
            print('edit is called')
            self.root.destroy()
            #register.Main(x)
            main.Main(x)
   
if __name__ == '__main__':
    obj = daily()
