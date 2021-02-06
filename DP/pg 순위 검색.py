# java 1 cpp 2 python 3
# frontend 1 backend 2
# junior 1 senior 2
# chicken 1 pizza 2

def trans1(a):
    if a=='java': return 1
    if a=='cpp': return 2
    if a=='python': return 3
    else: return 0
def trans2(a):
    if a=='frontend': return 1
    if a=='backend': return 2
    else: return 0

def trans3(a):
    if a=='junior': return 1
    if a=='senior': return 2
    else: return 0

def trans4(a):
    if a=='chicken': return 1
    if a=='pizza': return 2
    else: return 0

def binSearch(_list,score,left,right):
    if left==right:
        return left
    mid=int((left+right)/2)
    if _list[mid]<score:
        return binSearch(_list,score,mid+1,right)
    else:
        return binSearch(_list,score,left,mid)
def solution(info, query):
    answer = []
    scores=[[ [ [ [] for _ in range(3) ] for _ in range(3) ] for _ in range(3) ] for _ in range(4)]
    infos=[]; querys=[];
    for _info in info:
        a,b,c,d,e=_info.split(" ")

        for _a in [0,trans1(a)]:
            for _b in [0,trans2(b)]:
                for _c in [0,trans3(c)]:
                    for _d in [0,trans4(d)]:
                        scores[_a][_b][_c][_d].append(int(e))

    for s1 in scores:
        for s2 in s1:
            for s3 in s2:
                for s4 in s3:
                    s4.sort()

    for _query in query:
        a,b,c,d=_query.split(" and ")
        e,f=d.split(" ")
        score=scores[trans1(a)][trans2(b)][trans3(c)][trans4(e)]
        if len(score):
            idx=binSearch(score,int(f),0,len(score)-1)
            cnt=len(score)-idx
            if score[-1]<int(f):
                cnt=0
            answer.append(cnt)
        else:
            answer.append(0)
    return answer



solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])