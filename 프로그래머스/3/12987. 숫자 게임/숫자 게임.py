from collections import deque
def solution(A, B):
    result=0
    A.sort(reverse=True)
    B.sort(reverse=True)
    A=deque(A)
    B=deque(B)
    
    for i in range(len(A)):
        # A가 크면 젤 작은거 내보내기 (어처피 못이기니까 피해 최소화)
        if A[0]>B[0]:
            B.pop()
            A.popleft()
        elif A[0]==B[0]:
            A.popleft()
            B.pop()
        else:
            A.popleft()
            B.popleft()
            result+=1
            
    return result