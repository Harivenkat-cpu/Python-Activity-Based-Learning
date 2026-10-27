# Student Performance Trend Analysis— Easy

name = input("Enter student name: ")

subjects = ["Maths", "Python", "Physics"]

exam1 = []
exam2 = []

print("Enter marks for Examination 1:")
for subject in subjects:
    mark = int(input(subject + ": "))
    exam1.append(mark)

print("Enter marks for Examination 2:")
for subject in subjects:
    mark = int(input(subject + ": "))
    exam2.append(mark)

total1 = sum(exam1)
total2 = sum(exam2)

average = total2 / len(subjects)

print("\n--- Performance Analysis ---")
print("Student:", name)

for i in range(len(subjects)):
    change = exam2[i] - exam1[i]

    if change > 0:
        print(subjects[i], "Improved by", change)
    elif change < 0:
        print(subjects[i], "Declined by", abs(change))
    else:
        print(subjects[i], "No change")

if average >= 75:
    classification = "Excellent"
elif average >= 50:
    classification = "Good"
else:
    classification = "Needs Improvement"

print("Average Marks:", average)
print("Classification:", classification)
