import sys
from collections import deque, defaultdict

people = int(sys.stdin.readline())  # 전체 사람의 수
personA, personB = map(int, input().split(" "))  # 사람의 번호
n = int(input())  # 부모자식간의 관계수
familly = defaultdict(list)
for _ in range(n):
    parent, child = map(int, input().split(" "))
    familly[parent].append(child)
    familly[child].append(parent)
visited = [-1] * (people + 1)
visited[personA] = 0

# def dfs(start,count):
#     if start == personB:
#         print(count)
#     visited[start] = 0
#     for adj in familly[start]:
#         if visited[adj] == -1:
#             dfs(adj,count+1)
#
# dfs(personA,0)


# def dfs(start):
#     for adj in familly[start]:
#         if visited[adj] == -1:
#             visited[adj] = visited[start] +1
#             dfs(adj)
# dfs(personA)
#
# print(visited[personB])



# visited = [-1] * (people + 1)
# q = deque([personA])
# visited[personA] = 0

# q가 탐색할 친구

# adj는 내가 다음에 갈 곳
# node 는 현재 위치
# while q:
#     node = q.popleft()
#     for adj in familly[node]:
#         if visited[adj] == -1:
#             q.append(adj)
#             visited[adj] = visited[node] + 1
#
# print(visited[personB])

