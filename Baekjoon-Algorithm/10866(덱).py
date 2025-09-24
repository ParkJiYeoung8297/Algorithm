import sys
from collections import deque


n=int(sys.stdin.readline())
dq=deque('')

for i in range(n):
    run=sys.stdin.readline().split()
    if run[0]=="push_front":
        dq.appendleft(int(run[1]))
    elif run[0]=="push_back":
        dq.append(int(run[1]))
    elif run[0]=="pop_front":
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())
    elif run[0]=="pop_back":
        if len(dq)==0:
            print(-1)
        else:
            print(dq.pop())
    elif run[0]=="size":
        print(len(dq))
    elif run[0]=="empty":
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif run[0]=="front":
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    elif run[0]=="back":
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])