from collections import deque
def solution(n, t, m, timetable):
    answer = ''
    new_timeTable=[]
    for time in timetable:
        T=list(map(int,time.split(":")))
        new_timeTable.append(T[0]*60+T[1])
    new_timeTable.sort()
    new_timeTable=deque(new_timeTable)
    start=540 # 9시
    
    # n-1개의 셔틀
    for i in range(n-1):
        time=start+i*t
        count=0
        while new_timeTable:
            if new_timeTable[0]<=time:
                new_timeTable.popleft()
                count+=1
            else:
                break
            if count==m:
                break
    # 마지막 셔틀 (이제 진짜 타야함!!)
    last=start+(n-1)*t
    length=len(new_timeTable)
    
    # 마지막 셔틀 지각한 사람 제외
    for time in range(length):
        if time>last:
            new_timeTable.pop()
        else:
            break
           
    if len(new_timeTable)>=m:
        last=min(new_timeTable[m-1]-1,last)
            
    # 시간, 분으로 변환
    hour=str(last//60)
    minute= str(last-60*(last//60))
    return hour.rjust(2,"0")+":"+minute.rjust(2,"0")
    return answer