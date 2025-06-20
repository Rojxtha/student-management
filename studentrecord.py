from student_management import(
    add_student_record, update_student_record,
    view_student_record, delete_student
)
     
def menu():
    run=True
    while run:
        print("Enter 1 to add student")
        print("Enter 2 to view student details")
        print("Enter 3 to update student")
        print("Enter 4 to delete student")
        print("Enter 5 to take student")
        print("Enter 6 to view student")
        print("Enter 8 to end")
        option=input()
        if option=="1":
            add_student_record()
        elif option=="2":
            view_student_record()
        elif option=="3":
            update_student_record()
        else:
            print("Invalid choices")
menu()
