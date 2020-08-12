# Uses python3
def edit_distance(b, a):
    if a == b: return 0
    #write your code here
    T = [[float('inf')] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        T[i][0] = i

    for j in range(len(b) + 1):
        T[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                diff = 0
            else:
                diff = 1

            T[i][j] = min(T[i-1][j] + 1,
                          T[i][j-1] +1,
                          T[i-1][j-1] + diff)


    return T[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
