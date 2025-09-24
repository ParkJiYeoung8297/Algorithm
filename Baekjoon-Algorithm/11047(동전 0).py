import sys

N,K=map(int,sys.stdin.readline().split())

def choose_coin(k,coins,result): # 가격, 코인 목록, 코인 개수
    if k<coins[-1]:         # 값<코인
        coins.pop()
        result=choose_coin(k,coins,result)
        return result
    elif k==coins[-1]:       # 값=코인
        result=result+1
        return result
    else:                    # 값>코인
        if k%coins[-1]==0:   
            result=result+(k//coins[-1])
            return result
        else:
            result=result+(k//coins[-1])
            k=k%coins[-1]
            coins.pop()
            result=choose_coin(k,coins,result)  # 남은 금액으로 재귀
            return result


result=0
coins=[]
for i in range(N):
    coins.append(int(input()))
 
print(choose_coin(K,coins,result))