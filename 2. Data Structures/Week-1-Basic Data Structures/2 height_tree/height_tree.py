# python3

import sys
import threading
import collections
import collections

def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = -1
    tree = collections.defaultdict(list)
    q = collections.deque([-1])
    for i, node in enumerate(parents):
        tree[node].append(i)
    while q:
        max_height += 1
        l = len(q)
        for _ in range(l):
            node = q.popleft()
            q.extend(tree[node])
    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
