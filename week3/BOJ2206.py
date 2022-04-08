import sys
from collections import deque
from pprint import pprint

x, y = map(int, sys.stdin.readline().split(" "))
visited = [[[-1] * 2 for _ in range(y)] for _ in range(x)]

maze = []
for _ in range(x):
    maze.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append([0, 0, 0])
visited[0][0][0] = 1
while q:
    cur_x, cur_y, count = q.popleft()

    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        if 0 <= next_x < x and 0 <= next_y < y:
            if visited[next_x][next_y][count] == -1:
                if maze[next_x][next_y] == 1 and count == 0 :
                    visited[next_x][next_y][1] = visited[cur_x][cur_y][count] + 1
                    q.append([next_x,next_y,count+1])
                elif maze[next_x][next_y] == 0:
                    visited[next_x][next_y][count] = visited[cur_x][cur_y][count] + 1
                    q.append([next_x,next_y,count])


if visited[x-1][y-1][0] == -1:
    print(visited[x - 1][y - 1][1])
else:
    print(-1)
