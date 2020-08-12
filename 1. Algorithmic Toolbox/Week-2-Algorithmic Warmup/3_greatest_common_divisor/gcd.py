# Uses python3
# 2-3: Greatest Common Divisor

import sys

def gcd(a, b):
    if b == 0:
        return a

    adash = a%b
    return gcd(b, adash)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))