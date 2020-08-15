#Uses python3
import sys
def reach(adj, x, y):
    #write your code here
    if y in adj[x]:
        return 1
    # def dfs(x, y):
    visited[x] = True

    for i in adj[x]:
        if not visited[i]:
            j = reach(adj, i, y)
            if j==1: return 1

    # j = reach(adj, x, y)

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
    global visited
    visited = [0] * (n+1)
    find_conn = input()
    x, y = [int(x) for x in find_conn.split()]

    final = reach(adj, x, y)
    if final:
        print(1)
    else:
        print(0)

