import sys
import copy
input=sys.stdin.readline

n,answer=int(input()),10000
coins=[input() for _ in range(n)]
coins=list(map(lambda coin:sum(1<<(n-i-1)
    for i in range(n) if coin[i]=='T'),coins))

for r in range(1<<n):
    now_coins=copy.deepcopy(coins)
    now_sum=0
    for i in range(n):
        now_coins[i]^=r

    for i in range(n):
        temp=bin(now_coins[i]).count('1')
        now_sum+=min(temp,n-temp)
    answer=min(answer,now_sum)

print(answer)
        