def solution(n, times):
    answer=float('inf')
    min_time=min(times)
    start=min_time
    end=min_time*n # 이렇게 안하면 시간 초과남 (젤 적게 걸리는 애 혼자 다 처리하는게 최대)
    
    while (1):
        if end==start:
            break
        mid=(start+end)//2
        count=0
        for i in times:
            count+=mid//i
        # print(start, end, count)
        if count>=n:
            answer=mid # 이거 갱신 부분(내가 잘 놓치는 파트) → 조건 만족하면 값 갱신
            end=mid # mid도 포함
        else:
            start=mid+1 # mid 포함 안함
        
    return answer