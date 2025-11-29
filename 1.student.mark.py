def listCourses(courses):
    print("Available courses:")
    for i, course in enumerate(courses):
        print(f"{i}. ID: {course["id"]}, Name: {course["name"]}")
    print("\n")

def listStudents(students):
    print("Students list:")
    for i, student in enumerate(students):
        print(f"{i+1}. ID: {student["id"]}, Name: {student["name"]}, DoB: {student["DoB"]}")
    print("\n")


def inputMark(students, courses, coursesIdx):
    print(f"Input mark of courses {courses[coursesIdx]["name"]}:")
    marks = []
    for i, student in enumerate(students):
        mark = input(f"\n{i + 1}. ID: {student["id"]}, Name: {student["name"]}: ")
        marks.append(int(mark))
    return marks

def showMarks(students, courses, coursesIdx):
    print(f"Mark of courses {courses[coursesIdx]["name"]}:\n")
    marks = courses[coursesIdx]["marks"]
    for i, student in enumerate(students):
        print(f"{i + 1}. ID: {student["id"]}, Name: {student["name"]}, Mark: {marks[i]}")

def display():
    print("----------")
    print("1. List Students")
    print("2. List Courses")
    print("3. Input Student mark")
    print("4. Show Student mark")
    print("5. Exit")
    print("----------")

def main():
    studentNubmer = int(input("Input number of students: "))

    students = []
    courses = []

    for i in range(0,studentNubmer):
        print(f"\nInput student {i+1} information (id, name, DoB):")
        id, name, DoB = [x for x in input().split(", ")]
        students.append({
                        "id": id,
                        "name": name,
                        "DoB" : DoB
                        })

    courseNubmer = int(input("\nInput number of courses: "))

    for i in range(0,courseNubmer):
        print(f"\nInput course {i+1} information (id, name,):")
        id, name = [x for x in input().split(",")]
        courses.append({
                        "id": id,
                        "name": name
                        })

        while True:
            display()
            choice = int(input("\nYour choice: "))
            if choice == 1:
                listStudents(students)
            elif choice == 2:
                listCourses(courses)
            elif choice == 3:
                courseID = input(("\nEnter course id: "))
                for i, course in enumerate(courses):
                    if course["id"] in courseID:
                        courseIdx = i
                marks = inputMark(students, courses, courseIdx)
                courses[courseIdx]["marks"] = marks
            elif choice == 4:
                courseID = input(("\nEnter course id: "))
                for i, course in enumerate(courses):
                    if course["id"] in courseID:
                        courseIdx = i
                showMarks(students, courses, courseIdx)
            else:
                break

main()