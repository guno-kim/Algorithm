import sys
N=int(input())
M=int(input())
num=[False]*100001
armors=list(map(int,sys.stdin.readline().split()))

for armor in armors:
    num[armor]=True

if M>=200000:
    print(0)
else:
    cnt=0
    for armor in armors:
        if num[M-armor]:
            cnt+=1
    print(cnt//2)
    
        