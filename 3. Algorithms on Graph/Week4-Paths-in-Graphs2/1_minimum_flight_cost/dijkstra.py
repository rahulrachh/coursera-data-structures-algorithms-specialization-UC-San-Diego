# uses python3
import queue

def distance(adj, cost, s, t):
    # write your code here

    dist = [10**9] * len(adj)
    dist[s] = 0
    qH = queue.PriorityQueue()
    qH.put(s)


    while not qH.empty():
        u = qH.get()
        for v in adj[u]:
            v_ind = adj[u].index(v)
            if dist[v] > dist[u] + cost[u][v_ind]:
                dist[v] = dist[u] + cost[u][v_ind]
                """
                Only adding nodes to the queue that have lower distance
                compared to other nodes that are present, so no need
                to extract the minimum as we we are only adding nodes that 
                have improved distance which is less than the others.
                """
                qH.put(v)


    if dist[t] == 10**9:
        return -1
    else:
        return dist[t]


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
        # adj[y].append(x)
        adj[x].append(y)
        cost[x].append(c)

    find_distance = input()
    s, t = [int(x) for x in find_distance.split()]
    print(distance(adj, cost, s, t))


