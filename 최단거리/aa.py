import sys
import heapq

input=sys.stdin.readline

v,e=map(int,input().split())
start=int(input())
INF=int(1e9)
d=[INF]*(v+1)

edge=[[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    edge[a].append((b,c))

d[start]=0
pq=[]
pq.append([0,start])

while pq:
    start_to_mid,mid=heapq.heappop(pq)
    for  end,mid_end in edge[mid]:
        if d[end]>start_to_mid+mid_end:
            d[end] = start_to_mid + mid_end
            duplicate=False
            for node in pq:
                if node[1]==end:
                    node[0]=d[end]
                    duplicate = True
            if not duplicate:
                heapq.heappush(pq,(d[end],end))

for dist in d[1:]:
    if dist == INF:
        print("INF")
    else:
        print(dist)