import sys
from pprint import pprint
sys.setrecursionlimit(10 ** 6)

w = int(sys.stdin.readline())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visit = [[0 for _ in range(w)] for _ in range(w)]
grid = []
cnt = 0
for _ in range(w):
    word = list(input())
    grid.append(word)

def dfs(x, y):
    visit[x][y] = 1
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < w and 0 <= next_y < w:
            if visit[next_x][next_y] == 0 and grid[x][y] == grid[next_x][next_y]:
                visit[next_x][next_y] = 1
                dfs(next_x, next_y)

for x in range(w):
    for y in range(w):
        if visit[x][y] == 0:
            dfs(x,y)
            cnt += 1
print(cnt)

for x in range(w):
    for y in range(w):
        if grid[x][y] == "R":
            grid[x][y] = "G"

visit = [[0 for _ in range(w)] for _ in range(w)]
cnt1 = 0
for x in range(w):
    for y in range(w):
        if visit[x][y] == 0:
            dfs(x,y)
            cnt1 += 1
print(cnt1)