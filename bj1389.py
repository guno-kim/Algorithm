import sys
input=sys.stdin.readline
INF=int(1e8)

n,m=map(int,input().split())
arr=[[INF for _ in range(n+1)]  for _ in range(n+1)]
print(arr[0])

edge=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a][b]=1
    arr[b][a]=1
    edge[a]=b
    edge[b]=a

