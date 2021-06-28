import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
nums=list(map(int,input().split()))
temp=[0]*n

def merge(l,r):
    if l>=r:
        return 0
    m=(l+r)//2
    swap=merge(l,m)+merge(m+1,r)
    i1,i2=l,m+1
    cnt=0
    for j in range(l,r+1):
        if i1>m:
            temp[j]=nums[i2];
            i2+=1
        elif i2>r:
            temp[j]=nums[i1];
            i1+=1
            swap+=cnt
        elif nums[i1]<=nums[i2]:
            temp[j]=nums[i1];
            i1+=1
            swap+=cnt
        else:
            temp[j]=nums[i2];
            i2+=1
            cnt+=1
    for j in range(l,r+1):
        nums[j]=temp[j]
    return swap

print(merge(0,n-1))