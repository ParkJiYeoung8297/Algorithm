def solution(sticker):
    answer = 0
    dp_first=[0]*len(sticker)
    dp_second=[0]*len(sticker)
    if len(sticker)==1:
        return sticker[0]
    

    # 첫번쨰 스티커를 떼는 경우
    dp_first[0]=sticker[0]
    dp_first[1]=max(sticker[1],dp_first[0])  # 이거 유의하기! dp[1]도 채워줘야함
    for i in range(2,len(sticker)-1):
        dp_first[i]=max(dp_first[i-2]+sticker[i], dp_first[i-1])
        
    
    # 첫번째 스티커를 안떼는 경우
    dp_second[1]=sticker[1]
    for i in range(2,len(dp_second)):
        dp_second[i]=max(dp_second[i-2]+sticker[i], dp_second[i-1])

    return max(max(dp_first),max(dp_second))