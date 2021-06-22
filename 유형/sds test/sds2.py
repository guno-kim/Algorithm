import sys
input=sys.stdin.readline
from collections import deque
import copy

def main():
    t=int(input())
    def strToBoard(s):
        for _ in range(6-len(s)):
            s='0'+s
        return list(map(int,s))
    def boardToInt(b):
        return int(''.join(str(i) for i in b))

    for caseNum in range(t):
        origin,target,l=map(int,input().split())
        m=len(str(max(origin,target)))
        f=list(input().rstrip())
        for i in range(l):
            if f[i]=='+':
                f[i]=1
            elif f[i]=='-':
                f[i]=-1
            else:
                f[i]=0
        rf=list(reversed(f))
        filters=[[0]*(6-l-i)+f+[0]*i for i in range(7-l)]+[[0]*(6-l-i)+rf+[0]*i for i in range(7-l)]
        origin=strToBoard(str(origin))
        target=strToBoard(str(target))
        que=deque()
        que.append((origin,0))
        answer=-1
        while que:
            now,cnt=que.popleft()
            isSame,diffIdx,dist=True,0,0
            for i in range(6):
                if now[i]!=target[i]:
                    isSame=False
                    diffIdx=i
                    dist=target[i]-now[i]
                    break
            if isSame:
                answer=cnt
                continue
            nowFilter=[]
            nowFilter=[x for x in filters if all(a==0 for a in x[:diffIdx])]
            if dist<0:
                nowFilter=[x for x in nowFilter if x[diffIdx]==-1]
            else:
                nowFilter=[x for x in nowFilter if x[diffIdx]==1]
            print(nowFilter)
            dist=abs(dist)
            if len(nowFilter)==1:
               que.append(([ now[i]+dist*nowFilter[0][i] for i in range(6)],cnt+dist))

            if len(nowFilter)==2:
                for j in range(dist+1):
                    que.append(([now[i]+j*nowFilter[0][i]+(dist-j)*nowFilter[1][i] for i in range(6)],cnt+dist))

        print('#'+str(caseNum+1),answer)
main()