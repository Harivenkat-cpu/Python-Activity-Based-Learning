# : Fuel Consumption and Route Comparison — Medium

distance = float(input("Distance (km): "))
fuel_price = float(input("Fuel price: "))

vehicles = ["CarA", "CarB", "CarC"]
mileage = [15, 18, 12]
available = [30, 35, 50]

best = ""
min_cost = float("inf")

for i in range(3):
    fuel = distance / mileage[i]
    required = fuel * 1.10
    cost = required * fuel_price

    print(vehicles[i], "required fuel:", round(required, 2),
          "cost:", round(cost, 2))

    if required <= available[i] and cost < min_cost:
        min_cost = cost
        best = vehicles[i]

print("Lowest-cost feasible vehicle:", best)