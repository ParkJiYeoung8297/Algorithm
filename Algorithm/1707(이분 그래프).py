import sys

K=int(input())

# DFS 
def DFS_stack(graph,v,visited):
    stack=[v] #시작 노드
    visited[v]=1 # 시작노드 색칠

    while stack:
        v=stack.pop()
        for i in graph[v]:
            if visited[i]==-1:
                visited[i]=1-visited[v]
                stack.append(i)
            else:
                if visited[i]==visited[v]:   # 인접한 노드에 같은 색으로 칠해지는 경우
                    return "NO"
    return "YES"

for i in range(K):
    V, E = map(int, sys.stdin.readline().split())  # 노드 , 간선

    # 그래프
    graph={k:[] for k in range(1,V+1)}
    
    for j in range(E):
        u,v=map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # 방문 여부
    visited=[-1]*(V+1)

    for i in range(1,V+1):
        if visited[i]==-1:
            result=DFS_stack(graph,i,visited)
            if result=="NO":
                break
        
    print(result)