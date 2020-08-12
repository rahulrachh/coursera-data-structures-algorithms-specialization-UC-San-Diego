# python3
import sys


def optimal_weight(W, w):
    result = [[0 for x in range(W + 1)] for y in range(len(w))]

    for j in range(0, len(w)):
        for i in range(1, W + 1):
            if w[j] > i:
                result[j][i] = result[j - 1][i]
            else:
                result[j][i] = max(w[j] + result[j - 1][i - w[j]], result[j - 1][i])

    return result[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))