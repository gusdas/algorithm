#노드 생성
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 데이터
        self.next = next  # 링크


# 링크드 리스트 생성, self는 자기자신
class LinkedList:
    def __init__(self):
        self.head = None  # 포인터(위치)

    def append(self, val):
        # head가 none을 가르키면 헤드에 Node추가하고 끝
        if not self.head:
            self.head = ListNode(val, None)
            return

        # node변수에 self.head 할당
        node = self.head
        while node.next:  # self.head.next가 없을때 까지
            node = node.next  # node에 node.next 할당

        # node.next는 None이니깐 ListNode 추가
        node.next = ListNode(val, None)

    def pop(self):
        if not self.head:
            return None

        pop = self.head.val
        self.head = self.head.next

        return pop

#

l1 = LinkedList()

l1.append(10)
l1.append(20)
l1.append(30)

l1.pop()
#
#
#
#
#
#
#
#
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         init = ListNode('init')
#         self.head = init
#         self.tail = init
#
#         self.current = None  # 현재노드
#         self.size = 0
#
#     def __len__(self):
#         return self.size
#
#     def __str__(self):
#         node = self.head
#         node = node.next
#         s = ''
#
#         for i in range(self.size):
#             s += f'{node.val}, '
#             node = node.next
#         return f'[{s[:-2]}]'
#
#     def append(self, val):
#         newNode = ListNode(val)
#         self.tail.next = newNode
#         self.tail = newNode
#         self.size += 1
#     def insert(self,input_index,input_data):
#         node = self.head
#
#         for i in range(input_index):
#             node = node.next
#         newNode = ListNode(input_data)
#         newNode.next = node.next
#         node.next = newNode
#
#         self.size += 1
#
#
#     def pop(self):
#         lastData = self.tail.val
#         node = self.head
#         for i in range(self.size):
#             if node.next is self.tail:
#                 self.tail = node
#                 break
#             node = node.next
#             self.size -= 1
#         return lastData
#
#     def find(self, val):
#         index = -1
#         node = self.head
#         node = node.next
#         for i in range(self.size + 1):
#             if node.val == val:
#                 return index
#             index += 1
#             node = node.next
#         return -1
#
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node.val
#             node = node.next
# #
# #
# # l = LinkedList()
# # l.append(10)
# # l.append(20)
# # l.append(30)
# # l.insert(2,1000)
# # print(l)
#
# # class units:
# #     name = ''
# #     hp = ''
# #     defend = '1'
# #     damaged= ''
# # class protoss:
# #     shield = ''
# #     shield_def = '1'
# #
# # class zealot(units,protoss):
# #     def __init__(self):
# #         self.name = 'zealot'
# #         self.hp = '100'
# #         self.damaged = '10'
# #
# # p1 = zealot()
# #
# # print(p1.shield_def)



