# python3
import sys
import random

def compute_prefix(text):
    s = [0] * len(text)
    s[0] = 0
    border = 0

    for idx in range(1, len(text)):

        while (border > 0) and (text[idx] != text[border]):
            border = s[border-1]

        if text[idx] == text[border]:
            border += 1
        else:
            border = 0

        s[idx] = border

    return s
    # pass


def find_pattern(pattern, text):
    if len(pattern) > len(text):
        return

    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    # randomly choose a symbol that is not A,T,G,C
    random_text = 'BDEFHIJKLMNOPQRSUVWXYZ!@#$%^&*()_1234567890<>?-`~";:,./'
    mid = random.choice(random_text)

#    K-N-P algorithm
    X = pattern + mid + text
    s = compute_prefix(X)
    result = []

    for idx in range(len(pattern)+1, len(X)):
        if s[idx] == len(pattern):
            result.append(idx - 2*len(pattern))

    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    if result:
        print(" ".join(map(str, result)))
    else:
        print()
