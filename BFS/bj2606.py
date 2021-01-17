import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
k=int(input())

edge=[[] for _ in range(n+1)]
virus=[0 for _ in range(n+1)]

for _ in range(k):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

q=deque()
q.append(1)

while q:
    temp=q.popleft()
    if virus[temp]:
        continue
    virus[temp]=1
    for next in edge[temp]:
        if not virus[next]:
            q.append(next)

print(sum(virus)-1)

