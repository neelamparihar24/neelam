from tkinter import *
from tkinter import messagebox


class UpdateCourseUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Update Course")
        self.root.geometry("400x400")

        Label(self.root,
              text="UPDATE COURSE",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=10)

        Label(frame,text="Course ID").grid(row=0,column=0,pady=10)
        self.course_id = Entry(frame,width=25)
        self.course_id.grid(row=0,column=1)

        Button(frame,
               text="Search",
               command=self.search_course).grid(row=0,column=2,padx=5)

        Label(frame,text="Course Name").grid(row=1,column=0,pady=10)
        self.course_name = Entry(frame,width=25)
        self.course_name.grid(row=1,column=1)

        Label(frame,text="Duration").grid(row=2,column=0,pady=10)
        self.duration = Entry(frame,width=25)
        self.duration.grid(row=2,column=1)

        Label(frame,text="Fee").grid(row=3,column=0,pady=10)
        self.fee = Entry(frame,width=25)
        self.fee.grid(row=3,column=1)

        btn_frame = Frame(self.root)
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Update",
               width=12,
               command=self.update_course).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=12,
               command=self.clear_form).grid(row=0,column=1,padx=10)


    def search_course(self):

        course_id = self.course_id.get()

        if course_id == "":
            messagebox.showerror("Error","Enter Course ID")
            return

        # Dummy data (later from DB)
        self.course_name.insert(0,"Python Full Stack")
        self.duration.insert(0,"6 Months")
        self.fee.insert(0,"45000")


    def update_course(self):

        if self.course_id.get() == "":
            messagebox.showerror("Error","Course ID required")
            return

        messagebox.showinfo("Success","Course Updated Successfully")


    def clear_form(self):

        self.course_id.delete(0,END)
        self.course_name.delete(0,END)
        self.duration.delete(0,END)
        self.fee.delete(0,END)


if __name__ == "__main__":
    app = UpdateCourseUI()
    app.root.mainloop()