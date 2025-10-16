from collections import defaultdict
def solution(n, computers):
    answer = 0
    visited=[0]*n
    graph=defaultdict(list)
    for idx,computer in enumerate(computers):
        for i in range(len(computer)):
            if i==idx:
                continue
            if computer[i]==1:
                graph[idx].append(i)
    
    def dfs(n):
        stack=[]
        stack.append(n)
        
        while stack:
            s=stack.pop()
            visited[s]=1
            for i in graph[s]:
                if visited[i]==0:
                    stack.append(i)

    
    for i in range(n):
        if visited[i]==0:
            dfs(i)
            answer+=1
            

    return answer