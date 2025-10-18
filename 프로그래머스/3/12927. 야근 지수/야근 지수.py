# 힙 구조를 이용해서 제일 숫자가 큰 것을 낮춤
import heapq
def solution(n, works):
    answer = 0
    overload=sum(works)-n
    re_works=[-i for i in works] # - 취해서 큰 값이 위에 오도록
    heapq.heapify(re_works)
    if overload>0:
        while n>0:
            work=heapq.heappop(re_works)
            heapq.heappush(re_works,work+1)
            n-=1
        answer=sum([i**2 for i in re_works])
            
    return answer