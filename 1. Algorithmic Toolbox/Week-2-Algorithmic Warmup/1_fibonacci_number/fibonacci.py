# Uses python3
# 2-1: Fibonacci Number

def calc_fib(n):
    z = []
    z.append(0)
    z.append(1)

    if n <= 1:
        return n

    else:
        for x in range(2, n + 1):
            z.append(z[x - 1] + z[x - 2])

        return z[-1]


n = int(input())
print(calc_fib(n))
