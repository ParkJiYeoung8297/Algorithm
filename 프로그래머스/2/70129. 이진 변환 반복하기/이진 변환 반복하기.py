def solution(s):
    answer = [0,0]
    
    while(s!="1"):
        answer[0]+=1
        S=list(s)
        count=0
        
        for i in range(len(S)):
            if S[i]=="0":
                answer[1]+=1
            else:
                count+=1
        # 변환 후 길이는 1의 개수와 같다 = count
        s=bin(count)[2:]
    return answer