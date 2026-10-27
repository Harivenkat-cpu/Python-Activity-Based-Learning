# Food Waste Monitoring System — Easy

days = int(input("Enter number of days: "))

limit = 10

for day in range(1, days + 1):
    print("\nDay", day)

    prepared = int(input("Meals prepared: "))
    served = int(input("Meals served: "))

    leftover = prepared - served
    wastage = (leftover / prepared) * 100

    print("Leftover meals:", leftover)
    print("Wastage percentage:", wastage, "%")

    if wastage > limit:
        print("Exceeds acceptable limit")
    else:
        print("Within acceptable limit")