def solution(m, n, puddles):
    board=[[0]*(m+1) for _ in range(n+1)]
    for y in range(1,n+1):
        board[y][1]=1
    for x in range(1,m+1):
        board[1][x]=1
    
    for px,py in puddles:
        board[py][px]=-1
        
    # 오른쪽, 아래로만 이동 가능 = 왼쪽/위의 값이 연못이 아니면 더함
    for cy in range(1,n+1):
        for cx in range(1,m+1):
            if cy==1 and cx==1:
                continue
            if 1<=cy<=n and 1<=cx<=m and board[cy-1][cx]!=-1 and board[cy][cx]!=-1 and board[cy][cx-1]!=-1:
                board[cy][cx]=board[cy-1][cx]+board[cy][cx-1]

            elif 1<=cy<=n and board[cy-1][cx]!=-1 and board[cy][cx]!=-1:
                board[cy][cx]=board[cy-1][cx]

            elif 1<=cx<=m and board[cy][cx-1]!=-1 and board[cy][cx]!=-1:
                board[cy][cx]=board[cy][cx-1]

    return (board[n][m])%1000000007 # 칸 수여서 마지막+1은 뻄