import sys
# from itertools import product

N=int(input())
M=int(input())
A=[i for i in range(10)]

# 1) 위아래 버튼 누른 경우 
result=abs(N-100)


# 2) 숫자 버튼 + 위아래버튼 누른 경우
if M!=0:
    E=list(map(int,sys.stdin.readline().split()))
    for i in E:      # 고장난 버튼 제거
        A.remove(i)

for i in range(1000000):
    str_i=str(i)
    if all(int(d) in A for d in str_i):
        presses = abs(N - i) + len(str_i)  # 목표 채널과의 차이 + 숫자 버튼 횟수
        result = min(result, presses)
print(result)