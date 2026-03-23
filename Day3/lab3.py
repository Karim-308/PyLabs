from statistics import mean

def create_files():
    student_file = open("students.txt", "w")
    students_list = ["Karim", "Basem", "Ahmed Saleh", "Andrew"]
    for i in range(len(students_list)):
        student_file.write(str(i + 1) + "," + students_list[i] + "\n")
    student_file.close()

    grades_file = open("grades.txt", "w")
    course_grades = [[1, "python", 90], [2, "python", 80], [3, "python", 70], [4, "python", 60],[1, "java", 80], [2, "java", 70], [3, "java", 60], [4, "java", 50],[1, "c++", 70], [2, "c++", 60], [3, "c++", 50], [4, "c++", 40]]
    
    for grade in course_grades:
        grades_file.write(str(grade[0]) + "," + grade[1] + "," + str(grade[2]) + "\n")
    grades_file.close()


def display_student_names():
    try:
        student_file = open("students.txt", "r")
    except FileNotFoundError:
        print("students.txt file not found")
        return

    lines = student_file.readlines()
    student_file.close()

    if len(lines) == 0:
        print("There are no students")
        return

    for line in lines:
        id, student_name = line.strip().split(",")
        print(f"Student {id} {student_name}")

    print("\n")


def display_python_grades():
    try:
        grades_file = open("grades.txt", "r")
    except FileNotFoundError:
        print("There are no grades")
        return

    lines = grades_file.readlines()
    grades_file.close()

    if len(lines) == 0:
        print("There are no grades")
        return

    print("Python course grades:-\n")

    for line in lines:
        id, course, grade = line.strip().split(",")
        if course == "python":
            print(f"Student {id}: {grade}")
    print("\n")

def display_student_info(student_id):
    try:
        student_file = open("students.txt", "r")
    except FileNotFoundError:
        print("There are no students")
        return

    student_lines = student_file.readlines()
    student_file.close()

    try:
        grades_file = open("grades.txt", "r")
    except FileNotFoundError:
        print("There are no grades")
        return

    grade_lines = grades_file.readlines()
    grades_file.close()

    for line in student_lines:
        id, student_name = line.strip().split(",")
        if id == student_id:
            print(f"Student {id}: {student_name} Report:\n")

    for line in grade_lines:
        id, course_name, grade = line.strip().split(",")
        if id == student_id:
            print(f"Course {course_name}: {grade}")

    print("\n")


def find_avg_grade(student_id):
    try:
        student_file = open("students.txt", "r")
    except FileNotFoundError:
        print("There are no students")
        return

    student_lines = student_file.readlines()
    student_file.close()

    try:
        grades_file = open("grades.txt", "r")
    except FileNotFoundError:
        print("There are no grades")
        return

    grade_lines = grades_file.readlines()
    grades_file.close()

    for line in student_lines:
        id, student_name = line.strip().split(",")
        if id == student_id:
            print(f"Student {id} {student_name} Average Grade:")

    student_grades = []
    for line in grade_lines:
        id, course_name, grade = line.strip().split(",")
        if id == student_id:
            student_grades.append(int(grade))

    if len(student_grades) > 0:
        print(f"Student {student_id} Average Grade: {mean(student_grades)}")
    else:
        print(f"No grades found for student {student_id}")


create_files()
print("Available students")
display_student_names()
display_python_grades()
print("\nStudent report\n")
student_id = input("Enter student id ")
display_student_info(student_id)
find_avg_grade(student_id)
