#Student Academic Risk Classification — Hard

n = int(input("Enter number of students: "))

names = []
marks = []
attendance = []
lab = []

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    m = int(input("Enter marks: "))
    a = float(input("Enter attendance: "))
    l = int(input("Enter lab score: "))

    names.append(name)
    marks.append(m)
    attendance.append(a)
    lab.append(l)

for i in range(n):
    risk = 0
    factors = []

    if marks[i] < 40:
        risk += 1
        factors.append("Marks")

    if attendance[i] < 75:
        risk += 1
        factors.append("Attendance")

    if lab[i] < 40:
        risk += 1
        factors.append("Lab")

    if risk >= 2:
        category = "High Risk"
    elif risk == 1:
        category = "Medium Risk"
    else:
        category = "Low Risk"

    print("\nName:", names[i])
    print("Risk Category:", category)

    if risk > 0:
        print("Risk Factors:", factors)
    else:
        print("Risk Factors: None")