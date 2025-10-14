# 맨 처음 시작한 방향과 시작점이 또 나타나면 사이클
# 문제 이해가 어려움..
def solution(grid):
    answer = []
    # y,x   (위, 우, 아래, 좌) → 이게 표준 방향 순서라함 , 이 순서로 안하면 이 문제 풀기 어려움
    dx=[0,1,0,-1]
    dy=[-1,0,1,0]
    
    # 시작점 + 방향까지 체크해야하니 3중 배열
    visited=[[[False]*4 for x in range(len(grid[0]))] for y in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for d in range(4):
                if visited[y][x][d]==False:
                    count=0
                    
                    nx,ny,nd=x,y,d
                    while not visited[ny][nx][nd]:
                        visited[ny][nx][nd]=True
                        count+=1
                        
                        # 이동
                        ny=(ny+dy[nd])%len(grid)
                        nx=(nx+dx[nd])%len(grid[0])
                        
                        if grid[ny][nx]=="L":
                            nd=(nd+3)%4 # 왼쪽 회전은 ↑ ← ↓ →
                        elif grid[ny][nx]=="R":
                            nd=(nd+1)%4 # 오른쪽 회전은 ↑ → ↓ ← 
                        
                    if count>0:
                        answer.append(count)          
                
    return sorted(answer) # 이게 문제 조건!!