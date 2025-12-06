class Student:
    def __init__(self, id=None, name=None, dob=None):
        self.__id = id
        self.__name = name
        self.__dob = dob
    
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getDOB(self):
        return self.__dob
    
    def input(self):
        id, name, dob = [x.strip() for x in input().split(",")]
        self.__id = id
        self.__name = name
        self.__dob = dob
    
    def getInfo(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}")
    

class Course:
    def __init__(self, id=None, name=None):
        self.__id = id
        self.__name = name
        self.__marks = []

    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def input(self):
        id, name = [x.strip() for x in input().split(",")]
        self.__id = id
        self.__name = name
    
    def getInfo(self):
        print(f"ID: {self.__id}, Name: {self.__name}")
    
    def inputMarks(self, students):
        print(f"Input mark of courses {self.__name}:")
        marks = []
        for i, student in enumerate(students):
            mark = input(f"{i+1}. ID: {student.getID()}, Name: {student.getName()}: ")
            marks.append(float(mark))
        self.__marks = marks
    
    def showMarks(self, students):
        print(f"Mark of courses {self.__name}:\n")
        for i, student in enumerate(students):
            if i < len(self.__marks):
                print(f"{i + 1}. ID: {student.getID()}, Name: {student.getName()}, Mark: {self.__marks[i]}")
    
    def setMarks(self, marks):
        self.__marks = marks


class studentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
    
    def inputStudents(self):
        student_number = int(input("Input number of students: "))
        self.__students = []
        
        for i in range(student_number):
            print(f"\nInput student {i+1} information (id, name, DoB):")
            student = Student()
            student.input()
            self.__students.append(student)
    
    def addStudent(self):
        student_number = int(input("Input number of students: "))
        currIdx = len(self.__students)
        for i in range(student_number):
            print(f"\nInput student {i+currIdx+1} information (id, name, DoB):")
            student = Student()
            student.input()
            self.__students.append(student)
    
    def inputCourses(self):
        course_number = int(input("\nInput number of courses: "))
        self.__courses = []
        
        for i in range(course_number):
            print(f"\nInput course {i+1} information (id, name):")
            course = Course()
            course.input()
            self.__courses.append(course)

    def addCourse(self):
        course_number = int(input("\nInput number of courses: "))
        currIdx = len(self.__courses)
        
        for i in range(course_number):
            print(f"\nInput course {i+currIdx+1} information (id, name):")
            course = Course()
            course.input()
            self.__courses.append(course)

    def listStudents(self):
        print("\nStudents list:")
        for i, student in enumerate(self.__students):
            print(f"{i+1}. ", end="")
            student.getInfo()
    
    def listCourses(self):
        print("\nAvailable courses:")
        for i, course in enumerate(self.__courses):
            print(f"{i}. ", end="")
            course.getInfo()
    
    def inputMarks(self):
        course_id = input("\nEnter course id: ")
        for course in self.__courses:
            if course.getID() == course_id:
                course.inputMarks(self.__students)
                return
        print("Course not found!")
    
    def showMarks(self):
        course_id = input("\nEnter course id: ")
        for course in self.__courses:
            if course.getID() == course_id:
                course.showMarks(self.__students)
                return
        print("Course not found!")
    
    def display(self):
        print("\n----------")
        print("1. List Students")
        print("2. List Courses")
        print("3. Add Students")
        print("4. Add Courses")
        print("5. Input Student mark")
        print("6. Show Student mark")
        print("7. Exit")
        print("----------")
    
    def start(self):
        self.inputStudents()
        self.inputCourses()
        
        while True:
            self.display()
            choice = int(input("Your choice: "))
            if choice == 1:
                self.listStudents()
            elif choice == 2:
                self.listCourses()
            elif choice == 3:
                self.addStudent()
            elif choice == 4:
                self.addCourse()
            elif choice == 5:
                self.inputMarks()
            elif choice == 6:
                self.showMarks()
            else:
                break


def main():
    management = studentMarkManagement()
    management.start()


if __name__ == "__main__":
    main()
