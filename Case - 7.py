#Multi-Stage Examination Eligibility System — Medium

attendance = float(input("Enter attendance percentage: "))
lab = input("Laboratory completed? (yes/no): ")
internal = float(input("Enter internal assessment marks: "))
fees = input("Fees cleared? (yes/no): ")

eligible = True

print("\nUnmet Requirements:")

if attendance < 75:
    print("- Minimum attendance of 75% is required")
    eligible = False

if lab.lower() != "yes":
    print("- Laboratory work must be completed")
    eligible = False

if internal < 40:
    print("- Minimum internal assessment mark is 40")
    eligible = False

if fees.lower() != "yes":
    print("- Fees must be cleared")
    eligible = False

if eligible:
    print("\nStudent is Eligible for the Final Examination")
else:
    print("\nStudent is Not Eligible for the Final Examination")