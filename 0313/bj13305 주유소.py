import sys
n=int(input())
roads=list(map(int,sys.stdin.readline().split()))
prices=list(map(int,sys.stdin.readline().split()))

result,cnt=0,1
min_price,dist=prices[0],0

while cnt<n:
    dist+=roads[cnt-1]
    if prices[cnt]<min_price:
        result+=min_price*dist
        min_price=prices[cnt]
        dist=0
    cnt+=1
result+=min_price*dist
print(result)