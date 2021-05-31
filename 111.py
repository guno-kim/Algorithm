N=int(input())
a = [[0, 0, 0, 0]] + [[1, 0, 0, 0] for i in range(8)] + [[0, 0, 1, 0]]
b = [[0, 0, 0, 0] for i in range(10)]

def print1(arr):
    for i in arr:
        print(i)
for n in range(1, N):
    for i in range(1, 9):
        for f in range(4):
            b[i][f] = a[i - 1][f] + a[i + 1][f]
    for f in [0, 2]:
        b[0][f | 1] = a[1][f] + a[1][f | 1]
        b[0][f | 1] = a[1][f] + a[1][f | 1]
    for f in [0, 1]:
        b[9][f | 2] = a[8][f] + a[8][f | 2]
    c = a
    a = b
    b = c
    for i in a:
        print(i)
    print('--------------')

ret = 0
for s in a:
    ret += s[3]
print(ret % 10**9)