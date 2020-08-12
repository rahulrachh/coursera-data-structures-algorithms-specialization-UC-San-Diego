# Uses python3
# 3-1: Money Change

import sys
def get_change(m):
    # write your code here
    ten = 0
    five = 0
    one = 0
    if m >= 10:
        ten = m // 10
        m = m - ten * 10
    
    if m >= 5:
        five = m // 5
        m = m - five * 5
    
    if m >= 1:
        one = m
    
    return ten + five + one

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
