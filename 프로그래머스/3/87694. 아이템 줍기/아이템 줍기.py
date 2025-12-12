# 직사각형에 해당하는 부분을 모두 1로 채우고, 경계선 제외 내부는 0으로 채움 (즉, 경계만 남도록)
# board[y][x]=1이면서 방문 안한곳을 이동해, bfs로 답을 구한다.
# 가장 핵심은 *2를 해야한다는 점이다❗️ (선분을 matrix 한칸으로 표시하기 위함)
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    board=[[0]*101 for _ in range(101)]
    
    # 테두리를 1로 칠함
    for x1,y1,x2,y2 in rectangle:
        x1,y1,x2,y2=x1*2,y1*2,x2*2,y2*2
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                board[j][i]=1
                
    # 해당 영역 테두리를 제외하고 0으로 채움      
    for x1,y1,x2,y2 in rectangle:
        x1,y1,x2,y2=x1*2,y1*2,x2*2,y2*2
        for i in range(x1+1,x2):
            for j in range(y1+1,y2):
                board[j][i]=0

    
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    dq=deque()
    dq.append((characterX*2,characterY*2,0))
    visited=[[0]*101 for _ in range(101)]
    visited[characterY*2][characterX*2]=1
    
    while dq:
        cx,cy,cdist=dq.popleft()
        
        if cx==itemX*2 and cy==itemY*2:
            return cdist//2
        
        for d in directions:
            nx,ny=cx+d[0], cy+d[1]
            if 0<=nx<101 and 0<=ny<101:
                if visited[ny][nx]==0 and board[ny][nx]==1:
                    visited[ny][nx]=1
                    dq.append((nx,ny,cdist+1))