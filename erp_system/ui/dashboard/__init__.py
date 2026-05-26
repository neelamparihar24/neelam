from tkinter import *

class DashboardUI:
    def __init__(self):
        self.root= Tk()
        self.root.title("ERP Dashboard")
        self.root.minsize(700,500)

        Label(self.root,
              text="ERP Dashboard",
              font=("Arial", 18,"bold" )).pack(pady=20)
        frame= Frame(self.root)
        frame.pack(pady=40)

        Button(frame,text="Student Module", width=20,height=2).grid(row=0, column=0, padx=10,pady=10)
        Button(frame,text="Employee Module", width=20,height=2).grid(row=0, column=1, padx=10,pady=10)
        Button(frame,text="Course Module", width=20,height=2).grid(row=1, column=0, padx=10,pady=10)
        Button(frame,text="Fee Module", width=20,height=2).grid(row=1, column=1, padx=10,pady=10)
        Button(frame,text="Attendance Module", width=20,height=2).grid(row=2, column=0, padx=10,pady=10)
        Button(frame,text="Reports Module", width=20,height=2).grid(row=2, column=1, padx=10,pady=10)
    def run(self):
        self.root.mainloop()