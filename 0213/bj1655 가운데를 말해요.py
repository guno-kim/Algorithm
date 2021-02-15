import heapq
import sys
N=int(input())
low=[];high=[];

low.append(-int(input()))
print(-low[0])
for i in range(N-1):
    num=int(sys.stdin.readline())
    if not i%2: #low원소가 하나 더 많은 상태
        if -low[0]<=num:
            heapq.heappush(high,num)
        else:
            mid=-heapq.heappop(low)
            heapq.heappush(high,mid)
            heapq.heappush(low,-num)
    else:
        if high[0]<num:
            mid=heapq.heappop(high)
            heapq.heappush(low,-mid)
            heapq.heappush(high,num)
        else:
            heapq.heappush(low,-num)
    print(-low[0])
