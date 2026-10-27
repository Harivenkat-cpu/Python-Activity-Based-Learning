# Retail Billing with Multiple Discount Rules — Medium

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0
items = []

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    item_total = price * quantity

    if category.lower() == "electronics":
        tax_rate = 18
    elif category.lower() == "clothing":
        tax_rate = 5
    elif category.lower() == "food":
        tax_rate = 2
    else:
        tax_rate = 0

    tax = item_total * tax_rate / 100

    subtotal += item_total
    total_tax += tax

    items.append([name, quantity, item_total, tax])

if subtotal >= 5000:
    discount = subtotal * 10 / 100

    if discount > 500:
        discount = 500
else:
    discount = 0

final_bill = subtotal + total_tax - discount

print("\n--- ITEMIZED INVOICE ---")

for item in items:
    print(item[0], "Qty:", item[1],
          "Price:", item[2],
          "Tax:", item[3])

print("\nSubtotal:", subtotal)
print("Total Tax:", total_tax)
print("Discount:", discount)
print("Final Bill:", final_bill)