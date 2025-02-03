def main():
    
    search_student("student_1")
    search_student("student_6")
    
students = ["student_1", "student_2", "student_3","student_4", "student_5"]
def search_student(name):
    
    if name in students:
        index = students.index(name)
        print(name," is present at index ",index,".")
    else:
        print(name," is not present in the list.")

if __name__=="__main__":
    main()