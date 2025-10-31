from collections import defaultdict
from collections import deque
def solution(tickets):
    answer = []
    region=set()
    dict_r=defaultdict(list)
    visited=defaultdict(int)
    
    
    for s,e in tickets:
        region.add(s)
        region.add(e)
        dict_r[s].append(e)
        visited[(s,e)]+=1
    # 알파벳순으로 앞선 답을 고르니, 미리 정렬해두기
    for k in dict_r.keys():
        dict_r[k].sort()

    def bfs(start,visited):
        queue=deque()
        queue.append((start,[start],visited))
        cand=[]
        while queue:
            s,route,new_visited=queue.popleft()
            
            if len(route)==len(tickets)+1:
                return route
            
            for r in sorted(dict_r[s]):
                if new_visited[(s,r)]>=1:
                    new_route=route.copy()
                    new_route.append(r)
                    
                    new_visited[(s,r)]-=1
                    queue.append((r,new_route,new_visited.copy()))
                    new_visited[(s,r)]+=1          
    # 첫 시작은 인천
    answer=bfs("ICN",visited)
    return answer