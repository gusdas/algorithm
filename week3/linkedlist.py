# 노드 생성
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 연결 리스트 생성
class linkedList:
    def __init__(self):
        self.head = None  # 포인터
        self.size = 0  # 크기
    #제일 뒤에 추가하는 함수
    def append(self, val):
        if not self.head:  # 헤더가 없으면 헤더에 추가
            self.head = Node(val)
            self.size += 1
            return

        node = self.head  # node 변수에 담아서 고정시켜야지 아래 while문이 작동함 즉 헤더는 고정하고 변수에 담긴 self.head는 이동시키고 추가

        while node.next:  # head의 next가 None일때까지 돌면서 데이터 추가
            node = node.next  # node에 node.next로 바꿔주면서 추가
        node.next = Node(val)
        self.size += 1

    #뒤에서 삭제하는 함수
    def back_delete(self, idx):
        real_idx = abs(self.size - idx)     #삭제할 위치 0 부터 찾기위해 뺴줌
        node = self.head                    #현재노드
        prev = self.head                    #prev현재 노드의 전
        for i in range(real_idx):           #real_idx
            prev = node                     #현재 노드를 prev에 저장하고
            node = node.next                #현재 노드의 next를 노드로 지정


        prev.next = node.next               #prev.next가 node.next로 가면 node의 연결이 끊겨서 node가 삭제됌
        self.size -= 1


l1 = linkedList()

l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.back_delete(2)
