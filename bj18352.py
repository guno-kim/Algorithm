import sys
import copy
from collections import deque
input=sys.stdin.readline

N,M,K,X=map(int,input().split())

edge=[[] for _ in range(N+1)]
visited=[False]*(N+1)
visited[X]=True

for _ in range(M):
    a,b=map(int,input().split())
    edge[a].append(b)

nodes=[]
nextNodes = []

nodes.append(X)
cnt=0
while cnt!=K:
    cnt+=1
    nextNodes=[]
    for node in nodes:
        for next in edge[node]:
            if not visited[next]:
                nextNodes.append(next)
                visited[next]=True
    nodes=copy.deepcopy(nextNodes)

if not nextNodes:
    print(-1)
else:
    for node in nextNodes:
        nextNodes.sort()
        print(node)

