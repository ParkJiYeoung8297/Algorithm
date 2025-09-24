N=int(input())

dp=[0]*(N+1)
for i in range(1,N+1):
    if int(i**0.5)==i**0.5: # 제곱수일 경우 1
        dp[i]=1
    else:
        for j in range(int(i**0.5)+1):
            dp[i]=min(dp[i-j*j]+1,dp[i]) # dp[i-j*j]에다가 제곱수 하나 더한거니까 +1


print(dp[N])