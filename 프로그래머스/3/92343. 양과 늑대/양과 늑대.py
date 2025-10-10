# 방법 1) dfs 백트래킹 방법 (트리 안그리고 할 수 있음, 대신 오래 걸림 주의)
def solution(info, edges):
    answer = 0
    visited=[0]*len(info)
    visited[0]=1
    
    def dfs(sheeps,wolves):
        nonlocal answer
        if sheeps>wolves:
            answer=max(answer,sheeps)
        else:
            return
        for parent,child in edges:
            wolf=info[child]==1
            # 부모 → 자식 으로 visited 확인하고 방문
            if visited[parent]==1 and visited[child]==0:
                visited[child]=1
                dfs(sheeps+(not wolf),wolves+wolf)
                visited[child]=0
            
    dfs(1,0) 
    return answer