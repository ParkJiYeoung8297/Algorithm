def solution(n, times):
    answer=float('inf')
    min_time=min(times)
    start=min_time
    end=min_time*n
    
    while (1):
        if end==start:
            break
        mid=(start+end)//2
        count=0
        for i in times:
            count+=mid//i
        # print(start, end, count)
        if count>=n:
            answer=mid
            end=mid # mid도 포함
        else:
            start=mid+1 # mid 포함 안함
        
    
    return answer