# python3
# Make Heap

def siftdown(x):
    j = data
    min_node = x
    right_node = 2 * x + 1
    left_node = 2 * x

    if left_node <= len(data)-1 and data[left_node] < data[min_node]:
        min_node = left_node

    if right_node <= len(data)-1 and data[right_node] < data[min_node]:
        min_node = right_node

    if x != min_node:
        swaps.append((x - 1, min_node - 1))
        data[x], data[min_node] = data[min_node], data[x]
        siftdown(min_node)


def build_heap(data):
    for x in range((len(data)-1)//2, 0, -1):
        siftdown(x)

    return swaps



n = int(input())
data = list(map(int, input().split()))
assert len(data) == n
# print(data)
swaps = []
data = [None] + data
result = build_heap(data)
print(len(result))

if swaps:
    for i, j in swaps:
        print(i, j)

#print(len(result))
# print()