# uses python3

def negative_cycle(adj, cost):
    dist = [float('inf')] * len(adj)
    dist[0] = 0

    for i in range(len(adj)):
        for u in range(len(adj)):
            for v_ind,v in enumerate(adj[j]):
                if dist[v] > dist[u] + cost[u][v_ind]:
                    dist[v] = dist[u] + cost[u][v_ind]


        if i == len(adj)-2:
            dist_list_prev = list(dist)
        if i == len(adj)-1:
            dist_list_curr = list(dist)


    if dist_list_prev == dist_list_curr:
        return 0
    else:
        return 1

if __name__ == '__main__':
    i = input()
    data = list(map(int, i.split()))
    n, m = data
    adj = [[] for _ in range(n + 1)]
    cost = [[] for _ in range(n + 1)]
    for _ in range(m):
        data_new = input()
        data_new = data_new.split()
        x, y, c = int(data_new[0]), int(data_new[1]), int(data_new[2])
        adj[x].append(y)
        cost[x].append(c)

    print(negative_cycle(adj, cost))
