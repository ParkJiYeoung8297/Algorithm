# 비트 연산자를 이용한 풀이 (아직 이해가 다 안됨)
def solution(beginning, target):
    INF=float('inf')
    answer = INF
    Y=len(beginning)
    X=len(beginning[0])
    
    for mask in range(1<<Y):
        count=0
        flipped_y=[0]*Y
        for y in range(Y):
            if mask&(1<<y):
                flipped_y[y]^=1
        
        flipped_x=[0]*X
        for x in range(X):
            # 첫 행을 고정
            flipped_x[x]=flipped_y[0]^beginning[0][x]^target[0][x]
        
        validate=True
        for y in range(Y):
            for x in range(X):
                if beginning[y][x]^flipped_x[x]^flipped_y[y]!=target[y][x]:
                    validate=False
                    break
            if not validate:
                break
                
        if validate:
            answer=min(answer,sum(flipped_x)+sum(flipped_y))

    return answer if answer!=INF else -1