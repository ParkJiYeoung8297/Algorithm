import sys

N=int(input())

A=list(map(int,sys.stdin.readline().split()))

dp=[A[0]]*N

for i in range(1,N):
    dp[i]=max(A[i],dp[i-1]+A[i])  # A[i]와 연속합 비교하여 더 큰 값으로 갱신
print(max(dp))
