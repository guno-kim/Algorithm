import sys
input = sys.stdin.readline
N=int(input())
l=list(map(int,input().split()))
s=set(l)
for ele in sorted(s):
    print(ele,end=' ')