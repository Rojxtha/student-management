with open('student_log.txt','a')as file:
    student_name=input("Enter students name:")
    student_class=input("Enter Class:")
    roll_no=input=input("Enter Roll Number:")
    student_info=f"Name:{student_name},Class:{student_class},Roll No:{roll_no}\n"
    file.write(student_info)
    print("Student information logged successfully!")
        
