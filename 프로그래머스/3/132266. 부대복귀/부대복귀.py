from collections import defaultdict
from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    road=defaultdict(list)
    for u,v in roads:
        road[u].append(v)
        road[v].append(u)
        
    def dikstra(position):
        checked=[0]*(n+1)
        distance=[float('inf')]*(n+1)

        queue=deque()
        queue.append((position,0))
        while queue:
            node,dist=queue.popleft()
            if distance[node]>dist:
                distance[node]=dist
            
            if checked[node]==1:
                continue
            checked[node]=1
            
            for i in road[node]:
                if checked[i]==0:
                    queue.append((i,dist+1)) 
        return distance
    
    # 목적지를 start로 각 지점까지의 최단거리 구하기
    # 저장한 값으로 한번에 정답 출려 (즉, 탐색은 한번만)
    memory=dikstra(destination)
    for s in sources:
        if memory[s]==float('inf'):
            answer.append(-1)
        else:
            answer.append(memory[s])
        
    return answer