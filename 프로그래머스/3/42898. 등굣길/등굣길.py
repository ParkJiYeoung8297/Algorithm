def solution(m, n, puddles):
    answer = 0
    # 오른쪽 또는 아래로만 움직임
    dp=[[0]*(m+1) for _ in range(n+1)]
    
    dp[1][1]=1
    
    # 물 웅덩이 표시
    for x,y in puddles:
        dp[y][x]=-1

    for y in range(1,n+1):
        for x in range(1,m+1):
            if dp[y][x]!=-1:
                if dp[y][x-1]!=-1:
                    dp[y][x]+=dp[y][x-1]
                if dp[y-1][x]!=-1:
                    dp[y][x]+=dp[y-1][x]

    return dp[n][m]%1000000007