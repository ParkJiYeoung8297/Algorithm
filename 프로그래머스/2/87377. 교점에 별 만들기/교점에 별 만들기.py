# 직선 두 개의 교점 구하기 , 정수면 반환, 아니며 -1 반환
def returnPoint(A,B):
    a,b,e=A
    c,d,f=B
    if (a*d)-(b*c)!=0:
        x=((b*f)-(e*d))/((a*d)-(b*c))
        y=((e*c)-(a*f))/((a*d)-(b*c))
        if x==int(x) and y==int(y):
            return (int(x),int(y))
    return -1

def findBound(A):
    if len(A)==0:
        return (0,0,0,0)
    max_x,max_y=A[0][0],A[0][1]
    min_x,min_y=max_x,max_y

    for xy in A:
        x,y=xy
        if x>max_x:
            max_x=x
        if x<min_x:
            min_x=x
        if y>max_y:
            max_y=y
        if y<min_y:
            min_y=y
    return (abs(max_x-min_x)+1,abs(max_y-min_y)+1,min_x,min_y)

def moveStar(point,min_x,min_y):
    return [[x-min_x,y-min_y] for x,y in point]

def drawStar(board,point):
    h=len(board)
    w=len(board[0]) if h>0 else 0
    for x,y in point:
        if 0<=x<w and 0<=y<h:
            board[len(board)-1-y][x]='*'
    # board.reverse()
    return board

def solution(line):
    answer = []

    point=set()
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            result=returnPoint(line[i],line[j])
            if result!=-1:
                point.add(result)
    point=list(point)
    
    size_x,size_y,min_x,min_y=findBound(point)
    
    # 비어있으면 에러처리
    if size_x==0 or size_y==0:
        return []

    
    # 보드 만들기
    board=[["."]*size_x for _ in range(size_y)]
    
    # 점 이동
    new_point=moveStar(point,min_x,min_y)
    
    # 별 그리기
    new_board=drawStar(board,new_point)
    
    # 정답 만들기
    for b in new_board:
        answer.append("".join(b))
        

    return answer
