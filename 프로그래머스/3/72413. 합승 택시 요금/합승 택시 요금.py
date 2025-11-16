# 아이디어가 생각하기 어려움 (답안 참고함)
# 출발지에서 도착지가 아니라, 
# 출발지(s)와 도착지(a,b)에서 각 노드까지의 최소거리를 구하고 (어디서 합승할 것인가를 구하는 것임)
# S[i]+A[i]+B[i] 합을 구하면 정답

from collections import defaultdict
import heapq
def solution(n, s, a, b, fares):
    answer = float('inf')
    graph=defaultdict(list)
    
    for u,v,c in fares:
        graph[u].append((v,c))
        graph[v].append((u,c))
        
    def dikstra(start):
        dist=[float('inf')]*(n+1)
        dist[start]=0
        heap=[(0,start)] # 비용,노드
        
        while heap:
            cost, node = heapq.heappop(heap)
            
            if cost > dist[node]:
                continue
            
            min_cost=0
            for v,c in graph[node]:
                new_cost=cost+c
                if new_cost<dist[v]:
                    dist[v]=new_cost
                    heapq.heappush(heap,(new_cost,v))
            
        return dist
    
    # s,a,b 에서 각 노드까지 최소비용 구하기
    S=dikstra(s)
    A=dikstra(a)
    B=dikstra(b)
    
    # S[i]+A[i]+B[i] 중 최소값 구하기
    for i in range(1,n+1):
        answer=min(S[i]+A[i]+B[i],answer)

    return answer