import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
a = int(sys.stdin.readline())

for _ in range(a):
    m = int(input())
    startX, startY = map(int, input().split(" "))
    desX, desY = map(int, input().split(" "))

    visit = [[0 for _ in range(m)] for _ in range(m)]

    q = deque()

    q.append([startX, startY])
    while q:
        cur_X, cur_Y = q.popleft()
        if cur_X == desX and cur_Y == desY:
            print(visit[desX][desY])
            break

        for i in range(8):
            newX = cur_X + dx[i]
            newY = cur_Y + dy[i]

            if newX >= 0 and newY >= 0 and newX < m and newY < m:
                if visit[newX][newY] == 0:
                    visit[newX][newY] = visit[cur_X][cur_Y] + 1
                    q.append([newX, newY])



