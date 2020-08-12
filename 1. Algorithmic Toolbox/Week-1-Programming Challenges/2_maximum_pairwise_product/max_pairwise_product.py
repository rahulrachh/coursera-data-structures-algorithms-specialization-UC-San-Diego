# python3
# 1-2: Maximum Pairwise Product

def max_pairwise_product(numbers):
    n = len(numbers)
    input_numbers.sort()
    return input_numbers[-1]*input_numbers[-2]

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
