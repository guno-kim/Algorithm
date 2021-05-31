import sys

K,N=map(int,sys.stdin.readline().split())

lines=[]
for _ in range(K):
    lines.append(int(input()))

left=1
right=sum(lines)//K+1
while left<right:
    mid=(left+right)//2

    cnt=0
    for line in lines:
        cnt+=line//mid
    if cnt>=N:
        left=mid+1
        answer=mid
    else:
        right=mid

print(answer)

    
