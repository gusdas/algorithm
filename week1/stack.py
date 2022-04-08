class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None\



    def push(self,val):
        self.top = Node(val,self.top)

    def pop(self):

        pop = self.top.val
        self.top = self.top.next

        return pop


#
#
# c1 = Stack()
# c1.push(1)
# c1.push(2)
# c1.push(3)
# c1.pop()
#
# print(c1.pop())
#
#
#
# print(c1)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # class Node:
# #     def __init__(self, val, next):
# #         self.val = val
# #         self.next = next
# #
# #
# # class Stack:
# #     def __init__(self):
# #         self.top = None
# #
# #     def is_empty(self):
# #         return self.top is None
# #
# #     def push(self, val):
# #         self.top = Node(val, self.top)
# #
# #     def pop(self):
# #         if not self.top:
# #             return None
# #
# #         node = self.top
# #         self.top = self.top.next
# #
# #         return node.item
# #
# #
# # def is_vailed(s):
# #     pair = {
# #         '}': '{',
# #         ']': '[',
# #         ')': '(',
# #     }
# #     opener = '[{('
# #     stack = []
# #     for char in s:
# #         if char in opener:
# #             stack.append(char)
# #         else:
# #             if not stack:
# #                 return False
# #             top = stack.pop()
# #             if pair[char] != top:
# #                 return False
# #     return not stack
# #
# #
# # print(is_vailed("[][{}]"))