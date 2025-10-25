
def solution(sticker):
    answer = 0

    if len(sticker)<=3:
        return max(sticker)
    
    # 스티커 뗼건지, 말건지 선택(dfs 말고 dp로 선택하기)
    dp=[0]*(len(sticker)-1)
    
    #0을 똈을 때
    dp=[0]*(len(sticker)-1)
    dp[0]=sticker[0]
    dp[1]=max(sticker[1],dp[0])  # 이거 유의하기! dp[1]도 채워줘야함
    for i in range(2,len(sticker)-1):
        dp[i]=max(dp[i-1],dp[i-2]+sticker[i]) # 안떼기, 떼기
    answer=dp[-1]
    # 0 안뗐을 때
    dp=[0]*len(sticker)
    dp[1]=sticker[1]
    for i in range(2,len(sticker)):
        dp[i]=max(dp[i-1],dp[i-2]+sticker[i]) # 안떼기, 떼기
    answer=max(answer,dp[-1])
    return answer

    