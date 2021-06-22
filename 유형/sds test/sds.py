import sys
from itertools import combinations
import copy
input=sys.stdin.readline

t=int(input())
for caseNum in range(t):
    n=int(input())
    times=list(map(int,input().split()))
    times.sort()
    dp=[1000000]*(2**n)
    def rToTime(r):
        return [times[i] for i in r]
    def rToBit(r):
        return sum([1<<i for i in r])

    def rec(l,r,_sum):
        if dp[rToBit(r)]<_sum:
            return
        else:
            dp[rToBit(r)]=_sum

        if len(r)==1 or len(r)==2:
            dp[0]=min(dp[0],_sum+max(rToTime(r)))
            return

        for a,b in combinations(r,2):
            temp=0
            tempL,tempR=copy.deepcopy(l),copy.deepcopy(r)
            tempL.append(a);    tempL.append(b);
            tempR.remove(a);    tempR.remove(b);
            tempL.sort();   
            rideCamel=tempL.pop(0)
            tempR.append(rideCamel)#오른쪽으로 이동
            rec(tempL,tempR,_sum+max(times[a],times[b])+times[rideCamel])

    rec([],[i for i in range(n)],0)
    print('#'+str(caseNum+1),dp[0])