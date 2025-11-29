# 점이 아닌 막대기 기준 가능한지 판단
def possible(pillars,beams,n):
    for x,y in pillars:
        if y==0:
            continue
        if (x,y-1) in pillars:
            continue
        if (x-1,y) in beams:
            continue
        if (x,y) in beams:
            continue
        return False
    
    for x,y in beams:
        if (x,y-1) in pillars:
            continue
        if (x+1,y-1) in pillars:
            continue
        if (x-1,y) in beams and (x+1,y) in beams:
            continue
        return False
    return True
    
# 설치/삭제하고 나서 가능한지 판단, 불가능하다면 빠꾸
def solution(n, build_frame):
    pillars=set()
    beams=set()
    answer = []
    
    for x,y,a,b in build_frame:
        if a==0:
            if b==1:
                pillars.add((x,y))
                if not possible(pillars,beams,n):
                    pillars.remove((x,y))
            else:
                pillars.remove((x,y))
                if not possible(pillars,beams,n):
                    pillars.add((x,y))
        else:
            if b==1:
                beams.add((x,y))
                if not possible(pillars,beams,n):
                    beams.remove((x,y))
            else:
                beams.remove((x,y))
                if not possible(pillars,beams,n):
                    beams.add((x,y))
    for x,y in pillars:
        answer.append([x,y,0])
    for x,y in beams:
        answer.append([x,y,1])
    answer.sort()        
    return answer