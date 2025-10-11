# 선택은 +,- 둘 중 하나
# dfs 로 풀기
def solution(numbers, target):
    answer = 0
    def dfs(result,idx):
        nonlocal answer
        if idx==len(numbers) and result==target:
            answer+=1
        if idx>=len(numbers):
            return
            
        dfs(result+numbers[idx],idx+1)
        dfs(result-numbers[idx],idx+1)
    
    dfs(0,0)
    return answer