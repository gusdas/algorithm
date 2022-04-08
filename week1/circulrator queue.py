class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Circulrator_Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def enQueue(self, val):
        if not self.front:
            node = Node(val)
            self.front = node
            self.rear = node

        self.rear.next = Node(val)
        self.rear = self.rear.next
    def deQueue(self):
        if self.front == None:
            return None
        data = self.front.val
        self.front = self.front.next

        if self.front == None:
            self.rear = None
            return data
        return data
#
# c1 = Queue()
# c1.enQueue(10)
# c1.enQueue(20)
# c1.deQueue()