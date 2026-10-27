# ATM Transaction Sequence Simulation — Easy

balance = 5000
deposits = 0
withdrawals = 0
rejected = 0

n = int(input("Number of transactions: "))

for i in range(n):
    t, amount = input("Enter type and amount: ").split()
    amount = float(amount)

    if amount <= 0:
        rejected += 1
    elif t.upper() == "D":
        balance += amount
        deposits += 1
    elif t.upper() == "W":
        if amount <= 3000 and amount <= balance:
            balance -= amount
            withdrawals += 1
        else:
            rejected += 1
    else:
        rejected += 1

print("Final balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Rejected:", rejected)
