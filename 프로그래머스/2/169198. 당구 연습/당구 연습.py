# 이해가 어려웠던 문제. 그냥 수선 그려서 피타고라스 쓰면 되지 않나 했는데 그게 아님
# 반사를 이용해서 점을 이동시킨 후, 그게 직선이 될 때가 가장 짧은 길이임
# 목표 좌표를 네 border 기준으로 대칭 이동 시킴
def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        targetX, targetY=ball
        dist=[]
        
        candidates=(targetX, -targetY), (targetX, 2*n-targetY), (2*m-targetX, targetY), (-targetX, targetY)
        
        for cand in candidates:
            dist.append((startX-cand[0])**2+(startY-cand[1])**2)
            
        # 직선상에 있는 경우 공을 먼저 치는 경우 제외
        if targetX==startX:
            if targetY>=startY: # 위로 가는 경우 제외
                dist[1]=float('inf')   
            else: # 아래로 가는 경우 제외
                dist[0]=float('inf')     
        elif targetY==startY: # 
            if targetX>=startX:  # 오른쪽으로 가는 경우 제외
                dist[2]=float('inf')   
            else: # 왼쪽으로 가는 경우 제외
                dist[3]=float('inf')   

        
        answer.append(min(dist))
        
        
    return answer