from tkinter import *
from tkinter import messagebox
from threading import *
import mysql.connector
from datetime import datetime
import time

mylock = RLock()

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="neelam24",
        database="busdb")

class Bus:
    def __init__(self, bus_name, mylock):
        self.bus_name = bus_name
        self.mylock = mylock

    def reserve(self, customer_name, gender, mobile, need_seats):
        conn = get_connection()
        cursor = conn.cursor()

        self.mylock.acquire()

        try:
            conn.start_transaction()
            
            cursor.execute(
                "SELECT avail_seat FROM Bus_Details WHERE bus_name=%s FOR UPDATE",
                (self.bus_name,)
            )

            result = cursor.fetchone()

            if result:
                avail_seat = result[0]

                print(f"\nAvailable seats: {avail_seat}")

                if avail_seat >= need_seats:

                    tname = current_thread().name
                    print(f"{need_seats} seat(s) booked for {customer_name} by {tname}")

                    time.sleep(1)

                    new_seats = avail_seat - need_seats

                    cursor.execute(
                        "UPDATE Bus_Details SET avail_seat=%s WHERE bus_name=%s",
                        (new_seats, self.bus_name))
                    
                    booking_time = datetime.now()

                    cursor.execute("""
                        INSERT INTO bookings
                        (customer_name, gender, mobile, bus_name, seats_booked, booking_time)
                        VALUES (%s, %s, %s, %s, %s, %s)""",
                        (customer_name,gender,mobile,self.bus_name,need_seats,booking_time))

                    conn.commit()

                    print("Booking Successful")
                    print(f"Seats Left: {new_seats}")
                    clear_fields()

                else:
                    print(f"Sorry {customer_name}, seats are full")
                    conn.rollback()

        except Exception as e:
            conn.rollback()
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()
            self.mylock.release()

def clear_fields():
    name_entry.delete(0, END)
    mobile_entry.delete(0, END)
    seats_entry.delete(0, END)

    gender_var.set("")
    bus_var.set("HansTravels")

def book_ticket():
    customer_name = name_entry.get()
    gender = gender_var.get()
    mobile = mobile_entry.get()
    seats = seats_entry.get()
    bus_name = bus_var.get()

    if customer_name == "" or gender == "" or mobile == "" or seats == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    try:
        seats = int(seats)
    except:
        messagebox.showerror("Error", "Seats must be a number")
        return

    b1 = Bus(bus_name, mylock)

    t1 = Thread(
        target=b1.reserve,
        args=(customer_name, gender, mobile, seats))
    t1.start()

root = Tk()
root.title("Bus Ticket Booking System")
root.geometry("500x500")
root.config(bg="lightblue")

heading = Label(
    root,
    text="Bus Ticket Booking System",
    font=("Arial", 20, "bold"),
    bg="lightblue",
    fg="darkblue")

heading.pack(pady=20)

Label(root, text="Customer Name", font=("Arial", 12), bg="lightblue").pack()
name_entry = Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

Label(root, text="Gender", font=("Arial", 12), bg="lightblue").pack()
gender_var = StringVar()

gender_menu = OptionMenu(root, gender_var, "Male", "Female", "Other")
gender_menu.config(font=("Arial", 11), width=20)
gender_menu.pack(pady=5)

Label(root, text="Mobile Number", font=("Arial", 12), bg="lightblue").pack()
mobile_entry = Entry(root, font=("Arial", 12), width=30)
mobile_entry.pack(pady=5)

Label(root, text="Select Bus", font=("Arial", 12), bg="lightblue").pack()

bus_var = StringVar()
bus_var.set("HansTravels")

bus_menu = OptionMenu(root, bus_var, "HansTravels", "VRL", "OrangeTravels")
bus_menu.config(font=("Arial", 11), width=20)
bus_menu.pack(pady=5)

Label(root, text="Number of Seats", font=("Arial", 12), bg="lightblue").pack()
seats_entry = Entry(root, font=("Arial", 12), width=30)
seats_entry.pack(pady=5)

book_btn = Button(
    root,
    text="Book Ticket",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    padx=10,
    pady=5,
    command=book_ticket
)
book_btn.pack(pady=20)

root.mainloop()