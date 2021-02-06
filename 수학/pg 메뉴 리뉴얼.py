def solution(orders, course):
    answer = []
    candidates={}

    for order in orders:
        order=''.join(sorted(order))
        _len=len(order)
        arrs=[]
        for i in range(_len):
            temp=[]
            temp.append(i)
            arrs.append(temp)
        cnt=1
        while True:
            narrs=[]
            for arr in arrs:
                for j in range(arr[-1]+1,_len):
                    temp=list(arr)
                    temp.append(j)
                    narrs.append(temp)
            arrs=narrs
            cnt+=1
            if cnt in course:
                for arr in arrs:
                    temp=""
                    for i in arr:
                        temp+=order[i]
                    if temp in candidates.keys():
                        candidates[temp]+=1
                    else:
                        candidates[temp]=1
            if cnt==_len or cnt==course[-1]:
                break
    result={}
    for i in course:
        result[i]={'max':2,"arr":[]}
    
    for c in candidates.items():
        
        now_result=result[len(c[0])]

        if c[1]==now_result["max"]:
            now_result['arr'].append(c[0])
        if c[1]>now_result["max"]:
            now_result['arr'].clear()
            now_result['arr'].append(c[0])
            now_result['max']=c[1]
    
    for obj in result.values():
        answer.extend(obj['arr'])
    answer.sort()
    return answer



#------------찾아본 코드 itertools, counter 사용하면 간단하게 풀이가능
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        print(most_ordered)
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])