from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}
#방문한 배열 stat넣고 생성
# deque start넣고 생성
#q가 없을때까지 반복
# q에서 popleft로 node를 가져옴
# 그래프[노드] 갯수만큼 반복
# 그때 그노드는 방문한적이 없어야함(방문한 배열로 확인)
# 조건 충족시 q랑 방문한 배열에 추가
# 이렇게 해야지 q에 방문 한적 없는 아이들만 추가 되고 방문한 적없는 노드에서 돌면서 노드를 찾음

#dfs와 bfs의 차이는 visited를 for문에서 추가해주냐(bfs) 노드로 추가해주냐(dfs)
def bfs_queue(start):
    visited = [start]
    q = deque([start])
    # q가 탐색할 친구
    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited

assert bfs_queue(1) == [1, 2, 3, 4, 5, 6, 7]