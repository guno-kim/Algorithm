import sys
input = sys.stdin.readline
N=int(input())
l=[]
for _ in range(N):
    a,b=map(int,input().split())
    l.append((a,b))

l.sort(key=lambda x:(x[1],x[0]))
# (1,4) (5,5) (4,5)->2
# (1,4) (4,5) (5,5) ->3

cnt=0
limit=0
for ele in l:
    if ele[0]>=limit:
        limit=ele[1]
        cnt+=1
print(cnt)
