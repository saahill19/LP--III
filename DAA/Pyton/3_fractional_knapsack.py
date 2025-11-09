def fractional_knapsack():
    n = int(input("Enter number of items: "))
    weights = []
    values = []

    for i in range(n):
        w = float(input(f"Enter weight of item {i+1}: "))
        v = float(input(f"Enter value of item {i+1}: "))
        weights.append(w)
        values.append(v)

    capacity = float(input("Enter knapsack capacity: "))

    res = 0.0
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)

    for weight, value in items:
        if capacity <= 0:
            break
        if weight > capacity:
            res += capacity * (value / weight)
            capacity = 0
        else:
            res += value
            capacity -= weight

    print(f"Maximum Profit in Knapsack: {res}")

if __name__ == "__main__":
    fractional_knapsack()
