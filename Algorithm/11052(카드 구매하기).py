import sys

# 입력
N=int(input())
P=sys.stdin.readline()
P='0 '+P
P=P.split()
P=list(map(int,P))
A=[0]*(N+1)
A[1]=P[1]

#A[i]의 최댓값을 구하는 것은 max(A[i],A[i-1]+P[1],A[i-2]+P[2],...A[0]+P[i])임
for i in range(2,N+1): # A[2]~A[N]을 채우는 루프

    for j in range(1,i+1): # 하나의 A[i]의 최댓값 구하는 과정
        f1=A[i]
        f2=P[j]+A[i-j]
        A[i]=max(f1,f2)

print(A[N])