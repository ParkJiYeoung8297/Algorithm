# 우와...해답 보니까 5진법으로 풀면 되는 간단한 문제라네..
# 5진법도 5자리씩이고, 이것도 5자리씩 규칙이 있으니까 5진법 사용하면 편함
# 0 → 00000 , 1 → 11011

def solution(n, l, r):
    answer = 0
    for i in range(l-1,r):
        while i>0:
            mod=i%5
            i=i//5
            if mod==2: # 가운데 영역에 해당 (즉, 0이라는 소리)
                break
        else: # while..else 문 (while이 break 안되면 실행됨)
            answer+=1        
        
    return answer