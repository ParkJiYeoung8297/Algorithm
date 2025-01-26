import sys
from collections import deque

t=sys.stdin.readline()

def Euclidean(a,b):  # 유클리드 호제법
    if a==b:
        return a
    else:
        if a<b:
            a,b=b,a   # 큰 수를 a에 배치
        d1=a   #dividened
        d2=b     #divisor
        r=1
        while (1):
            if r==0: #remainder
                break
            r=d1%d2
            d1=d2
            d2=r

        return d1

        

for i in range(int(t)):
    result=0
    A=sys.stdin.readline().split()
    A=deque(A)
    n=A.popleft()
    n=int(n)
    for k in range(n-1):
        for j in range(1,n-k):
            result=result+Euclidean(int(A[k]),int(A[k+j]))
    print(result)