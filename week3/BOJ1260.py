import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10 ** 6)

dot, line, start = map(int, sys.stdin.readline().split(" "))
visitDFS = [start]
visitBFS = [start]
graph = defaultdict(list)

for _ in range(line):
    parent, child = map(int, sys.stdin.readline().split(" "))
    graph[parent].append(child)
    graph[child].append(parent)


for i in range(1, dot+1): #문제에 정점 작은거 부터 방문 하라하니까 정렬
    graph[i].sort()

def dfs(s):
    for node in graph[s]:
        if node not in visitDFS:
            visitDFS.append(node)
            dfs(node)
dfs(start)


q = deque()
q.append(start)

while q:
    cur = q.popleft()
    for node in graph[cur]:
        if node not in visitBFS:
            visitBFS.append(node)
            q.append(node)

a = " ".join(str(_)for _ in visitDFS)
print(a)
b = " ".join(str(_)for _ in visitBFS)
print(b)


