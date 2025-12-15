# 이분 탐색을 떠올려야 효율성을 해결할 수 있다. (1초 1초 시뮬레이션은 효율성 통과 못함)
# "t초에 완료된 작업수"에 집중하기
def solution(n, cores):
    if len(cores)>n:
        return n

    def count_works(t):
        return sum(t//i+1 for i in cores) # t초에 수행된 작업 개수(t초에 작업 진행 중도 포함)
    
    left, right=0, max(cores)*n
    while left<right:
        mid=(left+right)//2
        if count_works(mid)>=n:
            right=mid
        else:
            left=mid+1
    t=left
    
    already_done=count_works(t-1)
    left_work=n-already_done
    
    for idx,value in enumerate(cores):
        if t%value==0:
            left_work-=1
            if left_work==0:
                return idx+1