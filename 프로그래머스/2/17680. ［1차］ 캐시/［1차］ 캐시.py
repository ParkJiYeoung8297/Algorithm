from collections import deque
def solution(cacheSize, cities):
    answer = 0
    stack=deque()
    cache={}
    
    for city in cities:
        city=city.lower()
        if city in cache:
            answer+=1
            stack.remove(city)
            stack.append(city)
        else:
            cache[city]=1
            stack.append(city)
            answer+=5
            if len(stack)>cacheSize:
                del cache[stack.popleft()]
    
    
    
    return answer