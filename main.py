import json
import os


class Student:

    def __init__(self, student_id, name, age, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department
        self.marks = {}
        self.attendance = {}
        self.grade = ""

    def add_marks(self):
        print("\nEnter marks")

        

        self.marks["english"] = int(input("English: "))
        self.marks["tamil"] = int(input("Tamil: "))
        self.marks["maths"] = int(input("Maths: "))
        self.marks["science"] = int(input("Science: "))
        self.marks["social_science"] = int(input("Social Science: "))

        self.calculate_grade()

    def calculate_grade(self):
        total = sum(self.marks.values())
        average = total / len(self.marks)

        if average >= 90:
            self.grade = "A+"
        elif average >= 80:
            self.grade = "A"
        elif average >= 70:
            self.grade = "B"
        elif average >= 60:
            self.grade = "C"
        elif average >= 50:
            self.grade = "D"
        else:
            self.grade = "F"

    def add_attendance(self):
        print("\nEnter attendance")

        total_classes = int(input("Total classes: "))
        attended_classes = int(input("Attended classes: "))

        percentage = (attended_classes / total_classes) * 100

        self.attendance = {
            "total_classes": total_classes,
            "attended_classes": attended_classes,
            "percentage": percentage
        }

    def display(self):
        print("\n-------------------------")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Department :", self.department)

        print("\nMarks:")

        if self.marks:
            for subject, mark in self.marks.items():
                print(subject, ":", mark)
        else:
            print("No marks added")

        print("\nGrade:", self.grade if self.grade else "Not calculated")

        print("\nAttendance:")

        if self.attendance:
            print("Total classes    :", self.attendance["total_classes"])
            print("Attended classes :", self.attendance["attended_classes"])
            print("Percentage       :", round(self.attendance["percentage"], 2), "%")
        else:
            print("No attendance added")

        print("-------------------------")


# ------------------------------------------------
# JSON FUNCTIONS
# ------------------------------------------------


def load_data():

    if not os.path.exists("data.json"):
        return {}

    with open("data.json", "r") as file:
        return json.load(file)


def save_data(data):

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


# ------------------------------------------------
# ADD STUDENT
# ------------------------------------------------


def add_student():

    data = load_data()

    student_id = str(len(data) + 1)

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    department = input("Enter department: ")

    student = Student(
        student_id,
        name,
        age,
        department
    )

    data[student_id] = {
        "name": student.name,
        "age": student.age,
        "department": student.department,
        "marks": student.marks,
        "attendance": student.attendance,
        "grade": student.grade
    }

    save_data(data)

    print("\nStudent added successfully.")


# ------------------------------------------------
# DELETE STUDENT
# ------------------------------------------------


def delete_student():

    data = load_data()

    student_id = input("Enter student ID to delete: ")

    if student_id in data:

        del data[student_id]

        save_data(data)

        print("Student deleted successfully.")

    else:
        print("Student ID not found.")


# ------------------------------------------------
# VIEW STUDENTS
# ------------------------------------------------


def view_students():

    data = load_data()

    if not data:
        print("No students found.")
        return

    for student_id, details in data.items():

        student = Student(
            student_id,
            details["name"],
            details["age"],
            details["department"]
        )

        student.marks = details.get("marks", {})
        student.attendance = details.get("attendance", {})
        student.grade = details.get("grade", "")

        student.display()


# ------------------------------------------------
# ADD MARKS
# ------------------------------------------------


def add_marks():

    data = load_data()

    student_id = input("Enter student ID: ")

    if student_id not in data:
        print("Student ID not found.")
        return

    student_data = data[student_id]

    student = Student(
        student_id,
        student_data["name"],
        student_data["age"],
        student_data["department"]
    )

    student.marks = student_data.get("marks", {})
    student.attendance = student_data.get("attendance", {})
    student.grade = student_data.get("grade", "")

    student.add_marks()

    data[student_id]["marks"] = student.marks
    data[student_id]["grade"] = student.grade

    save_data(data)

    print("\nMarks added successfully.")
    print("Grade:", student.grade)


# ------------------------------------------------
# ADD ATTENDANCE
# ------------------------------------------------


def add_attendance():

    data = load_data()

    student_id = input("Enter student ID: ")

    if student_id not in data:
        print("Student ID not found.")
        return

    student_data = data[student_id]

    student = Student(
        student_id,
        student_data["name"],
        student_data["age"],
        student_data["department"]
    )

    student.marks = student_data.get("marks", {})
    student.attendance = student_data.get("attendance", {})
    student.grade = student_data.get("grade", "")

    student.add_attendance()

    data[student_id]["attendance"] = student.attendance

    save_data(data)

    print("\nAttendance added successfully.")


# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------


while True:

    print("\n========== STUDENT MANAGEMENT ==========")

    print("1. Add student")
    print("2. Delete student")
    print("3. View students")
    print("4. Add marks")
    print("5. Add attendance")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        delete_student()

    elif choice == "3":
        view_students()

    elif choice == "4":
        add_marks()

    elif choice == "5":
        add_attendance()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")