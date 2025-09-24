import sys
from collections import deque

A=sys.stdin.readline().split()
N=int(A[0])  # 노드
M=int(A[1])  # 에지
V=int(A[2])  # 시작 노드

# 노드와 간선 dict로 저장
graph = {i: [] for i in range(1, N + 1)} 

for i in range(M):
    A=list(map(int,sys.stdin.readline().split()))
    graph[int(A[0])].append(int(A[1]))
    graph[int(A[1])].append(int(A[0]))

# 그래프의 value를 정렬
for key in graph:
    graph[key].sort()

# 방문 여부
visited=[0]*(N+1)
visited[V]=1

# 재귀를 이용한 DFS
def DFS_recursive(graph,v,visited):
    for i in graph[v]:   #해당 노드와 연결된 노드 탐색
        if visited[i]==0: # 방문 안했으면 경로 추가
            visited[i]=1
            X1.append(i)  
            DFS_recursive(graph,i,visited)
    return X1

# 경로
X1=[V]
X1=DFS_recursive(graph,V,visited)  # DFS
print(" ".join(map(str,X1)))


# 재귀를 이용한 BFS
def BFS_recursive(graph,v):
    visited2=[0]*(N+1)
    visited2[V]=1

    queue=deque([v])  # 시작 노드 추가

    while queue:
        s=queue.popleft()
        X2.append(s)
        for i in graph[s]:
            if visited2[i]==0:
                queue.append(i)
                visited2[i]=1

    return X2

X2=[]
X2=BFS_recursive(graph,V)  # DFS
print(" ".join(map(str,X2)))