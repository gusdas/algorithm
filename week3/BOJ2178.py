from collections import deque
from pprint import pprint
import sys

x, y = map(int, sys.stdin.readline().split(" "))
maze = [0] * x
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[0 for _ in range(y)] for _ in range(x)]
visited[0][0] = 1
for i in range(x):
    arr = list(input())
    maze[i] = arr

cnt = sys.maxsize


def dfs(cur_x, cur_y, route):

    global cnt
    if cur_x == x - 1 and cur_y == y - 1:
        cnt = min(cnt, route)
        return

    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        if 0 <= next_x < x and 0 <= next_y < y and maze[next_x][next_y] == '1':
                if visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    dfs(next_x, next_y, route + 1)
                    visited[next_x][next_y] = 0

dfs(0, 0, 1)


#
# q = deque()
# q.append([0, 0])
# visited[0][0] = 1
#
# while q:
#     cur_x, cur_y = q.popleft()
#
#     for i in range(4):
#         next_x = cur_x + dx[i]
#         next_y = cur_y + dy[i]
#
#         if next_x >= 0 and next_x < x and next_y >= 0 and next_y < y:
#             if maze[next_x][next_y] == '0':
#                 continue
#             else:
#                 if visited[next_x][next_y] == 0:
#                     q.append([next_x, next_y])
#                     visited[next_x][next_y] = visited[cur_x][cur_y] + 1
#
# print(visited)
# ====================================================================================================================================
