from tkinter import *
from tkinter import messagebox


class FeePaymentUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Fee Payment")
        self.root.geometry("400x400")

        Label(self.root,
              text="FEE PAYMENT",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=10)

        Label(frame,text="Student ID").grid(row=0,column=0,pady=10)
        self.student_id = Entry(frame,width=25)
        self.student_id.grid(row=0,column=1)

        Label(frame,text="Course").grid(row=1,column=0,pady=10)
        self.course = Entry(frame,width=25)
        self.course.grid(row=1,column=1)

        Label(frame,text="Total Fee").grid(row=2,column=0,pady=10)
        self.total_fee = Entry(frame,width=25)
        self.total_fee.grid(row=2,column=1)

        Label(frame,text="Paid Amount").grid(row=3,column=0,pady=10)
        self.paid_amount = Entry(frame,width=25)
        self.paid_amount.grid(row=3,column=1)

        Label(frame,text="Payment Mode").grid(row=4,column=0,pady=10)
        self.payment_mode = Entry(frame,width=25)
        self.payment_mode.grid(row=4,column=1)

        btn_frame = Frame(self.root)
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Submit Payment",
               width=15,
               command=self.submit_payment).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0,column=1,padx=10)


    def submit_payment(self):

        if self.student_id.get() == "":
            messagebox.showerror("Error","Student ID required")
            return

        messagebox.showinfo("Success","Fee Payment Recorded Successfully")
        self.clear_form()


    def clear_form(self):

        self.student_id.delete(0,END)
        self.course.delete(0,END)
        self.total_fee.delete(0,END)
        self.paid_amount.delete(0,END)
        self.payment_mode.delete(0,END)


if __name__ == "__main__":
    app = FeePaymentUI()
    app.root.mainloop()