# dfs로 구하기
def solution(begin, target, words):
    answer = float('inf')
    cand=[]
    visited=[0]*len(words)
    
    # 두 단어 비교하기
    def compare(a,b):
        A=list(a)
        B=list(b)
        count=0
        for i in range(len(A)):
            if A[i]==B[i]:
                count+=1
        if count==len(A)-1:
            return 1
        return 0
    
    
    # 타겟 단어 있는지 판단
    if target not in words:
        return 0
    
    def dfs(start,count):
        nonlocal answer
        stack=[]
        stack.append((start,count))
        visited[start]=1
        while stack:
            idx,curr_count=stack.pop()
            if words[idx]==target:
                answer=min(answer,curr_count)


            for w in range(len(words)):
                if visited[w]==0:
                    if compare(words[idx],words[w]):
                        visited[w]=1
                        stack.append((w,curr_count+1))
                                     
    for w in range(len(words)):
        if compare(begin,words[w]):
            dfs(w,1)
    return answer