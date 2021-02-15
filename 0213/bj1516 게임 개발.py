import sys
from collections import deque
N=int(input())
buildings=[]
time=[0]*(N+1)
for idx in range(1,N+1):
    temp=list(map(int,sys.stdin.readline().split()))
    pre=[]
    for i in temp[1:]:
        if i ==-1:
            break
        pre.append(i)
    buildings.append([idx,temp[0],pre,0])# 번호, 시간, 선수 건물, 이전 건물 최대 건설 완료 시간

buildings.sort(key=lambda x:len(x[2]))

while buildings:
    i=0
    while len(buildings[i][2])==0:
        idx=buildings[i][0]
        time[idx]=buildings[i][1]+buildings[i][3]
        i+=1

        for b in buildings:
            if idx in b[2]:
                b[2].remove(idx)
                if b[3]<time[idx]:
                    b[3]=time[idx]
        if i==len(buildings):
            break
    buildings=buildings[i:]
    buildings.sort(key=lambda x:len(x[2]))

for t in time[1:]:
    print(t)  