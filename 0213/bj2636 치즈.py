import sys
input=sys.stdin.readline
N,M=map(int,input().split())
MAP=[]
time=0
visited=[[False]*M for _ in range(N)]
for _ in range(N):
    temp=list(map(int,input().split()))
    MAP.append(temp)

d=[(0,1),(0,-1),(1,0),(-1,0)]
stack,air,hole=[(0,0)],[],[]
visited[0][0]=True
while stack:
    c=stack.pop()
    air.append(c)
    for i in range(4):
        nx=c[0]+d[i][0];ny=c[1]+d[i][1];
        if not(0<=nx<N and 0<=ny<M) or visited[nx][ny]:
            continue
        if MAP[nx][ny]:
            continue
        visited[nx][ny]=True
        stack.append((nx,ny))
cnt=0;


while True:
    next_air=[]

    while air:
        c=air.pop()
        for i in range(4):
            nx=c[0]+d[i][0];ny=c[1]+d[i][1];
            if not(0<=nx<N and 0<=ny<M) or visited[nx][ny]:
                continue
            visited[nx][ny]=True
            if MAP[nx][ny]:
                next_air.append((nx,ny))
            else: # 구멍
                air.append((nx,ny))
    if not next_air:
        break
    cnt=len(next_air)
    air=next_air
    time+=1

print(time)
print(cnt)