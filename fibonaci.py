def fib(n):
    c = []
    if n > 0:
        a = 0
        b = 1
        c.append(a)
        c.append(b)
        for i in range(1, n):
            c.append(c[i-1] + c[i])
        return c
    else:
        print("Not a valid Number")


result = fib(100)

print(result)
