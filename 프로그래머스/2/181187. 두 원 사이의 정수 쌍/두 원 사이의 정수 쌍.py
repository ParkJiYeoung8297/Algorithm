# 1 사분면만 구하면, 나머지는 대칭이니까 정답을 구할 수 있음
# 원 공식 : x^2+y^2=r^2 → y=(r^2-x^2)**0.5
import math
def circleInnerPoint(r):
    result=0
    for x in range(1,r):
        result+=int(((r**2)-(x**2))**0.5)
    return (result+r)*4+1

def circleboundPoint(r):
    result=0
    for x in range(1,r):
        if int(((r**2)-(x**2))**0.5)==math.ceil(((r**2)-(x**2))**0.5):
            result+=1
        
    return (result*4)+4
        
        

def solution(r1, r2):
    return circleInnerPoint(r2)-circleInnerPoint(r1)+circleboundPoint(r1)