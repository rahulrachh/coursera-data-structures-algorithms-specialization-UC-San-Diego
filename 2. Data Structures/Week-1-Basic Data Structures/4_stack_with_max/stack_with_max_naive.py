#python3
# Stack with maximum

import sys

class StackWithMax():
    def __init__(self):
        self.stack = []

    def Push(self, a):
        if not self.stack:
            self.stack.append((a, a))
        else:
            max_elem = self.stack[-1][1]
            self.stack.append((a, max(max_elem,a)))

    def Pop(self):
        if self.stack:
            self.stack.pop()

    def Max(self):
        if self.stack:
            return self.stack[-1][1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
