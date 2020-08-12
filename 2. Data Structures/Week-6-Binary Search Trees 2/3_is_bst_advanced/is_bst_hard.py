# python3
# Is it a Binary Search Tree? Hard version.

import sys, threading
sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class BinarySearchTree:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]

        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().rstrip().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def IsBinarySearchTree(self):
        if self.n == 0: return True
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        x = 0
        def inorder(x):
            if x != -1:
                inorder(self.left[x])
                self.result.append(self.key[x])
                inorder(self.right[x])

        inorder(x)

        # checks if it is a BST
        for x in range(1, len(self.result)):
            if self.result[x] < self.result[x-1]:
                return False

        # checks whether there are equal elements in the left subtree
        for x in range(len(self.key)):
            if self.left[x] != -1:
                if self.key[x] == self.key[self.left[x]]:
                    return False

        return True


def main():
    nodes = BinarySearchTree()
    # print(tree)
    nodes.read()
    if nodes.IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
