# Uses python3
import sys

def get_change(money):
    result = [0 for _ in range(money+1)]
    coin_change = [1, 3, 4]
    for m in range(1, money+1):
        for coin in coin_change:
            if m >= coin:
                num_coins = result[m - coin] + 1
                if result[m] == 0:
                    result[m] = num_coins
                elif num_coins < result[m]:
                    result[m] = num_coins

    return result[-1]
    #write your code here
    # return m // 4
    # pass

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 34
    print(get_change(m))
