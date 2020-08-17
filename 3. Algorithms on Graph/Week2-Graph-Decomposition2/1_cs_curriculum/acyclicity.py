#Uses python3
import sys

def reach(adj, x, y):
    #write your code here
    if y in adj[x]:
        return 1
    visited[x] = True
    for i in adj[x]:
        if not visited[i]:
            j = reach(adj, i, y)
            if j == 1: return 1

def acyclic(adj):
    for x in range(1, len(adj)):
        cycle = reach(adj, x, x)
        if cycle == 1:
            return 1

if __name__ == '__main__':
    i = input()
    data = list(map(int, i.split()))
    v, e = data
    adj = [[] for _ in range(v+1)]
    for _ in range(1, e+1):
        data_new = input()
        data_new = data_new.split()
        x, y = int(data_new[0]), int(data_new[1])
        adj[x].append(y)
    global visited
    visited = [False] * (v + 1)

    pk = acyclic(adj)
    if pk:
        print(1)
    else:
        print(0)
