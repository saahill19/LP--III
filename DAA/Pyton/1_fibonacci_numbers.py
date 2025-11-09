def fibonacci_iterative(n):
    if n <= 0:
        return [], 0
    elif n == 1:
        return [0], 0
    elif n == 2:
        return [0, 1], 0
    fib = [0, 1]
    steps = 0
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
        steps += 1
    return fib, steps

if __name__ == "__main__":
    n = int(input("Enter number of terms in Fibonacci sequence: "))
    sequence, step_count = fibonacci_iterative(n)
    print(f"\nFibonacci sequence up to {n} terms:")
    print(sequence)
    print(f"\nStep count (number of additions performed): {step_count}")