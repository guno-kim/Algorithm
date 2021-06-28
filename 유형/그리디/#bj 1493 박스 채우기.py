import sys
input=sys.stdin.readline

a,b,c=map(int,input().split())
v=a*b*c
n=int(input())
cubes=[list(map(int,input().split())) for _ in range(n)]
cubes.sort(reverse=True)
cnts=[]
for i in range(n):
    length=cubes[i][0]
    maxCnt=(a>>length)*(b>>length)*(c>>length)
    cubes[i].append(maxCnt)#(length,possible,maxCnt)

cubes[0][1]=min(cubes[0][1],cubes[0][2])
fill=cubes[0][1]
for i in range(1,n):
    lenDist=cubes[i-1][0]-cubes[i][0]
    fill=fill*(8**lenDist)
    cubes[i][1]=min(cubes[i][1],cubes[i][2]-fill)
    fill+=cubes[i][1]


if v!=sum( ((2**length)**3)*cnt for length,cnt,mc in cubes):
    print(-1)
else:
    print(sum(cube[1] for cube in cubes))
