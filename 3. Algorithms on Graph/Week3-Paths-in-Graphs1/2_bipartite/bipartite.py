#Uses python3
import sys

def bipartite(adj):
    color = [None] * len(adj)

    for x in range(1, len(adj)):
        if color[x] == None: color[x] = 0
        for nodes in adj[x]:
            if color[nodes] == None:
                color[nodes] = color[x] ^ 1

    for x in range(1, len(adj)):
        for nodes in adj[x]:
            if color[nodes] == color[x]:
                return 0


    return 1


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

    path = bipartite(adj)
    if path == 1:
        print(1)
    else:
        print(0)
