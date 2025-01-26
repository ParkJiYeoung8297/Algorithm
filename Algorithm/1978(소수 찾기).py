import sys

n=int(input())
N=0
a=sys.stdin.readline().split()

for i in range(n):
    x=int(a[i])
    if x==1:   # 초기 조건 1 : 1은 소수아님
        continue
    elif x==2:  #초기 조건 2 : 2는 소수
        N=N+1
        continue

    for j in range(1,x-1): # for 문은 x>=3일떄 사용 가능
        if x%(x-j)==0:  #2붗터 x-1까지 나눠지는 숫자가 있으면 카운트 제외
            x=0
    if x!=0:
        N=N+1

print(N)