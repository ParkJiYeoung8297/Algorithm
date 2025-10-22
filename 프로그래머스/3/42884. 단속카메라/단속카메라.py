# 맨 앞에서 부터 없앰 (level 2요격 시스템이랑 비슷한 문제)
def solution(routes):
    answer = 0
    routes.sort()

    i=0
    while(i<len(routes)):
        answer+=1
        s,e=routes[i]
        cand=e
        for idx in range(i+1,len(routes)):
            ns,ne=routes[idx]
            if ns>cand:
                break
            if ne<cand:
                cand=ne
            i=idx
        i+=1
    return answer