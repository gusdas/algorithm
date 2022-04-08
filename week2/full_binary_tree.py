from collections import deque
def test_max_depth(lst):
    root = make_tree_by(lst, 0)
    if not root:
        return 0

    q = deque([root])
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst): # 재귀함수로 인덱스를 2* 부모 +1 해주니깐 리프노드에선 실행하지 않도록 걸러줌
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        #배열로 만들때 [0,1,2,null,null,5,6]
        #  0
        #1   2
        #   5 6
        parent.left = make_tree_by(lst, 2 * idx + 1) #왼쪽은 부모인덱스 * 2 + 1
        parent.left = make_tree_by(lst, 2 * idx + 2) #왼쪽은 부모인덱스 * 2 + 1

    return parent