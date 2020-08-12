# Uses python3
# 2-5: Fibonacci Number Again

import sys

def get_fibonacci_huge_naive(n, k):
    a = None
    b = None
    z = [0, 1]
    pisanoperiod = None
    for x in range(1, n ** 2):
        a = (z[x - 1] + z[x]) % k

        if len(z) > 2 and a == 1 and z[x] == 0:
            pisanoperiod = len(z) - 1
            break

        z.append(a)

    if pisanoperiod:
        return z[n % pisanoperiod]

    return z[n]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))


