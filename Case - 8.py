#Library Borrowing and Fine Reconciliation — Medium

n = int(input("Enter number of books: "))

total_fine = 0
returned_count = 0

for i in range(n):
    print("\nEnter details for book", i + 1)

    book = input("Enter book ID: ")
    allowed = int(input("Enter allowed borrowing days: "))
    actual = int(input("Enter actual borrowing days: "))

    if actual > allowed:
        delay = actual - allowed
        fine = delay * 5
        total_fine = total_fine + fine

        print("Book", book, "is overdue")
        print("Delay:", delay, "days")
        print("Fine: Rs.", fine)
    else:
        fine = 0
        returned_count = returned_count + 1

print("\nTotal Fine: Rs.", total_fine)
print("Returned Count:", returned_count)