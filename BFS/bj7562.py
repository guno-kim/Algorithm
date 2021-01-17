import sys
from collections import deque
input=sys.stdin.readline

times=int(input())
dx = [1, -1, 1, -1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

for ___ in range(times):
    n=int(input())
    sx,sy=map(int,input().split())
    ex,ey=map(int,input().split())
    dist=[[-1]*n for _ in range(n)]
    dist[sx][sy]=1
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if x==ex and y==ey:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if dist[nx][ny] != -1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
    print(dist[ex][ey]-1)