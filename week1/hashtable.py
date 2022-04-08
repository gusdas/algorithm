import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000  # 기본사이즈
        self.table = collections.defaultdict(ListNode)  # 테이블을 ListNode를 담게 될 기본자료형으로 선언
        # collections.defaultdict사용시 존재하지않는 키 조회시 default를 생성해준다

    def put(self, key: int, value: int) -> None:
        index = key % self.size  # key로 size를 나머지연산을 통한 해싱방법을 사용하여 index를 정한다.

        # 만약 해당 인덱스에 아무것도 없으면 키,값을 삽입하고 종료하는데 .value를 넣은 이유는 defaultdict사용하여 defalut가 되도록 했기 때문이다.
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return



        p = self.table[index]
        while p: #index를 돌면서 확인
            if p.key == key: #해시충돌 발생 키가 존재할 경우 값을 업데이트한다
                p.value = value
                return
            if p.next is None:
                break
                p = p.next      #p.next를 p로 바꾸면서 탐색
            p.next = ListNode(key, value) # p = p.next로 인해 p가 none이 되는데 p.next에서 왜 에러가 발생해?

    def get(self, key: int) -> int:
        index = key % self.size #나머지연산으로 index를 구하고
        if self.table[index].value is None: #비어있으면 -1 반환
            return -1

        p = self.table[index]
        while p:
            if p.key == key: #키가 일치하면 값가져오기
                return p.value
            p = p.next #p.next를 p로 바꾸면서 탐색
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None: #아무것도 없을때
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next #3항 연산자로  p.next is None이면  ListNode()넣고 false면 p.next 넣기
            return

        #연결리스트 노드삭제
        prev = p #prev는 이전 노드 p는 현재노드로 p.next로 탐색하다가 일치하는 노드 발견시 이전노드.next를 현재노드의  next로 바꿔버려서 p의 연결없앤다.
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next #다음 노드 탐색을 위한 변환
