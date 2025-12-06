# 출발-봉우리-출발 에서 사이사이에 최대한 path가 많이 들어가면 intensity가 작아진다.
# 대칭이기 때문에 출발-봉우리까지만 구하면 된다.
# 다음 이동할 때, 갈 수 있는거 중에서 가장 작은 intensity로 가자
# 이를 위해서 heap을 사용한다.
from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    graph=defaultdict(list)
    for u,v,c in paths:
        graph[u].append((v,c))
        graph[v].append((u,c))
    
    intensitys=[float("inf")]*(n+1)
    min_i=float("inf")
    min_n=float("inf")
    
    gates_set=set(gates) # 리스트를 set으로 바꾸면 조회O(1)로 시간 초과 예방 가능
    summits_set=set(summits)
    

    heap=[]
    for start in gates_set:
        intensitys[start]=0
        heapq.heappush(heap,(0,start))
        
    while heap:
        intensity,node=heapq.heappop(heap)
        
        if intensity>intensitys[node]: # min_intensity 보다 크면 탐색할 필요 없음
            continue
        
        if node in summits_set: # 정상
            continue
            
        for u,c in graph[node]:
            new_int=max(intensity,c)
            
            if u in gates_set: # 시작점은 패쓰
                continue
                
            if new_int<intensitys[u]:
                intensitys[u]=new_int
                heapq.heappush(heap,(new_int,u))
            
    summits.sort() # 번호 작은 봉우리부터
    for s in summits:
        if intensitys[s]<min_i:
            min_i=intensitys[s]
            min_n=s 

    return [min_n,min_i]