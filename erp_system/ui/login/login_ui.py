from tkinter import * 
from tkinter import messagebox
from ui.dashboard.dashboard_ui import DashboardUI

class LoginUI:
    def __init__(self):
        self.root= Tk()
        self.root.title("ERP Login")
        self.root.minsize(400,300)
        self.root.resizable(False, False)

        Label(self.root,text= "ERP System Login" , 
              font=("Arial",16,"bold"),fg="black",bg="pink").pack(pady=20)
        
        Label(self.root, text="username",fg="black",bg="orange").pack()

        self.username= Entry(self.root, width=30)
        self.username.pack(pady=5)

        Label(self.root, text="password",fg="black",bg="orange").pack()
        self.password= Entry(self.root, width=30)
        self.password.pack(pady=5)

        Button(self.root,
               text="login",
               width= 20,
               fg="black",
               bg="orange",
               command=self.login).pack(pady=20)
    def login(self):
        uname= self.username.get()
        pwd= self.password.get()

        if uname== "admin" and pwd== "1234":
            messagebox.showinfo("success", "login successful") 

            self.root.destroy()

            dashboard= DashboardUI()
            dashboard.run()
        else:
            messagebox.showerror("Error", "Invalid Login")

    def run(self):
        self.root.mainloop()