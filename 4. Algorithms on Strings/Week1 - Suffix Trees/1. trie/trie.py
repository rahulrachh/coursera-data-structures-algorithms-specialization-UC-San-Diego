#Uses python3

def build_trie(patterns):
    tree = dict()
    node = 0

    for pattern in patterns:
        i = 0

        for letter in pattern:
            if tree.get(i):
                if letter not in tree[i]:
                    tree[i].update({letter: node+1})
                    node += 1
                    i = node
                else:
                    i = tree[i][letter]
            else:
                tree[i] = {letter: node+1}
                node += 1
                i += 1

    return tree

if __name__ == '__main__':
    number_of_patterns = int(input())
    patterns = []

    for strings in range(number_of_patterns):
        patterns.append(input())

    tree = build_trie(patterns)

    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

