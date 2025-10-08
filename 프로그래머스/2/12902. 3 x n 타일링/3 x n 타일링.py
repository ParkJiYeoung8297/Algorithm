def solution(n):
    answer = 0
    dp=[0]*(n+1)
    dp[2]=3
    dp[4]=11
    if n%2==1:
        return 0
    else: 
        if n>=6:
            for i in range(6,n+1,2):
                dp[i]=dp[i-2]*4-dp[i-4] # 이게 점화식 (잘 이해 못함..)
    
        return dp[n]%1000000007