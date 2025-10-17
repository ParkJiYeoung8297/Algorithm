def solution(triangle):
    answer = 0
    dp=[[0]*len(triangle) for _ in range(len(triangle))]
    dp[0][0]=triangle[0][0]
    for i in range(1,len(triangle)):
        dp[i][0]=dp[i-1][0]+triangle[i][0]
        dp[i][i]=dp[i-1][i-1]+triangle[i][i]
        for idx in range(1,i):
            dp[i][idx]=max(dp[i-1][idx-1]+triangle[i][idx],dp[i-1][idx]+triangle[i][idx])
    return max(dp[len(triangle)-1])