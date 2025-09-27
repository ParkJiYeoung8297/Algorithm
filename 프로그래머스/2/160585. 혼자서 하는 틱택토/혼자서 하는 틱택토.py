# O와 X의 개수로 푸는 문제
def checkBingo(boards,mark):
    # 가로
    for b in boards:
        if b==[mark,mark,mark]:
            return True
    # 세로
    for i in range(3):
        if boards[0][i]==boards[1][i]==boards[2][i]==mark:
            return True
    
    # 대각선
    if boards[0][0]==boards[1][1]==boards[2][2]==mark:
        return True

    # 대각선
    if boards[0][2]==boards[1][1]==boards[2][0]==mark:
        return True
    return False

def solution(board):
    boards=[list(b) for b in board]
    
    # O와 X의 개수 세기
    count={"O":0,"X":0}
    
    # O보다 X의 개수가 많거나, O가 X 보다 2개 이상 많거나 하면 실패
    for y in range(len(boards)):
        for x in range(len(boards[0])):
            if boards[y][x]=="O":
                count["O"]+=1
            elif boards[y][x]=="X":
                count["X"]+=1
    
    if count["O"]<count["X"] or count["O"]>=count["X"]+2:
        return 0
    
    # O 과 X 개수가 같으면 X가 돌 놓고 종료, O 빙고이면 실패
    if count["O"]==count["X"] and checkBingo(boards,"O"):
        return 0
        
    
    # O 개수가 X 개수보다 1 크다면 O가 돌 놓고 종료, X 빙고이면 실패
    if count["O"]==(count["X"]+1) and checkBingo(boards,"X"):
        return 0
    
    return 1