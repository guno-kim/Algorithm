def solution(new_id):
    answer = ''
    flag=False

    for c in new_id:
        if not( c.isalpha() or c.isdigit() or c=='-'or c=='_' or c=='.' ):#1
            continue
        if c.isupper():#2
            c=c.lower()
        if c=='.':#3
            if flag:
                continue
            else:
                flag=True
        else:
            flag=False
        answer+=c

    if len(answer) and answer[0]=='.':
        answer=answer[1:]
    if len(answer) and answer[-1]=='.':
        answer=answer[:-1]

    if len(answer)==0:
        answer="a"
    
    if len(answer)>15:
        answer=answer[:15]
    if answer[-1]=='.':
        answer=answer[:-1]
    if len(answer)<=2:
        while len(answer)<3:
            answer+=answer[-1]
    return answer