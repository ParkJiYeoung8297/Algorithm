n=int(input())

dp=[1,2,0] # 메모리 사용 줄이는 bottom up 방식


if n==1:
    print(1)
elif n==2:
    print(2)
else:
    for i in range(n-2):
        dp[2]=dp[0]+dp[1]
        dp[0]=dp[1]
        dp[1]=dp[2]

    print(dp[2]%10007)