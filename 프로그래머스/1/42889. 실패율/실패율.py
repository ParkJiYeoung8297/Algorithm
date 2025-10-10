# history 나열 후 개수가 낮은거 부터 출력
from collections import Counter
def solution(N, stages):
    answer = []
    history=[0]*(N+2) # 스테이지 참여한 사람
    fail=[0]*(N+2)    # 스테이지 실패한 사람
    count=Counter(stages)
    history[N]=count[N+1]
    
    for n in range(N,-1,-1):
        history[n]+=count[n]+history[n+1]
        fail[n]+=count[n]
        
    # 2 → 1라운드 통과, 2라운드 참가
    # 3 → 1라운드 통과, 2라운드 통과, 3 라운드 참가
    
    # 이부분이 시간을 많이 씀
    result=[(-(fail[x]/history[x]),x) if history[x]!=0 else (0,x) for x in range(1,N+1) ]
    result.sort()
    answer=[x for f,x in result]
    
    return answer