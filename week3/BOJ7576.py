import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
m, n = map(int, sys.stdin.readline().split(" "))
matrix = []

for i in range(n):
    matrix.append((list(map(int, sys.stdin.readline().split(" ")))))

visited = [[-1] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

q = deque()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 0

def bfs():
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and matrix[nx][ny] != -1:
                    visited[nx][ny] = visited[cur_x][cur_y] + 1
                    q.append([nx, ny])

bfs()
answer = -1
isbreak = False
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1 and matrix[i][j] != -1:
            isbreak = True
            break
        elif answer < visited[i][j]:
            answer = visited[i][j]
    if isbreak == True:
        answer = -1
        break

print(answer)

