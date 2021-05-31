N=int(input())
guitars=[]
for _ in range(N):
    guitars.append(input())

def key2(g):
    sum=0
    for c in g:
        if c.isdecimal():
            sum=sum+int(c)
    return sum

a=sorted(guitars,key=lambda x: (len(x),key2(x),x))
for i in a:
    print(i)