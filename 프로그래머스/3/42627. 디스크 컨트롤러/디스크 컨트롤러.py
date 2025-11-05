import heapq
def solution(jobs):
    answer = 0
    total_time=0
    jobs.sort() # 요청 시간이 먼저인거를 앞으로 정렬
    idx=0
    n=len(jobs)
    heap_j=[]
    
    while idx<n or heap_j:
        while idx<n and jobs[idx][0]<=total_time:
            heapq.heappush(heap_j, (jobs[idx][1],jobs[idx][0],idx))
            idx+=1
        
        if heap_j:
            time,start,number=heapq.heappop(heap_j)
            total_time+=time
            answer+=(total_time-start)
        else: # 대기큐에 아무것도 없음, 다음 시작 시간으로 점프
            total_time=jobs[idx][0]
        
    return answer//n