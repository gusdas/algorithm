def card(num):
    l1 = Queue()
    for i in range(num):

        l1.push(i)
    return l1.front.val

print(card(4))


class Node:
    def __init__(self,val,next=None ):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value, None)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.item

    def is_empty(self):
        return self.front is None
