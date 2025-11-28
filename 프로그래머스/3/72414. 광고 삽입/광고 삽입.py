# 시작할 때는 +1, 끝나면 -1을 해서 누적 시청자 수(prefix sum)를 계산하는게 키 포인트!
# 슬라이딩 윈도우 알고리즘으로 최적의 광고 시간 구하기

# 시간 분 초를 초 단위로 바꿈
def change_time(time):
    T=time.split(":")
    hour=int(T[0])*60*60
    minute=int(T[1])*60
    second=int(T[2])
    return hour+minute+second

# 다시 시간:분:초로 바꿈
def return_time(time):
    hour=time//(60*60)
    minute=(time-(hour*60*60))//60
    second=time-(hour*60*60)-minute*60
    times=[str(hour).rjust(2,"0"),str(minute).rjust(2,"0"),str(second).rjust(2,"0")]
    
    return ":".join(times)

def solution(play_time, adv_time, logs):
    answer = ''
    times=[]
    
    for time in logs:
        start,end=time.split("-")
        times.append((change_time(start),change_time(end)))
        
    play=change_time(play_time)
    adv=change_time(adv_time)
    # 시작 시간으로 정렬
    times.sort()
    record=[0]*(play+2)
    prefix_sum=[0]*(play+2)
    
    # 시작점과 끝점 기록
    for start,end in times:
        record[start]+=1
        record[end]-=1
    
    # 누적 시청자 수 구함
    prefix_sum[0]=record[0]
    for i in range(1,len(record)):
        prefix_sum[i]=prefix_sum[i-1]+record[i]
    
    # # 누적 시청 시간 구하기 (시청자가 2명이면, 시청시간도 2배)
    for i in range(1,len(prefix_sum)):
        prefix_sum[i]+=prefix_sum[i-1]
    
    max_view=prefix_sum[adv-1]
    start_time=0
    # 슬라이딩 윈도우로 가장 시청시간이 높은 거 찾기
    for i in range(play-adv+1):
        view=prefix_sum[i+adv-1]-prefix_sum[i-1]
        if view>max_view:
            max_view=view
            start_time=i
            

    return return_time(start_time)