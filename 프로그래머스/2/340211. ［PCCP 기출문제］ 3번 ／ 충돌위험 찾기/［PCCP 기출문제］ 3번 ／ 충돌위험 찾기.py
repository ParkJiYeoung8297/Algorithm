# 직선 또는 한번 꺾어서 이동할 수 밖에 없음 (r좌표 먼저 움직임)
# t 초에 같은 좌표위에 로봇이 있으면 충돌 위험 count (좌표 기준으로 count)
from collections import Counter
def solution(points, routes):
    answer = 0
    dict_r={} #로봇의 현재 좌표
    dest_r={}
    
    for i in range(len(routes)):
        rout=routes[i]
        dict_r[i]=points[rout[0]-1]
        dest_r[i]=[]
        for j in range(1,len(rout)):
            dest_r[i].append(points[rout[j]-1])
    

    def move(robot,r,c): # 로봇 번호와 목적지 좌표
        cur_r,cur_c=dict_r[robot]
        # r이 같은지 먼저 파악
        if cur_r>r:
            cur_r-=1
        elif cur_r<r:
            cur_r+=1
        else:
            if cur_c<c:
                cur_c+=1
            elif cur_c>c:
                cur_c-=1
            else:
                del dest_r[robot][0]
                if len(dest_r[robot])==0:
                    del dict_r[robot]
                return 1 # 도착함
        dict_r[robot]=[cur_r,cur_c]
        return 0
            
    def check_bomb(dict_r):
        count=Counter([tuple(i) for i in dict_r.values()])
        return len([i for i in count.values() if i>=2])
    
    arrive=0
    while (dict_r):
        answer+=check_bomb(dict_r)
        for r in range(len(routes)):
            if r in dict_r.keys():
                flag=move(r,dest_r[r][0][0],dest_r[r][0][1])
                arrive+=flag
                if flag==1 and len(dest_r[r])>0:
                    move(r,dest_r[r][0][0],dest_r[r][0][1])
                    arrive+=flag
            
    return answer