N=int(input())
stair= [0]
for _ in range(N):
    stair.append(int(input()))

score1=[0 for _ in range(N+1)]
score2=[0 for _ in range(N+1)]
score1[1]=stair[1]
score2[1]=stair[1]

for i in range(2,N+1):
    score1[i]=max(score1[i-2],score2[i-2])+stair[i]
    score2[i]=score1[i-1]+stair[i]

print(max(score1[N],score2[N]))