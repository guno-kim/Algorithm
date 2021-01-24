import sys
import heapq
input=sys.stdin.readline
INF=int(1e8)

N,M,X=map(int,input().split())

edge=[[] for _ in range(N+1)]
edge_rev=[[] for _ in range(N+1)]

dist=[INF]*(N+1)
dist[X]=0
dist_rev=[INF]*(N+1)
dist_rev[X]=0

for _ in range(M):
    a,b,c=map(int,input().split())
    edge[a].append((b,c))
    edge_rev[b].append((a,c))

def dijk(dist,edge):
    pq=[]
    pq.append((0,X))
    while pq:
        s_mid_weight,mid=heapq.heappop(pq)
        for end,mid_end_weight in edge[mid]:
            if dist[end]> s_mid_weight+mid_end_weight:
                dist[end] = s_mid_weight + mid_end_weight
                heapq.heappush(pq,(dist[end],end))

dijk(dist,edge)
dijk(dist_rev,edge_rev)
dist[0]=0
dist_rev[0]=0
print(max([i+j for i,j in zip(dist,dist_rev) ]))