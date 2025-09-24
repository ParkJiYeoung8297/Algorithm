# 조합을 만들어보고, 백트래킹으로 결과 만족 안할 때, 빠꾸해야할거 같은
from itertools import combinations
def solution(n, q, ans):
    answer=0
    list_n=[i for i in range(1,n+1)]
    
    # combinations로 가능한 조합 다 구하기
    cases=map(set,combinations(list_n,5))
    
    # 교집합으로 몇개 맞았는지 계산 (이건 set끼리만 계산 가능, list를 set으로 변환하기)
    for case in cases:
        flag=1
        for idx,list_q in enumerate(q):
            if len(case.intersection(set(list_q)))!=ans[idx]: 
                flag=0
                break
        answer=answer+1 if flag==1 else answer
          
    return answer