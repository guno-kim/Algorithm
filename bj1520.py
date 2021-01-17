# ####1
#
# import sys;input=sys.stdin.readline
# m,n=map(int,input().split())
#
# height=[list(map(int,input().split())) for _ in range(m)]
# dx=[0,0,-1,1]
# dy=[1,-1,0,0]
# cnt=[[0 for _ in range(n)] for __ in range(m)]
# cnt[0][0]=1
# list=[]
# start_height=height[0][0]
# end_height=height[m-1][n-1]
# for y in range(m):
#     for x in range(n):
#         if end_height<=height[y][x]<=start_height:
#             list.append((y,x,height[y][x]))
#
# list.sort(key=lambda x:x[2],reverse=True)
#
# for l in list:
#     y=l[0];x=l[1]
#     for i in range(4):
#         ny=y+dy[i]
#         nx=x+dx[i]
#         if 0<=ny<m and 0<=nx<n:
#             if height[y][x]>height[ny][nx]:
#                 cnt[ny][nx]+=cnt[y][x]
#
# print(cnt[m-1][n-1])

####2

# import sys;input=sys.stdin.readline
# sys.setrecursionlimit(999999)
# m,n=map(int,input().split())
# height=[list(map(int,input().split())) for _ in range(m)]
# dx=[0,0,-1,1]
# dy=[1,-1,0,0]
# dp=[[-1 for _ in range(n)] for u in range(m)]
#
# def visit(y,x):
#     if y==m-1 and x==n-1:
#         return 1
#     if dp[y][x]!=-1:
#         return dp[y][x]
#     dp[y][x]=0
#     for i in range(4):
#         ny=y+dy[i]
#         nx=x+dx[i]
#         if 0<=ny<m and 0<=nx<n:
#             if height[ny][nx]<height[y][x]:
#                 dp[y][x]+=visit(ny,nx)
#     return dp[y][x]
# print(visit(0,0))

