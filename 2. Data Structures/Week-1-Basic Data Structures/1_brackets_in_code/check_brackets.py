# python3
# Check brackets in the code

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i, next))

        if next in ")]}":
            if not opening_brackets_stack:
                return i+1
            else:
                if not are_matching(opening_brackets_stack[-1][1],next):
                    return i+1
                else:
                    opening_brackets_stack.pop()

    if not opening_brackets_stack:
        return "Success"
    else:
        return opening_brackets_stack[-1][0]+1

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
