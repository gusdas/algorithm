# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  #dummy를 만드는 이유는 head부터 시작해도 되지만 여러 예외처리를 해줘야해서이다.
        fast = dummy
        slow = dummy
        head = dummy

        for i in range(n):
            fast = fast.next    #n만큼 fast를 먼저 이동시켜준다.
                                #왜냐하면 우리는 뒤에서부터 삭제하기위해 먼저 가있고 하나씩 가면서 fast.next가 None일때  slow가 삭제할 노드전에 위치한다.
                                #삭제할 노드에 위치하게 짠다면 우리는 prev값을 들고 가지고있어야 노드를 연결한다.

        while fast.next:        #fast.next가 None일때 까지
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next #slow가 현재 prev라고 생각하면 편하다.
        return head.next        #head가 현재 dummy에 위치했으니깐 head.next head로하고
                                # = dummy를 삭제해도 될거 같은데 [1] 일때를 빼주지 못한다.
                                #그래서 dummy를 추가하는 이유기도 한다.