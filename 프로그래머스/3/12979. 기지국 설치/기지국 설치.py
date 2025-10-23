# 이미 설치된거를 기준으로 이전에 몇개가 들어가야하는지 계산
import math
def solution(n, stations, w):
    answer = 0
    idx=1
    r=2*w+1

    for station in stations:
        start=station-w
        if idx<start:
            answer+=math.ceil((start-idx)/r)
        idx=station+w+1

    # 마지막 설치된 기지국 이후 처리
    if idx==n:
        answer+=1
    elif idx<n:
        answer+=math.ceil((n-idx)/r)

    return answer