# 스타 수열 조건 
# 1) 길이 2이상 짝수 2) 2개씩 묶었을 때, 공통 원소 1개 이상 3) 연속하는 수(2n-2,2n-1)가 같지 않음
# bfs 로 탐색하면, 시간초과 발생 → 그리디 방법으로 변경! 
# 스타 수열에서 공통 원소 X를 포함한 횟수가 수열 길이를 결정한다.
# 따라서, 등장 횟수가 많은 원소를 탐색하면 된다. (2번 조건이 가장 핵심)
from collections import Counter
def solution(a):
    answer = 0
    count=Counter(a)
    
    for key, value in count.items():
        if value*2<answer: # 이미 answer가 더 크다면, 탐색할 필요 없음
            continue
        
        idx=0
        length=0
        while idx<len(a)-1:
            if (a[idx]==key or a[idx+1]==key) and a[idx]!=a[idx+1]:
                length+=2
                idx+=2
            else:
                idx+=1
                
        answer=max(answer,length)
        
    return answer