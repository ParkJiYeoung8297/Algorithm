def solution(s):
    answer = 1
    
    # 투 포인터
    
    # 같은 포인터(i,i)가 중앙
    for i in range(len(s)):
        count=1
        start=i-1
        end=i+1

        while start>=0 and end<=len(s)-1:
            if s[start]==s[end]:
                count+=2
                answer=max(answer,count)
                start-=1
                end+=1
            else: 
                break
       
    # 두 개의 포인터(i,i+1)가 중앙
    for i in range(len(s)):
        count=0
        start=i
        end=i+1
        
        while start>=0 and end<=len(s)-1:
            if s[start]==s[end]:
                count+=2
                answer=max(answer,count)
                start-=1
                end+=1
            else: 
                break

        
    return answer