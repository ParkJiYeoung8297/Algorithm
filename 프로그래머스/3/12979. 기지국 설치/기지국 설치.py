from collections import deque
def solution(n, stations, w):
    answer = 0
    stations=deque(stations)

    idx=0
    while(idx<n):
        if stations:
            # 이미 설치된 기지국 범위보다 작으면 new 설치
            if idx<stations[0]-1-w:
                answer+=1
                idx+=2*w+1
            else:
                idx=stations[0]-1+w+1
                stations.popleft()
            continue
        answer+=1
        idx+=2*w+1

    return answer