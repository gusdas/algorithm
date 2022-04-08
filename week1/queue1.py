class Node:
    def __init__(self,val,next=None ):
        self.val = val
        self.next = next

class queue:
    def __init__(self):
        self.front = None


    def append(self,val):
        if not self.front:
            self.front = Node(val,None)

        node = self.front
        while node.next:
            node = node.next
        self.front.next = Node(val,None)












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
        node = self.front
        self.front = self.front.next
        return node.item

    def is_empty(self):
        return self.front is None
#
#
# l1 = Queue()
#
# l1.push(10)
# l1.push(20)
# l1.push(30)
