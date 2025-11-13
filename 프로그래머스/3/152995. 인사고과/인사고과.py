def solution(scores):
    wonho=scores[0].copy()
    
    # 원호가 탈락 조건인지 체크
    for i in range(1,len(scores)):
        if wonho[0]<scores[i][0] and wonho[1]<scores[i][1]:
            return -1
    filterd_s=[wonho]
        
    # 앞의 요소로 미리 정렬하면, 뒤에 요소만 비교해주면 됨
    scores.sort(key=lambda x: (-x[0],x[1]))
    max_v=-1
    for i in range(len(scores)):
        if scores[i][1]<max_v:
            continue
        max_v=scores[i][1]
        filterd_s.append(scores[i])
        
    filterd_s.sort(key=lambda x:sum(x), reverse=True)

    
    # 원호보다 큰 사람이 몇명인지 세면 됨
    rank=1
    score=sum(filterd_s[0])

    for i in range(len(filterd_s)):
        # 순위 갱신
        if sum(filterd_s[i])!=score:
            rank=i+1
            score=sum(filterd_s[i])
            
        if filterd_s[i]==wonho:
            return rank 
    return -1