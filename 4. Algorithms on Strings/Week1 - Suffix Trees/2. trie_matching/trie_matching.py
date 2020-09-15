# uses python3

# This function build the Trie
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
                    # i += 1
            else:
                tree[i] = {letter: node+1}
                node += 1
                i += 1

    return tree

# Traverses through the Text with the trie and finds the pattern.
def find_pattern(text, trie):
    indexes = []
    i = 0
    j = 0
    root = trie[0]
    v = root
    # pattern = True
    pattern_index = []
    while j < len(text):
        # letter = text[i]
        while i < len(text) and text[i] in v:
            if '$' in trie[v[text[i]]]:
                # j += 1
                if pattern_index:
                    indexes.append(pattern_index[0])
                else:
                    indexes.append(j)
                break
            else:
                v = trie[v[text[i]]]
                pattern_index.append(i)
                i += 1

        j += 1
        i = j
        v = root
        pattern_index.clear()


    return indexes if len(indexes) > 0 else None


text = input()
# print(text)
n = int(input())
# print(n)
patterns = []

# Here I have added '$' at the end of the pattern
# so that i know that I have reached to the end 
# of the pattern while traversing through the text.

for i in range(n):
    patterns.append(input()+'$')

# print(patterns)
trie = build_trie(patterns)

indexes_pattern = find_pattern(text, trie)

if indexes_pattern:
    print(' '.join (map (str, indexes_pattern)))
else:
    print()
