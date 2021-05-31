import sys
from collections import deque
input = sys.stdin.readline
di=[0,0,1,-1]
dj=[1,-1,0,0]
n, m = map(int, input().split())
miro = [list(input().rstrip()) for _ in range(n)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]

q = deque()
q.append((0, 0, False))
res = 1
can = False
while q:
    length = len(q)
    for _ in range(length):
        i, j, x = q.popleft()
        if i == n-1 and j == m-1:
            print(res)
            can = True
            exit()
        for u in range(4):
            ni=i+di[u]; nj=j+dj[u]
            if not (0 <= ni < n and 0 <= nj < m):
                continue
            if miro[ni][nj] == '0':
                if not visited[x][ni][nj]:
                    visited[x][ni][nj] = True
                    q.append((ni, nj, x))
            else:
                if not x and not visited[x][ni][nj]:
                    visited[x][ni][nj] = True
                    q.append((ni, nj, True))

    res += 1

if not can:
    print(-1)

