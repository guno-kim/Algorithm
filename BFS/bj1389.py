import sys
import copy
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[[0 for _ in range(n+1)]  for _ in range(n+1)]

edge=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

nodes=[]
nextNodes=[]

for i in range(1,n+1):
    visited=[True]+[False]*n
    visited[i]=True
    nodes=[i]
    cnt=0
    while nodes:
        cnt+=1
        nextNodes=[]
        for node in nodes:
            for nextNode in edge[node]:
                if not visited[nextNode]:
                    visited[nextNode]=True
                    arr[i][nextNode]=cnt
                    nextNodes.append(nextNode)
        nodes=copy.deepcopy(nextNodes)
min=int(1e8)
answer=0
for i in range(1,n+1):
    temp=sum(arr[i])
    if min>temp:
        min=temp
        answer=i
print(answer)