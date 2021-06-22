import sys
input=sys.stdin.readline
from collections import deque
import copy

def main():
    INF=100000   
    PRIME=52967 
    T=int(input())
    for caseNum in range(T):
        N=int(input())
        dp=[INF]*PRIME
        cars=[]

        for i in range(1,N+1):
            r,c,d=input().split()
            r=int(r); c=int(c)
            if d=='E':
                cars.append([i,[r,c],False,0])# 처음 좌표, 가로, 이동
            elif d=='W':
                cars.append([i,[r,c+1],False,0])
            elif d=='N':
                cars.append([i,[r+1,c],True,0])
            elif d=='S':
                cars.append([i,[r,c],True,0]) 
    
        def makeMap(cars):
            temp=[[0]*6 for _ in range(6)]
            for i in range(6):
                temp[0][i]=-1;temp[i][0]=-1
            for i,[r,c],isVertical,move in cars:
                if isVertical:#세로
                    temp[r+move][c]=i;temp[r+move-1][c]=i
                else:
                    temp[r][c+move]=i;temp[r][c+move-1]=i
            return temp


        carMap=makeMap(cars)

        def getMoveRange(carMap,car):
            i,[r,c],isVertical,move=car
            moveRange=[]
            if isVertical:#세로
                nowR=r+move;
                for i in [1,2,3]:
                    if nowR+i>5 or carMap[nowR+i][c]!=0:break
                    moveRange.append(i)
                for i in [-1,-2,-3]:
                    if nowR+i-1<0 or carMap[nowR+i-1][c]!=0:break
                    moveRange.append(i)
            else:
                nowC=c+move;
                for i in [1,2,3]:
                    if nowC+i>5 or carMap[r][nowC+i]!=0:break
                    moveRange.append(i)
                for i in [-1,-2,-3]:
                    if nowC+i-1<0 or carMap[r][nowC+i-1]!=0:break
                    moveRange.append(i)
            return moveRange

        def hash(cars):
            temp=0
            for car in cars:
                move=car[-1]
                if move<0:move+=4
                temp+=(4**(car[0]-1))*move
            return temp%PRIME

        que=deque()
        que.append((cars,0))
        answer=INF
        while que:
            cars,cnt=que.popleft()
            h=hash(cars)

            if dp[h]<=cnt or cnt>=answer:
                continue
            else:
                dp[h]=cnt
            carMap=makeMap(cars)
            
            if all(i==0 for i in carMap[3][cars[0][3]+3:6]):
                answer=min(answer,cnt+1)
                continue

            for car in cars:
                moveRange=getMoveRange(carMap,car)
                i,[r,c],isVertical,move=car
                for e in moveRange:
                    newCars=copy.deepcopy(cars)
                    newCars[i-1][3]=move+e
                    que.append((newCars,cnt+1))

        if answer!=INF:
            print('#'+str(caseNum+1),answer)
        else:
            print('#'+str(caseNum+1),-1)
main()