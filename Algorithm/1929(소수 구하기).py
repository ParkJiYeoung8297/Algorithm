import sys
from collections import deque
import math

n=sys.stdin.readline().split()
X=deque()

for i in range(int(n[0]),int(n[1])+1):
    if i==1:      # 초기 조건 1
        continue
    elif i==2:    # 초기 조건 2
        X.append(i)
        continue
    elif i==3:    # 초기 조건 3
        X.append(i)
        continue

    for j in range(2,int(math.sqrt(i))+1): # i>=4일때만 사용 가능, 2부턴 i의 제곱근 수 까지만 나눠봐도 소수를 알 수 있음
        if i%j==0:
            i=0
            break
    if i!=0:
        X.append(i)

for i in X:
    print(i)