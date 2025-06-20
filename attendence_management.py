from datetime import date
import os

def take_attendence():
    with open("student.txt","r")as file:
        student_data= file.readlines()
        student_attendance=[]
        for student in student_data:
            student = student.strip()
            roll = student.split(",")[0]
            name = student.split(",") [1]
            while True:
                print(roll, name)
                attendence= input("Present (y/n)").lower()
                if attendence == "y" or attendence =="n":
                    student_attendance.append(f"{roll},name{name},{attendence}\n")
                    break
                else:
                    print("Invalid Input")
        with open(f"attendence/{date.today()}.txt","w")as file:
            file.writelines(student_attendance)

    

def view_attendance():
    date_input= input("Enter Data (yyyy-mm-dd) to View Attendance")
    if os.path.exists(f"attencance/{date_input}.txt"):
        with open(f"attendeance/{date_input}.txt","r")as file:
            attendance_data= file.readlines()
            for attendance in attendance_data:
                print(attendance.strip)
            
    else:
        print("file does not exist")
