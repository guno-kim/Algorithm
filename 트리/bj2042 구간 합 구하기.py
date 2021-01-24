import sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
n=1;
while n<N:
    n*=2
segment=[0]*(2*n)
for i in range(N):
    segment[n+i]=int(input())

for i in range(n-1,0,-1):
    segment[i]=segment[2*i]+segment[2*i+1]


def update(idx):
    idx=idx//2
    if idx==0:
        return
    segment[idx]=segment[2*idx]+segment[2*idx+1]
    update(idx)

def sum(idx,start,end,left,right):
    if end<left or right<start:
        return 0
    elif left<=start and end<=right:
        return segment[idx]
    else:
        return sum(idx*2,start,(start+end)//2,left,right)+ sum(idx*2+1,(start+end)//2+1,end,left,right)

for _ in range(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        segment[n+b-1]=c
        update(n+b-1)
    else:
        print(sum(1,1,n,b,c))