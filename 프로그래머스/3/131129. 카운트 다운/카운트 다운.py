# dp를 이용해서 문제 풀기
# dp[i]는 dp[i-score]에서 싱글, 더블, 트리플, 볼을 던졌을 때 최소의 (던진 횟수, 싱글/볼 횟수) 조건을 만족하는 값이다.
# 점수는 1~60까지 한정적이기 때문에 이를 탐색함, (점수,싱글/볼 여부)를 score에 저장
def solution(target):
    INF=float('inf')
    answer = []
    scores=[]
    dp=[(INF,-INF) for _ in range(target+1)] # 던진 횟수, 싱글/볼 횟수 (목표 : 최소 던진 횟수, 최대 싱글/볼 횟수)
    dp[0]=[0,0]
    
    # 싱글
    for i in range(1,21):
        scores.append((i,1))
    
    # 더블
    for i in range(1,21):
        scores.append((i*2,0))
    
    # 트리플
    for i in range(1,21):
        scores.append((i*3,0))
    
    # 볼
    scores.append((50,1))

    for i in range(1,target+1):
        min_throw=dp[i][0]
        max_sb=dp[i][1]
        
        for score, sb in scores:
            if i-score<0:
                continue
            curr_throw=dp[i-score][0]+1
            curr_sb=dp[i-score][1]+sb
            
            # 조건 1: 던지는 횟수가 작다.
            # 조건 2: 던지는 횟수가 같다면, 싱글/볼 여부가 더 많다.
            if curr_throw<min_throw or (curr_throw==min_throw and curr_sb>max_sb):    
                min_throw=curr_throw
                max_sb=curr_sb
        dp[i]=(min_throw,max_sb)
 
    return dp[target]