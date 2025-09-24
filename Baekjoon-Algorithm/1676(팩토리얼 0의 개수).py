import sys

x=sys.stdin.readline()
x=int(x)

def factorial(a,b):
    if a==0 or a==1:
        return 1
    if a==b:
        return 1
    else:
        return a*factorial(a-1,b)

    
X=factorial(x//2,0)*factorial(x,x//2)  # 런타임 에러 때문에 분할 정복으로 변경

# 0의 개수 구하기
count=0
while (1):
    if X==0:
        break
    if X%10!=0:
        break
    else:
        count=count+1
        X=X//10

print(count)