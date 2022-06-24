from student import Student

def printStudentData(list_of_students):
    for student in list_of_students:
        print(f"{student.getfName()} {student.getlName()}: {student.getMajor()}")
        print(f"GPA: {student.getGpa()}")
        print(f"Class: {student.getClassLevel()}")
        print(f"ID: {student.getId()}\n")
    return
def load_students(fileName):
    student_list = []
    try:
        counter = 0
        file = open(fileName, "r").readlines()
        for line in file:
            counter += 1
            if counter == 1:
                continue
            item = line.split(",")
            if len(item) != 6:
                raise Exception(f"Error: Not all fields are filled in line {counter}.")
            theStudent = Student(item[0], item[1], item[2], int(item[3]), float(item[4]),  item[5])
            student_list.append(theStudent)
    except Exception as err:
        print(err)
    return student_list

def sortList(student_list):
    student_list.sort(key=lambda theStudent: theStudent.getMajor())

def main():
    student_list = load_students("students.csv")
    printStudentData(student_list)


main()