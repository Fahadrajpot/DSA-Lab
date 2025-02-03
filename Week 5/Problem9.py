def main():
    add_student("studetn_1")
    add_student("student_2")
    add_student("student_3")
    display_students()
    remove_student("student__4")
    display_students()
students = []
def add_student(name):
    students.append(name)
    print(name," has been added to the list.")

def remove_student(name):
    if name in students:
        students.remove(name)
        print(name," has been removed from the list.")
    else:
        print(name," is not in the list.")

def display_students():
    if students:
        print("List of students:")
        for student in students:
            print(student)
    else:
        print("The list is empty.")


if __name__=="__main__":
    main()
