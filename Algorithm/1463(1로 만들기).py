X=int(input())

dp=[0]*(X+1)

for i in range(2,X+1): # 
    dp[i]=dp[i-1]+1   #1번 조건(1 뺴기) 모든 수는 1로 뺄 수 있으니 dp 값 채우기

    if i%3==0:   # 2번 조건(3으로 나누어 떨어짐) 만족할 때, 더 작은 값으로 갱신
        dp[i]=min(dp[i],dp[i//3]+1)

    if i%2==0:   # 3번 조건(2로 나누어질때) 만족할 때, 더 작은 값으로 갱신
        dp[i]=min(dp[i],dp[i//2]+1)

print(dp[X])
