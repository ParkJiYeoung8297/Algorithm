# 1) 왼쪽부터 값을 add 해서 종류 개수 맞을 때까지 확장
# 2) 종류 개수 맞으면 왼쪽 포인터를 오른쪽으로 옮겨서 최소길이 찾음
# 3) 2번 하고나서 개수 0개인거 del 하고 다시 1번으로 돌아감
from collections import defaultdict
def solution(gems):
    answer=[0,100000]
    types=len(set(gems))
    left=0
    count=defaultdict(int)
    
    for right, value in enumerate(gems):
        count[gems[right]]+=1
        
        while len(count)==types:
            if right-left<answer[1]-answer[0]:
                answer=[left+1,right+1]
            count[gems[left]]-=1
            if count[gems[left]]==0:
               del count[gems[left]]
            left+=1
    return answer