def fibonacci(n):
    if n == 1:
        return (n, 0)
    else:
        (i, j) = fibonacci(n - 1)
        return (i + j, i)

f = fibonacci(8)
print(f)
