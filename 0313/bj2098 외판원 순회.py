import sys
n=int(input())
weight=[ list(map(int,sys.stdin.readline().split())) for _ in range(n) ]
INF=10**8
dp=[[INF]*(1<<n) for _ in range(n)]

def tsp(last,visited):#visited 이외에 뒷부분 회귀경로의 최소값
    if visited==(1<<n)-1:
        return weight[last][0] or INF
    if dp[last][visited]!=INF:
        return dp[last][visited]

    temp=INF
    for i in range(1,n):
        if visited & (1<<i)==0 and weight[last][i]:
            temp=min(temp,tsp(i,visited|(1<<i))+weight[last][i])
    dp[last][visited]=temp
    return temp
print(tsp(0,1))
