# 1, 4, 7, 8 →  어디서 시작해도 사이클임
# 앞부터 그룹화로 묶어서 쪼개기
def solution(cards):
    result = []
    visited={}

    for i in range(len(cards)):
        groups=[]
        # 방문했는지 체크
        if cards[i] in visited:
            continue
        
        # while돌아서 사이클 완성하기
        while (1):
            groups.append(cards[i])
            visited[cards[i]]=1
            i=cards[i]-1
            if cards[i] in visited:
                break
        result.append(len(groups))  
    
    # 정답 계산
    if len(result)==1:
        return 0
    
    result.sort(reverse=True)
    
    return result[0]*result[1]