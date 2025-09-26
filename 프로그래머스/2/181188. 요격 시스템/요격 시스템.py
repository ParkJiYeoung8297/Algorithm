# 개구간 정렬해서 풀기
# 개구간 s,e 제외한 끝점에서 카운트
# 실수라는 점 조심 (등호 없는 부등호 사용하기)
from collections import deque
def solution(targets):
    answer = 0
    # 정렬
    targets.sort()
    targets=deque(targets)
    end=0
    
    # 앞에서 부터 범위 정해두고, 그 구간 안에 있는 애들은 pop 해버리기
    while targets:
        # 목표값보다 나중 시작
        if targets[0][0]<end:
            # 나중 시작, 먼저 끝나는 개구간 일 경우 end 갱신
            if targets[0][1]<end:
                end=targets[0][1]
            targets.popleft()
        else:
            start,end=targets.popleft() # 시작과 끝점
            answer+=1
               
    return answer