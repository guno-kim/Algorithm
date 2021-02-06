import heapq
INF=10**8

def solution(n, s, a, b, fares):
    answer = 0
    edges=[[] for _ in range(n+1)]
    for x,y,z in fares:
        edges[x].append((y,z))
        edges[y].append((x,z))
    print(edges)
    def daik(start):
        dist=[INF]*(n+1)
        dist[start]=0
        q=[(0,start)]
        while q:
            w,v1=heapq.heappop(q)
            for v2,weight in  edges[v1]:
                if dist[v2]> w+weight:
                    dist[v2]=w+weight
                    heapq.heappush(q,(dist[v2],v2))
        return dist

    ds=daik(s)
    da=daik(a)
    db=daik(b)

    answer=min( ds[i]+da[i]+db[i] for i in range(1,n+1))
    return answer

solution(7,3,4,1,	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
