import sys


x=sys.stdin.readline()
x=int(x)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)   # 재귀적 함수
    
print(factorial(x))