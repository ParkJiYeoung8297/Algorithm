def solution(triangle):
    answer = 0
    dp=[[0]*len(triangle[i]) for i in range(len(triangle))]
    dp[0][0]=triangle[0][0]
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j==0:
                dp[i][j]=max(dp[i-1][0]+triangle[i][j],triangle[i][j])
            elif j==i:
                dp[i][j]=max(dp[i-1][-1]+triangle[i][j],triangle[i][j])
            if j-1>=0 and j<i:
                dp[i][j]=max(dp[i-1][j-1]+triangle[i][j],dp[i-1][j]+triangle[i][j],triangle[i][j])

    
    return max(dp[-1])