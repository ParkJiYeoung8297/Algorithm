# 그리디 + 백트래킹 DFS로 풀어야한다. + 사전 순으로 우선 탐색
def solution(n, m, x, y, r, c, k):
    answer = ''
    dir=[('d',0,1),('l',-1,0),('r',1,0),('u',0,-1)] # 사전 순으로 정렬 , d, l, r, u
    
    cx,cy=y-1,x-1 # 출발
    ex,ey=c-1,r-1
    for i in range(k):
        moved=True
        for ch,dx,dy in dir:
            nx=cx+dx
            ny=cy+dy
            if not (0<=nx<m and 0<=ny<n):
                continue

            dist=abs(ex-nx)+abs(ey-ny)
            remain=k-i-1
            
            
            # 도착지에 도달 가능한지 파악 (바로 도착)
            if dist>remain:
                continue
            # 도착지에 도달 가능한지 파악 (돌아서 도착)
            if (remain-dist)%2==1:
                continue
            moved=False
            answer+=ch
            cx,cy=nx,ny
        if moved:
            return "impossible"
    if cx!=ex or cy!= ey:
        return "impossible"

    return answer