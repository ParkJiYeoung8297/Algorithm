# 그 수의 가장 큰 약수가 정답 (본인 제외)
def solution(begin, end):
    answer = [1]*(end-begin+1)
    idx=0
    for value in range(begin,end+1):
        if value==1:
            answer[idx]=0
        else:
            # 여기서 오류가 많이 남 (블록이 10000000까지만 가능하다는 조건)
            max_v=1
            for i in range(2,int(value**0.5)+1):
                if value%i==0:
                    if value//i<=10000000:
                        max_v=value//i
                        break
                    else:
                        max_v=i
            answer[idx]=max_v
        idx+=1
    return answer