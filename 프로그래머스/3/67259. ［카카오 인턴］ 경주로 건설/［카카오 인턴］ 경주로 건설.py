from collections import deque
def solution(board):
    answer=float('inf')
    visited=[[[float('inf')]*len(board) for _ in range(len(board))] for d in range(4)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    # 하 :0 , 상 : 1, 우 : 2, 좌 : 3
    
    def bfs(y,x):
        nonlocal answer
        queue=deque()
        if board[y+1][x]==0:
            queue.append((y+1,x,0,100)) # 하
            visited[0][y+1][x] = 100
        if board[y][x+1]==0:
            queue.append((y,x+1,2,100)) # 우
            visited[2][y][x+1] = 100
        while queue:
            ny,nx,nd,ncost=queue.popleft()
            if ny==len(board)-1 and nx==len(board)-1:
                answer=min(ncost,answer)
                continue

            for i in range(4):
                dy,dx=ny+directions[i][0],nx+directions[i][1]
                if dy>=len(board) or dx>=len(board) or dy<0 or dx<0:
                    continue
                new_cost=ncost+100 if i==nd else ncost+600
                if board[dy][dx]==0 and new_cost<visited[i][dy][dx]:
                    visited[i][dy][dx]=new_cost
                    queue.append((dy,dx,i,new_cost))
      
    bfs(0,0)
    
    return answer