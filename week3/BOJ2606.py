import sys
from collections import defaultdict, deque

coms = int(sys.stdin.readline())
line = int(sys.stdin.readline())
computer = defaultdict(list)
for _ in range(line):
    parent, child = map(int, sys.stdin.readline().split(" "))
    computer[parent].append(child)
    computer[child].append(parent)

visited = [0] * coms


def dfs(start, cnt):

    for adj in computer[start]:
        if visited[adj - 1] == 0:
            visited[adj-1] = 1
            dfs(adj, cnt + 1)


dfs(1,0)
print(sum(visited)-1)




# def bfs(start):
#     visited = [0] * coms
#     q = deque()
#     q.append(start)
#     visited[start-1] = 1
#     count = 0
#     while q:
#         cur = q.popleft()
#
#         for adj in computer[cur]:
#             if visited[adj-1] == 0:
#                 visited[adj-1] = 1
#                 q.append(adj)
#                 count += 1
#
#     print(count)
# bfs(1)
