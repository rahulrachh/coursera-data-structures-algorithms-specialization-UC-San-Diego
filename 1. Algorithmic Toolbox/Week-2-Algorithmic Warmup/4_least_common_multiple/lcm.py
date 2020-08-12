# Uses python3
# 2-4: Least Common Multiple

import sys

def gcd(a, b):
    if b == 0:
        return a

    adash = a%b
    return gcd(b, adash)


def lcm(a, b):
    return '%0.2d' %(a/gcd(a, b) * b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
