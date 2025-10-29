## dfs는 최단거리를 보장하지 않음. bfs로 풀어야함
from collections import defaultdict
from collections import deque
def solution(n, edge):
    answer = 0
    graph=defaultdict(list)
    visited=[0]*(n+1)
    
    
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(start):
        nonlocal answer
        depth=0
        level=defaultdict(int)
        queue=deque()
        
        queue.append((start,1))
        visited[start]=1
        while queue:
            flag=1
            node,count=queue.popleft()
            level[count]+=1
            depth=max(depth,count)
            for n in graph[node]:
                if visited[n]==0:
                    queue.append((n,count+1))
                    visited[n]=1
        return level[depth]
    
    return dfs(1)