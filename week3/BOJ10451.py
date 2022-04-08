import sys
from collections import defaultdict

n = int(sys.stdin.readline())
arr = []
m = []
graph = defaultdict()
for i in range(n):
    m.append(int(sys.stdin.readline()))
    arr.append(list(map(int,input().split(" "))))
    graph[i].append(list(map(int,input().split(" "))))


print(m)
print(arr)

