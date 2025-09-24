import sys
from collections import deque

n=sys.stdin.readline().strip('\n')

# 2진수를 3자리로 맞추기
while len(n) % 3 != 0:
    n = '0' + n

A=list(n) # 2진수 값

sum=0

for i in range(len(A)):
    if i%3==0:
        sum=sum+4*int(A[i])
        
    elif i%3==1:
        sum=sum+2*int(A[i])

    else:
        sum=sum+int(A[i])

        print(sum,end='') #세자리씩 끊기
        sum=0