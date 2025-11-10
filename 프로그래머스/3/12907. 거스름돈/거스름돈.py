def solution(n, money):
    dp=[0]*(n+1)
    # dp 사용하기
    for i in money:
        dp[i]+=1
        for idx in range(1,n+1):
            if idx-i>=0:
                dp[idx]+=dp[idx-i]
        
    return dp[n]%1000000007