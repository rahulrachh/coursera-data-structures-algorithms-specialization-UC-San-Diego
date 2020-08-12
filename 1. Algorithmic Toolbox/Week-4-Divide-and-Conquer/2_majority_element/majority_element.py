# Uses python3
import sys
from collections import Counter

def divide_func(seq):
    k = Counter(seq)
    len_seq = len(seq)
    k_sort = sorted(k.items(), key=lambda x: -x[1])
#    print(k_sort)
    if k_sort[0][1] > len_seq//2:
        return True
    else:
        return False


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a = [1, 2, 3, 1, 1]
    if divide_func(a):
        print(1)
    else:
        print(0)
