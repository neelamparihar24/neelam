from tkinter import *
from tkinter import messagebox


class AddCourseUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Add Course")
        self.root.geometry("400x350")

        Label(self.root,
              text="ADD COURSE",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=10)

        Label(frame,text="Course Name").grid(row=0,column=0,pady=10)
        self.course_name = Entry(frame,width=25)
        self.course_name.grid(row=0,column=1)

        Label(frame,text="Duration").grid(row=1,column=0,pady=10)
        self.duration = Entry(frame,width=25)
        self.duration.grid(row=1,column=1)

        Label(frame,text="Fee").grid(row=2,column=0,pady=10)
        self.fee = Entry(frame,width=25)
        self.fee.grid(row=2,column=1)

        Button(self.root,
               text="Add Course",
               width=20,
               command=self.add_course).pack(pady=20)


    def add_course(self):

        name = self.course_name.get()
        duration = self.duration.get()
        fee = self.fee.get()

        if name == "" or duration == "" or fee == "":
            messagebox.showerror("Error","All fields required")
            return

        messagebox.showinfo("Success","Course Added Successfully")

        self.clear_form()


    def clear_form(self):
        self.course_name.delete(0,END)
        self.duration.delete(0,END)
        self.fee.delete(0,END)


    def run(self):
       self.root.mainloop()


# testing purpose
if __name__ == "__main__":
    app = AddCourseUI()
    app.run()