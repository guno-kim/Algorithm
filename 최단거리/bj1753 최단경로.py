import sys
import heapq
input=sys.stdin.readline
INF=int(1e8)

V,E=map(int,input().split())
start=int(input())
node=[[] for _ in range(V + 1)]

for _ in range(E):
    mid,_to,w=map(int,input().split())
    node[mid].append((_to,w))

dist=[INF]*(V+1)
dist[start]=0
pque=[]
heapq.heappush(pque,(0,start))

while pque:
    midDist, mid=heapq.heappop(pque)

    for _to,w in node[mid]:
        newDist=w+midDist
        if newDist<dist[_to]:
            dist[_to]=newDist
            heapq.heappush(pque,(newDist,_to))

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])