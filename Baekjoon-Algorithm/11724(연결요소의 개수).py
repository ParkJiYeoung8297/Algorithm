import sys

A=sys.stdin.readline().split()
N=int(A[0])
M=int(A[1])

# 그래프 저장
graph={i: [] for i in range(1,N+1)}

for i in range(M):
    A=list(map(int,sys.stdin.readline().split()))
    graph[A[0]].append(A[1])
    graph[A[1]].append(A[0])

# 방문 여부
visited=[0]*(N+1)

def DFS_stack(graph,v,visited):
    stack=[v]
    while stack:
        v=stack.pop()
        for i in graph[v]:
            if visited[i]==0:
                stack.append(i)
                visited[i]=1
    return visited

result=0
for i in range(1,N+1):
    if visited[i]==0:
        visited=DFS_stack(graph,i,visited)
        result=result+1

print(result)