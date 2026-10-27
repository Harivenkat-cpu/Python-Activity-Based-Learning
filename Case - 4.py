#Multi-Product Price Fluctuation Analysis — Easy

n = int(input("Enter number of products: "))
threshold = float(input("Enter fluctuation threshold (%): "))

products = []
changes = []

for i in range(n):
    name = input("Enter product name: ")
    old_price = float(input("Enter old price: "))
    new_price = float(input("Enter new price: "))

    change = ((new_price - old_price) / old_price) * 100

    products.append(name)
    changes.append(change)

print("\n--- Price Fluctuation Analysis ---")

for i in range(n):
    print(products[i], ":", round(changes[i], 2), "%")

    if abs(changes[i]) > threshold:
        print("Flag: Exceeds threshold")

max_change = max(changes, key=abs)
index = changes.index(max_change)

print("\nMaximum fluctuation:", round(abs(max_change), 2), "%")
print("Product:", products[index])