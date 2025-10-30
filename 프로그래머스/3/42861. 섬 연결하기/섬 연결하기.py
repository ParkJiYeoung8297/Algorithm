#  최소 신장 트리 문제 (PRIM 사용)
from collections import defaultdict
import heapq
def solution(n, costs):
    answer = 0
    graph=defaultdict(list)
    dist=dict()
    cost=[float('inf')]*n # 시작 노드 부터 각 노드까지 최소비용
    visited=[0]*n # 해당 노드에 연결된 노드 탐색 끝
    parent=[None]*n # 해당 노드에서 최소 간선의 길이로 연결된 노드
    cost[0]=0
    
    for u,v,w in costs:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    Q=[(0,0)] # cost, start
    while Q:
        curr_cost, start=heapq.heappop(Q)
        if visited[start]:
            continue
        visited[start]=1
        
        answer+=curr_cost

        # 새로운 탐색
        for v,w in graph[start]:
            if visited[v]==0 and w<cost[v]:
                parent[v]=start
                cost[v]=w
                heapq.heappush(Q,(w,v))
                
   
    return answer