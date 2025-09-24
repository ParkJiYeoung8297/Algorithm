import sys
from collections import deque

a=sys.stdin.readline().split()
dq=deque('')

for i in range(1,int(a[0])+1): #queue에 숫자 넣음
    dq.append(i)


print("<",end="")

while(len(dq)>1):
    for i in range(int(a[1])-1):
        dq.append(dq.popleft())
    print("{}, ".format(dq.popleft()),end="")

print("{}>".format(dq.popleft()),end="")