import sys

E,S,M=list(map(int,sys.stdin.readline().split()))

k=0
while (1):
    N=k*28+S
    if N%15==(E%15) and N%19==(M%19):  # 15 나누어 떨어지는 경우 0이 아니라 15로 표기하므로 (E%15)로 함
        print(N)
        break
    else:
        k=k+1
