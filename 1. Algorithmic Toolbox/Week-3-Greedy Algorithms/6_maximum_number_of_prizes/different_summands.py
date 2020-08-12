# Uses python3
# 3-6: Maximum Number of Prizes (Different Summands)

import sys

def optimal_summands(number):
    z = []
    znum = number
    for x in range(1, number+1):
        if znum > 2*x:
            z.append(x)
            znum = znum - x

        else:
            z.append(znum)
            break

    return z

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
