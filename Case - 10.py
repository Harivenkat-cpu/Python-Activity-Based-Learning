#Integrated Student Record Consistency Checker — Hard

n = int(input("Enter number of students: "))

ids = []
names = []
marks = []
attendance = []
courses = []

for i in range(n):
    print("\nStudent", i + 1)

    sid = input("Enter student ID: ")
    name = input("Enter name: ")
    mark = float(input("Enter marks: "))
    attend = float(input("Enter attendance: "))
    course = input("Enter course: ")

    ids.append(sid)
    names.append(name)
    marks.append(mark)
    attendance.append(attend)
    courses.append(course)

print("\n--- Consistency Check ---")

for i in range(n):
    error = False

    if ids[i] == "" or names[i] == "" or courses[i] == "":
        print("Student", i + 1, ": Missing value")
        error = True

    if ids.count(ids[i]) > 1:
        print("Student", i + 1, ": Duplicate ID")
        error = True

    if marks[i] < 0 or marks[i] > 100:
        print("Student", i + 1, ": Invalid marks")
        error = True

    if attendance[i] < 0 or attendance[i] > 100:
        print("Student", i + 1, ": Invalid attendance")
        error = True

    if error == False:
        print("Student", i + 1, ": Record is consistent")