# Uses only python3
import sys

def dfs(adj, used, order, x):
    #write your code here
    if len(order) != len(adj) - 1:
        for nodes in adj[x]:
            if not used[nodes]:
                dfs(adj, used, order, nodes)

        if (used[x] == 0) and ((len(adj[x]) == 0) or all([used[x] == 1 for x in adj[x]])):
            order.append(x)
            used[x] = 1


def toposort(adj):
    #write your code here
    used = [0] * len(adj)
    order = []
    for vertex in range(1, len(adj)):
        dfs(adj, used, order, vertex)
    
    return order


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

    # print(adj)

    order = toposort(adj)
    for x in order[::-1]:
        print(x, end=' ')
