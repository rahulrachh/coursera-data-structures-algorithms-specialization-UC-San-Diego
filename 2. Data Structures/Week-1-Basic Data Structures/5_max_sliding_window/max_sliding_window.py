# python3
# Maximum in Sliding Window

from collections import deque

def max_sliding_window_naive(nums, k):
    d = deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out += nums[d[0]],
    return out


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
