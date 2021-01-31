import sys
T=int(input())
INF=10**8
for ___ in range(T):
    N,M,K=map(int,sys.stdin.readline().split())
    edges=[[] for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d=map(int,sys.stdin.readline().split())
        edges[u].append([v,c,d])
    
    dp=[[INF]*(M+1) for _ in range(N+1)] # dp[a][b] a번 노드에 b 비용으로 갈 수 있는 최소거리
    dp[1][0]=0  # 1번에서 비용 0 -> 시간 0
    
    _min=INF

    for money in range(M+1):
        for node in range(1,N+1):
            now_time=dp[node][money]
            if now_time==INF:
                continue
            if node==N and now_time<_min:
                _min=now_time
            for v,c,d in edges[node]:
                if money+c>M or _min<now_time+d:
                    continue
                dp[v][money+c]=min(dp[v][money+c],now_time+d)

    if _min==INF:
        print("Poor KCM")
    else:
        print(_min)

