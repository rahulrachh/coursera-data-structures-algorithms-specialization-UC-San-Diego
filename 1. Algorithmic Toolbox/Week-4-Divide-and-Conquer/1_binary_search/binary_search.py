# Uses python3
import sys

def binarysearch(a, x):
    low, high = 0, len(a)-1
    while low <= high:
        mid = (low+high)//2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    array = input()
    elements_to_search = input()
    # print(array)
    data = list(map(int, array.split()))
    # print(data)
    data2 = list(map(int, elements_to_search.split()))
    # print(type(data2[0]))
    n = data[0]
    m = data2[0]
    a = data[1:]
    #
    for x in data2[1:]:
    # replace with the call to binary_search when implemented
        print(binarysearch(a, x), end = ' ')
