# python3
# Tree Orders

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
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


    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        x = 0
        def inordernested(x):
            if x != -1:
                # print(x)
                inordernested(self.left[x])
                self.result.append(self.key[x])
                inordernested(self.right[x])

        inordernested(x)
        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        x = 0
        def preordernested(x):
            if x != -1:
                self.result.append(self.key[x])
                preordernested(self.left[x])
                preordernested(self.right[x])

        preordernested(x)

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        x = 0
        def postordernested(x):
            if x != -1:
                postordernested(self.left[x])
                postordernested(self.right[x])
                self.result.append(self.key[x])

        postordernested(x)

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
