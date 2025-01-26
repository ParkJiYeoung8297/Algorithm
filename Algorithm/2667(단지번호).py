import sys

N=int(input())

#그래프 N*N matrix
graph=[]

for i in range(N):
    A=list(sys.stdin.readline().strip())
    A=list(map(int,A))
    graph.append(A)

# 방문 여부 N*N matrix
visited = [[0] * N for _ in range(N)]  # 올바른 방식


def DFS_stack(graph,u,v,visited,apart_NO):
    n=0 #단지 내에 아파트 개수
    stack=[[u,v]]
    while (stack):
        u,v= map(int,stack.pop())
        if visited[u][v]==0 and graph[u][v]!=0: # 집이 있음 & 방문 안함
            graph[u][v]=apart_NO         # 아파트 단지 색칠
            n=n+1                        # 색칠할 때마다 개수 세기
            visited[u][v]=1

            if u+1<N:
                if visited[u+1][v]==0 and graph[u+1][v]!=0: # 아래쪽 탐색
                    stack.append([u+1,v])
                else:
                    visited[u+1][v]=1
                
            if v+1<N:
                if visited[u][v+1]==0 and graph[u][v+1]!=0: # 오른쪽 탐색
                    stack.append([u,v+1])
                else:
                    visited[u][v+1]=1

            if 0<=u-1:
                if visited[u-1][v]==0 and graph[u-1][v]!=0: # 위쪽 탐색
                    stack.append([u-1,v])
                else:
                    visited[u-1][v]=1
            
            if 0<=v-1:
                if visited[u][v-1]==0 and graph[u][v-1]!=0: # 왼쪽 탐색
                    stack.append([u,v-1])
                else:
                    visited[u][v-1]=1
        else:
             visited[u][v]=1
    return graph, visited, apart_NO, n

apart_NO=2  
result=[]
for i in range(N):
     for j in range(N):
        if graph[i][j]==0:
            visited[i][j]=1
        else:
            if visited[i][j]==0:
                graph, visited, apart_NO, n=DFS_stack(graph,i,j,visited,apart_NO)
                result.append(n)
                apart_NO=apart_NO+1

result.sort() # 오름차순 정렬
print(len(result))
for i in range(len(result)):
    print(result[i])