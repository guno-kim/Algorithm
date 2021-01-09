import sys
input=sys.stdin.readline

N=int(input())

red=[0]*(N)
min_red=[0]*N
green=[0]*N
min_green=[0]*N
blue=[0]*N
min_blue=[0]*N

for i in range(N):
    r,g,b=map(int,input().split())
    red[i]=r
    green[i]=g
    blue[i]=b

min_red[0]=red[0]
min_green[0]=green[0]
min_blue[0]=blue[0]

for i in range(1,N):
    min_red[i]=min(red[i]+min_blue[i-1],red[i]+min_green[i-1])
    min_green[i]=min(green[i]+min_blue[i-1],green[i]+min_red[i-1])
    min_blue[i]=min(blue[i]+min_red[i-1],blue[i]+min_green[i-1])

print(min(min_red[N-1],min_blue[N-1],min_green[N-1]))