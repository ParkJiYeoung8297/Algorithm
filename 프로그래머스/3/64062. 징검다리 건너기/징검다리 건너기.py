# 이분 탐색으로 풀어야함
def solution(stones, k):
    answer = 0
    left=1
    right=max(stones)
    while left<=right:
        mid=(left+right)//2
        count=0
        for stone in stones:
            if stone-mid<=0:
                count+=1
            else:
                count=0
            if count==k:
                break
        if count==k: # 기준점 down
            right=mid-1
            answer=mid
        else: # 기준점 up
            left=mid+1
    return answer
            
            
 