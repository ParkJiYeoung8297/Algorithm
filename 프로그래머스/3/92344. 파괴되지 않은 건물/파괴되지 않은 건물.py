def solution(board, skill):
    answer = 0
    new_board=[[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    
    
    # 네 모서리만 계산해두고, 옆&밑으로 나중에 한꺼번에 계산하면 됨
    for s in skill:
        t, r1, c1, r2, c2, degree=s
        # 적의 공격
        if t==1:
            new_board[r1][c1]-=degree
            new_board[r1][c2+1]+=degree
            new_board[r2+1][c1]+=degree
            new_board[r2+1][c2+1]-=degree    
        # 아군
        elif t==2:
            new_board[r1][c1]+=degree
            new_board[r1][c2+1]-=degree
            new_board[r2+1][c1]-=degree
            new_board[r2+1][c2+1]+=degree
            
    for y in range(len(board)):
        for x in range(1,len(board[0])):
            new_board[y][x]+=new_board[y][x-1]
            
    for x in range(len(board[0])):
        for y in range(1,len(board)):
            new_board[y][x]+=new_board[y-1][x]
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]+new_board[y][x]>=1:
                answer+=1
        
    
    return answer


