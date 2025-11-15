def rotate(board):
    # 90도 회전 (이거 암기하기)
    return list(zip(*board[::-1]))

def check(board,m,n):
    for y in range(n):
        for x in range(n):
            # 1이 아니라는건 2(=돌기가 겹침)이거나 0(홈이 안채워짐)
            if board[m+y-1][m+x-1]!=1:
                return False
    return True

def solution(key, lock):
    answer = False
    m=len(key)
    n=len(lock)
    size=n+2*(m-1)
    board=[[0]*size for _ in range(size)]
    
    for y in range(n):
        for x in range(n):
            board[m+y-1][m+x-1]=lock[y][x]
    
    # 회전 4번 가능
    for _ in range(4):
        key=rotate(key)
        
        for y in range(n+m-1):
            for x in range(n+m-1):
                
                for i in range(m):
                    for j in range(m):
                        board[y+i][x+j]+=key[i][j]
                if check(board,m,n):
                    return True
                
                # 다시 되돌리기
                for i in range(m):
                    for j in range(m):
                        board[y+i][x+j]-=key[i][j]
            

    return answer