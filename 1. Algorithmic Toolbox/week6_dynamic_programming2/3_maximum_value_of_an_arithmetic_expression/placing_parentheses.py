# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j):
    tempMin = float('inf')
    tempMax = float('-inf')

    for k in range(i, j):
        a = evalt(max_val[i][k], max_val[k+1][j], exp_arr[k])
        b = evalt(max_val[i][k], min_val[k+1][j], exp_arr[k])
        c = evalt(min_val[i][k], max_val[k+1][j], exp_arr[k])
        d = evalt(min_val[i][k], min_val[k+1][j], exp_arr[k])

        tempMin = min(tempMin, a, b, c, d)
        tempMax = max(tempMax, a, b, c, d)

    return tempMin, tempMax

def get_maximum_value(dataset):
    #write your code here
    for i in range(len_num_arr):
        min_val[i][i], max_val[i][i] = num_arr[i], num_arr[i]

    for s in range(1, len_num_arr):
        for i in range(len_num_arr-s):
            j = i + s
            min_val[i][j], max_val[i][j] = MinAndMax(i, j)


    return max_val[0][-1]


if __name__ == "__main__":
    dataset = input()
    # size = ((len(dataset) - 1) // 2)+1
    # print(size)
    global num_arr
    global min_val
    global max_val
    global len_num_arr
    global exp_arr
    exp_arr = [dataset[x] for x in range(1, len(dataset), 2)]
    # print(exp_arr)
    num_arr = [int(dataset[x]) for x in range(0, len(dataset), 2)]
    len_num_arr = len(num_arr)
    # print(num_arr)
    min_val = [[0 for x in range(len_num_arr)] for y in range(len_num_arr)]
    max_val = [[0 for x in range(len_num_arr)] for y in range(len_num_arr)]
    print(get_maximum_value(dataset))
