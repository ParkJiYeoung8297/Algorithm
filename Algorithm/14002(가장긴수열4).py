import sys

N=int(input())

A=list(map(int,sys.stdin.readline().split()))

dp=[1]*N
B=[]

for i in range(N):
    for j in range(i):
        if A[j]<A[i]:
            dp[i]=max(dp[i],dp[j]+1)


Max=max(dp)
for i in range(N-1,-1,-1):  
    if dp[i]==Max:  # 가장 긴 수열의 N번째 수는 dp[i]=N임
        B.append(A[i])
        Max=Max-1

print(max(dp))
B.reverse()
print(' '.join(map(str,B)))