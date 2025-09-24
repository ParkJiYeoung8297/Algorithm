import sys
import math

x=sys.stdin.readline()  # 초기값 입력 받기 

def is_prime(i): # 조건 : i는 3이상의 홀수
    if i==3:
        return 1
    else:
        for j in range(2,int(math.sqrt(i))+1): # i>=5 일떄 실행
            if i%j==0:
                return 0
        return 1

while (1):
    X=int(x)
    if X==0:
        break

    # 홀수의 합으로 나타내기
    for i in range(3,int(X/2)+1,2): #b-a가 가장 큰 경우부터 소수인지 판단해서 불필요한 계산 줄이기
        print(i)
        a=i
        b=X-i
        
        # 소수 판별 함수
        if is_prime(a) and is_prime(b):
            result=(a,b)
            break

    if result: # 값이 있으면 출력
        print('{} = {} + {}'.format(X,result[0],result[1]))
    else: # 두 홀수로 나타낼 수 없으면 에러문 출력
        print("Goldbach's conjecture is wrong.")

    x=sys.stdin.readline()