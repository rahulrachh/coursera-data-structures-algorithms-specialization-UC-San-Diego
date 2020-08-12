# Uses python3
# 3-4: Maximum Advertisement Revenue (Maximum Dot Product)

import sys


def max_dot_product(a, b):
    # write your code here
    a.sort()
    b.sort()
    res = 0

    for i in range(len(a)):
        res += a[i] * b[i]

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    # n = 3
    a = data[1:(n + 1)]
    # a = [1, 3, -5]
    b = data[(n + 1):]
    # b = [-2, 4, 1]
    print(max_dot_product(a, b))


