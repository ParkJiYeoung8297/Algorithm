def solution(n, results):
    answer = 0

    graph=[[False]*(n+1) for _ in range(n+1)]
    
    for u,v in results:
        graph[u][v]=True
        
    # Floyd-Warshall (k-1까지의 결과에서 k를 추가했을 떄를 이용한 알고리즘)
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k]==True and graph[k][j]==True:
                    graph[i][j]=True
    answer=0
    for i in range(1,n+1):
        win = sum(graph[i])  # i 가 이긴 사람 수
        lose = sum([graph[j][i] for j in range(1,n+1)]) # j가 진 사람 수
        if win+lose==n-1:
            answer+=1
    return answer