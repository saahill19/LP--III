def knapsack(W, wt, val, n):
    if n < 0 or W <= 0:
        return 0
    if wt[n] > W:
        return knapsack(W, wt, val, n - 1)
    else:
        return max(
            val[n] + knapsack(W - wt[n], wt, val, n - 1),
            knapsack(W, wt, val, n - 1)
        )

def solve_knapsack():
    n = int(input("Enter number of items: "))
    wt = []
    val = []
    for i in range(n):
        w = int(input(f"Enter weight of item {i+1}: "))
        v = int(input(f"Enter value of item {i+1}: "))
        wt.append(w)
        val.append(v)
    W = int(input("Enter capacity of knapsack: "))
    result = knapsack(W, wt, val, n - 1)
    print("\nMaximum value in Knapsack:", result)

if __name__ == "__main__":
    solve_knapsack()
