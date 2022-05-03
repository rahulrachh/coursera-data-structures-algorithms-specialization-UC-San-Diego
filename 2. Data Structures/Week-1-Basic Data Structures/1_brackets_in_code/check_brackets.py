# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((next, i + 1))

        if next in ")]}":
            if not opening_brackets_stack:
                return i+1
            # Process closing bracket, write your code here
            last, idx = opening_brackets_stack.pop()
            if not are_matching(last, next):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0][1]
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
