from tkinter import *
from tkinter import ttk


class FeeReportUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Fee Report")
        self.root.geometry("800x450")

        Label(self.root,
              text="FEE REPORT",
              font=("Arial",18,"bold")).pack(pady=10)

        # Search Section
        search_frame = Frame(self.root)
        search_frame.pack(pady=10)

        Label(search_frame,text="Search Student").grid(row=0,column=0,padx=5)

        self.search_box = Entry(search_frame,width=30)
        self.search_box.grid(row=0,column=1,padx=5)

        Button(search_frame,
               text="Search",
               width=12).grid(row=0,column=2,padx=5)

        Button(search_frame,
               text="Show All",
               width=12,
               command=self.load_data).grid(row=0,column=3,padx=5)

        # Table
        table_frame = Frame(self.root)
        table_frame.pack(pady=20)

        scroll_y = Scrollbar(table_frame)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)

        self.fee_table = ttk.Treeview(
            table_frame,
            columns=("student_id","course","total_fee","paid","balance"),
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.config(command=self.fee_table.yview)
        scroll_x.config(command=self.fee_table.xview)

        self.fee_table.heading("student_id",text="Student ID")
        self.fee_table.heading("course",text="Course")
        self.fee_table.heading("total_fee",text="Total Fee")
        self.fee_table.heading("paid",text="Paid Amount")
        self.fee_table.heading("balance",text="Balance")

        self.fee_table["show"] = "headings"

        self.fee_table.column("student_id",width=120)
        self.fee_table.column("course",width=150)
        self.fee_table.column("total_fee",width=120)
        self.fee_table.column("paid",width=120)
        self.fee_table.column("balance",width=120)

        self.fee_table.pack()

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=10)

        Button(btn_frame,
               text="Refresh",
               width=12,
               command=self.load_data).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Close",
               width=12,
               command=self.root.destroy).grid(row=0,column=1,padx=10)

        self.load_data()


    def load_data(self):

        for row in self.fee_table.get_children():
            self.fee_table.delete(row)

        # Dummy data (replace with DB later)
        data = [
            (101,"Python Full Stack",45000,20000,25000),
            (102,"Data Science",65000,40000,25000),
            (103,"Web Development",30000,30000,0)
        ]

        for row in data:
            self.fee_table.insert("",END,values=row)


if __name__ == "__main__":
    app = FeeReportUI()
    app.root.mainloop()