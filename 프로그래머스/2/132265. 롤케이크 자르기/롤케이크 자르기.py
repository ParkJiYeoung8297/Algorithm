from collections import Counter
def solution(topping):
    answer = 0
    count=Counter(topping)
    me=len(count.keys())
    brother=set()
    
    for idx in range(len(topping)-1):
        t=topping[idx]
        brother.add(t)
        
        count[t]-=1
        if count[t]==0:
            del count[t]
        if len(brother)==len(count.keys()):
            answer+=1
    return answer