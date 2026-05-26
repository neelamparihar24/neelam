from tkinter import *
from tkinter import ttk


class ViewCourseUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("View Courses")
        self.root.geometry("750x450")

        Label(self.root,
              text="COURSE LIST",
              font=("Arial",18,"bold")).pack(pady=10)

        # Search Section
        search_frame = Frame(self.root)
        search_frame.pack(pady=10)

        Label(search_frame,text="Search Course").grid(row=0,column=0,padx=5)

        self.search_box = Entry(search_frame,width=30)
        self.search_box.grid(row=0,column=1,padx=5)

        Button(search_frame,
               text="Search",
               width=12).grid(row=0,column=2,padx=5)

        Button(search_frame,
               text="Show All",
               width=12,
               command=self.load_courses).grid(row=0,column=3,padx=5)

        # Table Frame
        table_frame = Frame(self.root)
        table_frame.pack(pady=20)

        scroll_y = Scrollbar(table_frame)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)

        self.course_table = ttk.Treeview(
            table_frame,
            columns=("id","name","duration","fee"),
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.config(command=self.course_table.yview)
        scroll_x.config(command=self.course_table.xview)

        self.course_table.heading("id",text="Course ID")
        self.course_table.heading("name",text="Course Name")
        self.course_table.heading("duration",text="Duration")
        self.course_table.heading("fee",text="Fee")

        self.course_table["show"] = "headings"

        self.course_table.column("id",width=100)
        self.course_table.column("name",width=200)
        self.course_table.column("duration",width=150)
        self.course_table.column("fee",width=120)

        self.course_table.pack()

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=10)

        Button(btn_frame,
               text="Refresh",
               width=12,
               command=self.load_courses).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Close",
               width=12,
               command=self.root.destroy).grid(row=0,column=1,padx=10)

        # Load dummy data
        self.load_courses()


    def load_courses(self):

        # Clear table
        for row in self.course_table.get_children():
            self.course_table.delete(row)

        # Dummy Data (later from MySQL)
        courses = [
            (1,"Python Full Stack","6 Months",45000),
            (2,"Data Science","8 Months",65000),
            (3,"Web Development","4 Months",30000),
        ]

        for course in courses:
            self.course_table.insert("",END,values=course)


    def run(self):
        self.root.mainloop()


# testing
if __name__ == "__main__":
    app = ViewCourseUI()
    app.run()