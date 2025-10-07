# dfs로 구하기 , 경우의 수는 A가 훔치거나, B가 훔치거나 2가지
# 고려사항 ! 중복 방문 체크 ! ← 이거 안하면 시간초과
def solution(info, n, m):
    answer =-1
    stack=[]
    stack.append([0,0,0]) # index, A 누적, B 누적
    visited={}
    while stack:
        idx,A_score,B_score=stack.pop()
        visited[(idx,A_score,B_score)]=1
        if A_score>=n or B_score>=m:
            continue
        if idx>=len(info):
            
            if answer==-1:
                answer=A_score
            else:
                answer=min(answer,A_score)
            continue
            
        if (idx+1,int(info[idx][0])+A_score,B_score) not in visited:
            stack.append([idx+1,int(info[idx][0])+A_score,B_score])
        if (idx+1,A_score,int(info[idx][1])+B_score):
            stack.append([idx+1,A_score,int(info[idx][1])+B_score])
            
    return answer