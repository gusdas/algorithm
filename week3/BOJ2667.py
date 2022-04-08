import sys
from collections import deque

w = int(sys.stdin.readline())
map1 = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited = [[0] * w for _ in range(w)]

for _ in range(w):
    map1.append(list(map(int, input())))


def bfs(x,y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    cnt = 0
    while q:
        cur_x, cur_y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < w and 0 <= ny < w:
                if visited[nx][ny] == 0 and map1[nx][ny] == 1:
                    map1[nx][ny] = 0
                    q.append([nx,ny])
    return cnt

arr = []
for i in range(w):
    for j in range(w):
        if map1[i][j] == 1:
            arr.append(bfs(i, j))


print(len(arr))
for i in sorted(arr):
    print(i)



# def dfs(x, y):
#     global cnt
#     visited[x][y] = 1
#     if map1[x][y] == 1:
#         cnt += 1
#     for i in range(4):
#         next_x = x + dx[i]
#         next_y = y + dy[i]
#         if 0 <= next_x < w and 0 <= next_y < w:
#             if visited[next_x][next_y] == 0 and map1[next_x][next_y] == 1:
#                 dfs(next_x, next_y)
#
#
# arr = []
# cnt = 0
# for i in range(w):
#     for j in range(w):
#         if visited[i][j] == 0 and map1[i][j] == 1:
#             dfs(i, j)
#             arr.append(cnt)
#             cnt = 0
#
# print(len(arr))
# for i in sorted(arr):
#     print(i)
