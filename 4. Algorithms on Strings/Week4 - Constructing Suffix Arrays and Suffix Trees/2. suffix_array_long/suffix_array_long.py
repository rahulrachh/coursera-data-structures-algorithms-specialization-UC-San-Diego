# python3
import sys

def compute_char_classes(text, order):
    classes = [None] * len(text)
    classes[order[0]] = 0

    for i in range(1, len(order)):
        classes[order[i]] = classes[order[i-1]]

        if text[order[i]] != text[order[i-1]]:
            classes[order[i]] += 1

    return classes


def sort_doubled(text, L, order, classes):
    count = [0] * len(text)
    new_order = [0] * len(text)

    for c in classes:
        count[c] += 1

    for i in range(1, len(text)):
        count[i] += count[i - 1]

    for i in range(len(text) - 1, -1, -1):
        start = (order[i] - L + len(text)) % len(text)
        cl = classes[start]

        count[cl] -= 1
        new_order[count[cl]] = start

    return new_order


def update_classes(order, classes, L):
    newClass = [None] * len(order)
    newClass[order[0]] = 0

    for i in range(1, len(order)):
        cur, prev = order[i], order[i-1]

        mid, midPrev = (cur + L) % len(order), (prev + L) % len(order)

        if (classes[cur] != classes[prev]) or (classes[mid] != classes[midPrev]):
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]

    return newClass


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    order = sorted(range(len(text)), key=lambda x: text[x])
    classes = compute_char_classes(text, order)
    L = 1

    while L < len(text):
        order = sort_doubled(text, L, order, classes)
        classes = update_classes(order, classes, L)
        L = L * 2

    return order
  # Implement this function yourself
  # return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))

  
