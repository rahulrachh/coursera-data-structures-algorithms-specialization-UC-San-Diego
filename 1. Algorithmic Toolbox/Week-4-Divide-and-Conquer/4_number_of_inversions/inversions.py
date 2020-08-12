# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions = get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(a, b, left, right)
    return number_of_inversions


def merge(a, b, left, right):
    ave = (left + right) // 2

    count = 0
    l = left
    r = ave
    k = left
    while l < ave and r < right:
        if a[l] <= a[r]:
            b[k] = a[l]
            l += 1
            k += 1
        else:
            count += ave - l
            b[k] = a[r]
            k += 1
            r += 1

    while l < ave:
        b[k] = a[l]
        l += 1
        k += 1
    while r < right:
        b[k] = a[r]
        k += 1
        r += 1

    for index in range(left, right):
        a[index] = b[index]

    return count


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n = 6
    # a = [2, 3, 9, 2, 9]
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))