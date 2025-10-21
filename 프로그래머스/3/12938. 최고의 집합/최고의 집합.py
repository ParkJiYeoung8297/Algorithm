def solution(n, s):
    answer = [-1]
    
    if s%n==0:
        answer=[s//n for _ in range(n)]

    else:
        remain=s%n
        answer=[(s-remain)//n for _ in range(n)]
        for i in range(n-1,n-1-remain,-1):
            answer[i]=answer[i]+1

    return answer if sum(answer)==s and 0 not in answer else [-1]
