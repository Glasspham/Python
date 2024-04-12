def triangle(n):
    for x in range(1, n + 1):
        print((" " * (n - x)) + ("*" * x))
triangle(5)
