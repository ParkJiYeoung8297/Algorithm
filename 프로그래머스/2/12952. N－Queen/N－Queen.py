# 위에서 부터 출발
# Q 두고 나서 아래, 옆을 다 색칠
# 각 행, 각의 열에는 반드시 하나의 Q가 놓여야함 → 안놓이면 중단
# dfs 문제!

def fillColor(y,x,board,n):
    # 가로
    board[y]=[1]*n
    # 세로
    for i in range(n):
        board[i][x]=1
    # 오른쪽 대각선
    n_y,n_x=y,x
    while (1):
        n_y+=1
        n_x+=1
        if n_y==n or n_x==n:
            break
        board[n_y][n_x]=1

    # 왼쪽 대각선
    n_y,n_x=y,x
    while (1):
        n_y+=1
        n_x-=1
        if n_y==n or n_x<0:
            break
        board[n_y][n_x]=1

    
    board[y][x]="Q"
    return board

def solution(n):
    answer=0
    board=[[0]*n for _ in range(n)]
    
    def dfs(y,x):
        stack=[]
        total=0
        stack.append((y,x,board))
        while stack:
            curr_y,curr_x,curr_board=stack.pop()
            
            # 마지막 줄이면 경우의 수 계산
            if curr_y==n-1:
                total+=sum([1 for i in curr_board[curr_y] if i==0])
                continue
            
            # 색칠할 수 있으면 색칠
            new_board=[b.copy() for b in curr_board]
            if curr_board[curr_y][curr_x]==0:
                new_board=fillColor(curr_y,curr_x,new_board,n)
            
            # 다음 가능한 경우들 stack에 추가
            for i in range(n):
                if new_board[curr_y+1][i]==0:
                    stack.append((curr_y+1,i,new_board))  

        return total
                    
        
    
    # 위에서 부터 출발
    for x in range(n):
        answer+=dfs(0,x) 
    return answer