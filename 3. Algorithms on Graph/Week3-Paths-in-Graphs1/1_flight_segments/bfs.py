#Uses python3
import sys
from collections import deque

def distance(adj, s, t):
    dist = [float('inf') for _ in range(len(adj))]
    dist[s] = 0
    q = [s]
    queue = deque(q)

    while len(queue) != 0:
        curr = queue.pop()
        for node in adj[curr]:
            if dist[node] == float('inf'):
                queue.appendleft(node)
                dist[node] = dist[curr] + 1
                if t == node:
                    return dist[node]
    #write your code here

    return -1

if __name__ == '__main__':
    i = input()
    data = list(map(int, i.split()))
    n, m = data
    adj = [[] for _ in range(n+1)]

    for _ in range(1, m+1):
        data_new = input()
        data_new = data_new.split()
        x, y = int(data_new[0]), int(data_new[1])
        adj[y].append(x)
        adj[x].append(y)

    find_conn = input()
    x, y = [int(x) for x in find_conn.split()]
    # print(adj)

    path = distance(adj, x, y)
    if path == -1:
        print(-1)
    else:
        print(path)
