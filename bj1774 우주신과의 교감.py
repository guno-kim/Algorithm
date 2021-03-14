import sys

N,M=map(int,sys.stdin.readline().split())
gods=[(0,0)]
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    gods.append((a,b))
    