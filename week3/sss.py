
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        self.top = Node(val, self.top)
        self.size += 1

    def pop(self):
        if not self.top:
            return -1
        pop = self.top.val
        self.top = self.top.next
        self.size -= 1

        return pop

    def empty(self):
        if self.size == 0:
            return 1
        return 0
Stack = Stack()
import sys


input = sys.stdin.readline

N = int(input())

for _ in range(N):
    word = input().split()
    order = word[0]
    if order == "push":
        value = int(word[1])
        Stack.push(value)
    elif order == "pop":
        print(Stack.pop())
    elif order == "size":
        print(Stack.size)
    elif order == "empty":
        print(Stack.empty())
    elif order == "top":
        if Stack.top.val:
            print(Stack.top.val)
        print(-1)

