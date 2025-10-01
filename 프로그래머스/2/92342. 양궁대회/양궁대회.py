# 중복 조합으로 풀 수 있음
# 중복 조합 구하면, 숫자가 작은 수 부터 순서대로 나오기 떄문에 최대 점수 차이인지만 보면 됨 (이거 중요)
from itertools import combinations_with_replacement
def solution(n, info):
    answer=[]
    score=[i for i in range(11)]
    max_gap=0
    candidate=combinations_with_replacement(score,n)
    

    for cand in candidate:
        # 개수로 변환
        c=[0]*11
        for i in cand:
            c[10-i]+=1

        lion=0
        apeach=0
        
        for i in range(11):
            if c[i]+info[i]==0:
                continue
            if c[i]>info[i]:
                lion+=(10-i)
            elif c[i]<=info[i]:
                apeach+=(10-i)
        if lion>apeach and max_gap<(lion-apeach):
            max_gap=(lion-apeach)
            answer=c
 
    return answer if answer else [-1]