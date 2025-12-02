# 110을 찾아서 모두 제거
# 마지막 111 앞에 두기 (111외에 남은 거는 모두 우선순위가 110보다 위임)
def solution(s):
    answer = []
    for st in s:
        stack=[]
        count110=0
        
        for char in st:
            stack.append(char)
            if len(stack)>=3 and stack[-3:]==["1","1","0"]:
                stack.pop()
                stack.pop()
                stack.pop()
                count110+=1
                
        rest="".join(stack)
        idx=rest.find("11")
        if idx==-1:
            idx=rest.rfind("0")+1
            if idx==-1:
                idx=len(rest)
        answer.append(rest[:idx] + "110"*count110 + rest[idx:])        
    
    return answer