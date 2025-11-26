# 배열 탐색으로는 시간초과나서 문제가 해결될 수 없음
# linked-list를 사용해야함 (중요)
def solution(n, k, cmd):
    answer = ''
    prev=[i-1 for i in range(n)]
    next=[i+1 for i in range(n)]
    next[-1]=-1 # 마지막
    cur=k
    removed=[]
    
    for c in cmd:
        C=c.split(" ")
        
        if C[0]=="U":
            for i in range(int(C[1])):
                if prev[cur]!=-1:
                    cur=prev[cur]
                else:
                    break
            
        elif C[0]=="D":
            for i in range(int(C[1])):
                if next[cur]!=-1:
                    cur=next[cur]
                else:
                    break
            
        elif C[0]=="C":
            removed.append((cur,prev[cur],next[cur]))
            
            # 연결 끊기
            if prev[cur]!=-1: # 맨앞이 아니라면
                next[prev[cur]]=next[cur]
            if next[cur]!=-1: # 맨뒤가 아니라면
                prev[next[cur]]=prev[cur]
            
            if next[cur]!=-1:
                cur=next[cur]
            else:
                cur=prev[cur]
            
            
        elif C[0]=="Z" and removed:
            r,p,ne=removed.pop()
            if p!=-1: # 맨앞이 아니라면
                next[p]=r
            if ne!=-1: # 맨 뒤가 아니라면
                prev[ne]=r
            

                
    answer=["O"]*n
    for R in removed:
        answer[R[0]]="X"
    return "".join(answer)