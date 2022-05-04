#python3
import sys

class Node:
    def __init__(self, val, max_elem, prev=None, next=None):
        self.val = val
        self.max_elem = max_elem
        self.prev = prev
        self.next = next        

class StackWithMax():
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0

    def Push(self, a):
        if not self.len:
            node = Node(a, a, self.head, self.tail)
            self.head.next = node
            self.tail.prev = node
        else:
            prev_node = self.tail.prev
            node = Node(a, max(a, prev_node.max_elem), prev_node, self.tail)
            prev_node.next = node
            self.tail.prev = node
        self.len += 1

    def Pop(self):
        if self.len:
            prev_node = self.tail.prev
            prev_prev_node = prev_node.prev
            prev_prev_node.next = self.tail
            self.tail.prev = prev_prev_node
            self.len -= 1

    def Max(self):
        if self.len:
            prev_node = self.tail.prev
            return prev_node.max_elem


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
