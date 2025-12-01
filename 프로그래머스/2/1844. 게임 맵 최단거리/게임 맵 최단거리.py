from collections import deque
def solution(maps):
    direction=[(1,0),(-1,0),(0,1),(0,-1)]
    
    def bfs(y,x,c):
        visited=[[0]*len(maps[0]) for _ in range(len(maps))]
        visited[y][x]=1
        queue=deque()
        queue.append((y,x,c)) # y,x,cost
        while queue:
            cy,cx,cost=queue.popleft()
            visited[cy][cx]=1
            if cy==len(maps)-1 and cx==len(maps[0])-1:
                return cost
            
            for dir in direction:
                ny=cy+dir[0]
                nx=cx+dir[1]
                if 0<=ny<len(maps) and 0<=nx<len(maps[0]) and maps[ny][nx]==1 and visited[ny][nx]==0:
                    queue.append((ny,nx,cost+1))
                    visited[ny][nx]=1
        return -1
                
    return bfs(0,0,1)  