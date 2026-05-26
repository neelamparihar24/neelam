from tkinter import *
from tkinter import messagebox


class DeleteCourseUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Delete Course")
        self.root.geometry("350x250")

        Label(self.root,
              text="DELETE COURSE",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=20)

        Label(frame,text="Course ID").grid(row=0,column=0,pady=10)

        self.course_id = Entry(frame,width=25)
        self.course_id.grid(row=0,column=1)

        btn_frame = Frame(self.root)
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Delete",
               width=12,
               command=self.delete_course).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=12,
               command=self.clear_form).grid(row=0,column=1,padx=10)


    def delete_course(self):

        course_id = self.course_id.get()

        if course_id == "":
            messagebox.showerror("Error","Enter Course ID")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this course?"
        )

        if confirm:
            messagebox.showinfo("Success","Course Deleted Successfully")
            self.clear_form()


    def clear_form(self):
        self.course_id.delete(0,END)


if __name__ == "__main__":
    app = DeleteCourseUI()
    app.root.mainloop()