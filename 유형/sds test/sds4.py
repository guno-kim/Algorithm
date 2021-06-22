import sys
input=sys.stdin.readline
from collections import deque
import copy

def main():
    T=int(input())
    for caseNum in range(T):
        n,k=map(int,input().split())

        lock=[input() for _ in range(k)]
        rings=list(list(map(int,list(lock[j][i] for j in range(k)))) for i in range(n))
        dists=[]
        for ring in rings:
            start=ring.index(1)
            rightDists,leftDists=[0]*k,[0]*k
            i=start;dist=0
            while True:
                if ring[i]:#1일때
                    dist=0    
                rightDists[i]=dist
                i+=1;dist+=1
                if i>=k:i-=k
                if i==start:break
            while True:
                if ring[i]:#1일때
                    dist=0    
                leftDists[i]=dist
                i-=1;dist+=1
                if i<0:i+=k
                if i==start:break
            ringDist=list(min(leftDists[i],rightDists[i]) for i in range(k))
            dists.append(ringDist)
        answer=min(sum(dists[j][i] for j in range(n)) for i in range(k))
        print('#'+str(caseNum+1),answer)
main()