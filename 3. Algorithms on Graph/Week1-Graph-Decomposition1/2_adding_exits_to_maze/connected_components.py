#Uses python3
import sys
def dfs(x, visited):
    visited[x] = True
    for node in adj[x]:
        if not visited[node]:
            dfs(node, visited)

    return visited


def number_of_components(adj):
    count = 0
    visited = [False] * (len(adj))
    for index in range(1, len(adj)):
        if not visited[index]:
            visited = dfs(index, visited)
            count += 1

    return count

if __name__ == '__main__':
    i = input()
    data = list(map(int, i.split()))
    v, e = data
    adj = [[] for _ in range(v+1)]
    for _ in range(1, e+1):
        data_new = input()
        data_new = data_new.split()
        x, y = int(data_new[0]), int(data_new[1])
        adj[y].append(x)
        adj[x].append(y)

    # print((x, y))
    # find_conn = input()
    # x, y = [int(x) for x in find_conn.split()]
    #
    # print(adj)
    print(number_of_components(adj))
