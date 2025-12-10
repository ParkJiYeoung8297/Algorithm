# dp[i]는 N을 i번 사용해서 만들 수 있는 숫자 조합들이다. 
# (최솟값이 8보다 크면 -1 return하라는 것에서 눈치챘어야..😅)
# dp에는 값 뿐만 아니라 리스트로 조합들까지 저장해둘 수 있다는 점 기억하기
# dp[i]는 (dp[i-1],dp[1]), (dp[i-2],dp[2]) ... (dp[1],dp[i-1]) 까지 조합들

def solution(N, number):
    dp=[set() for _ in range(9)]
    dp[0].add(0)
    
    for i in range(1,9):
        # 문자 이어붙힌 값
        if number==str(N)*i:
            return i
        dp[i].add(int(str(N)*i))
        
        # 사칙 연산
        for j in range(1,i):
            for k in dp[j]:
                for t in dp[i-j]:
                    dp[i].add(k+t)
                    dp[i].add(k-t)
                    dp[i].add(k*t)
                    if t!=0:
                        dp[i].add(k//t)
            
        # 타깃값 있는지 확인
        if number in dp[i]:
            return i

    return -1