#Uses python3
import math


def minimum_distance(n, x, y):
    # result = 0
    #write your code here
    nodes = tuple(zip(x, y))

    pos = 0
    nodes_distance = []
    while pos < len(x)-1:
        for i in range(pos+1, len(x)):
            x_dist = (nodes[pos][0] - nodes[i][0]) ** 2
            y_dist = (nodes[pos][1] - nodes[i][1]) ** 2
            dist = math.sqrt(x_dist + y_dist)
            nodes_distance.append((pos, i, dist))

        pos += 1

    
    # print(nodes_distance)
    sorted_nodes_distance = sorted(nodes_distance, key=lambda x: x[2])
    # print(sorted_nodes_distance)

    union_vertices = [x for x in range(n)]
    final_nodes = []
    result = 0
    for i in sorted_nodes_distance:
        if union_vertices[i[0]] != union_vertices[i[1]]:
            final_nodes.append(i)
            result += i[2]

            union_vertices = list(map(lambda x: union_vertices[i[0]] if x == union_vertices[i[1]] else x, union_vertices))

    return result

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    # data = list(map(int, input.split()))
    # print(data)
    # n = data
    x = []
    y = []
    for _ in range(n):
        x_y_data = list(map(int, input().split()))
        x.append(x_y_data[0])
        y.append(x_y_data[1])

    # print("length of x is {0}".format(len(x)))
    print("{0:.9f}".format(minimum_distance(n, x, y)))
