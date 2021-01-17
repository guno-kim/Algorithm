from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n,m=map(int,input().split())

dist=[[-1]*m for _ in range(n)]

_map = [list(map(int, list(input()))) for _ in range(n)]
q=deque()
q.append((0,0))
dist[0][0]=1
while q:
    x,y=q.popleft()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if not ( 0<=nx<n and 0<=ny<m ):
            continue
        if dist[nx][ny] != -1 or _map[nx][ny]==0:
            continue
        dist[nx][ny]=dist[x][y]+1
        q.append((nx,ny))
print(dist[n-1][m-1])