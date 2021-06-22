import sys
input=sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

INF=10**18
minArea=10**18
stones=[]
def main():
    T=int(input())
    for caseNum in range(T):
        global minArea,stones
        minArea=10**18
        N,K=map(int,input().split())
        stones=[]
        for _ in range(N):
            a,b,c=map(int,input().split())
            stones.append((a,b,c-1))
        stones.sort()
        def calc(stoneArr):
            X=max([stone[0] for stone in stoneArr])-min([stone[0] for stone in stoneArr])
            Y=max([stone[1] for stone in stoneArr])-min([stone[1] for stone in stoneArr])
            if X==0:X+=1;
            if Y==0:Y+=1
            return X*Y
        
        exist=[False]*K
        lines,partitions,temp=[],[],[]

        for stone in stones:
            exist[stone[2]]=True
            temp.append(stone)
            if all(exist):
                lines.append(stone[0])
                partitions.append(temp)
                temp=[]
        
        def calcArea(stones):
            global minArea
            if len(stones)<K:
                return False
            for comb in combinations(stones,K):
                types=[False]*K
                for c in comb:types[c[2]]=True
                if not all(types):continue
                minArea=min(minArea,calc(comb))
            return True

        def getArea(s,n):
            global minArea,stones
            if n<K:
                return False
            b=getArea(s+n//2,n-n//2)
            a=getArea(s,n//2)
            if not a and not b:
                return calcArea(stones[s:s+n])
            
            # line=(stones[s+n//2]+stones[s+n//2+1])//2
            # mid=[]
            # for stone in stones:
            #     if line-minArea<=stone[0]<=line+minArea:
            #         mid.append(stone)


        temp=[]
        for i in range(K):
            for stone in stones:
                if stone[2]==i:
                    temp.append(stone)
                    break
        calcArea(temp)

        
        getArea(0,N)
        
        print('#'+str(caseNum+1),minArea)
main()
