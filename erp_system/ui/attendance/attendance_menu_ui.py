from tkinter import *

from ui.attendance.mark_attendance_ui import MarkAttendanceUI
from ui.attendance.attendance_report_ui import AttendanceReportUI


class AttendanceMenuUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Attendance Module")
        self.root.geometry("400x300")

        Label(self.root,
              text="ATTENDANCE MANAGEMENT",
              font=("Arial",18,"bold")).pack(pady=30)

        frame = Frame(self.root)
        frame.pack(pady=20)

        Button(frame,
               text="Mark Attendance",
               width=20,
               height=2,
               command=self.open_mark_attendance).grid(row=0,column=0,padx=10,pady=10)

        Button(frame,
               text="Attendance Report",
               width=20,
               height=2,
               command=self.open_attendance_report).grid(row=0,column=1,padx=10,pady=10)


    def open_mark_attendance(self):
        MarkAttendanceUI()

    def open_attendance_report(self):
        AttendanceReportUI()