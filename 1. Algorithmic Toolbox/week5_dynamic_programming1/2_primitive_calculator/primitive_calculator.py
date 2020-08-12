# Uses python3
import sys

def optimal_sequence(N):
    result = [float('inf') for _ in range(N + 1)]
    result[0] = None
    result[1] = 0
    # print(result)
    for i in range(1, N + 1):
        if i + 1 <= N: result[i + 1] = min(result[i] + 1, result[i + 1])
        if 2 * i <= N: result[2 * i] = min(result[i] + 1, result[2 * i])
        if 3 * i <= N: result[3 * i] = min(result[i] + 1, result[3 * i])
        # print(result)

    i = result[-1]
    print(i)
    final = []
    for x in range(len(result) - 1, 0, -1):
        if result[x] == i:
            final.append(x)
            i -= 1

    for x in reversed(final):
        print(x, end=' ')


input = sys.stdin.read()
n = int(input)
# n = 96234
optimal_sequence(n)
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')
