import sys
import string

N=int(input())
A=list(sys.stdin.readline().strip('\n'))
B={}
op=["+","-","*","/"]
stack=[]

# 알파벳과 숫자 매칭
for i in range(N):
    B[string.ascii_uppercase[i]]=input()

for i in range(len(A)):
    if A[i] not in op:  # 연산기호 아니면(=값이면) 값 append하기
        stack.append(B[A[i]])
    else:
        x2=str(stack.pop())
        x1=str(stack.pop())
        stack.append(eval(x1+A[i]+x2)) # 문자열 계산해주는 eval 사용

print(format(stack.pop(),'.2f')) # 소수점 두자리로 표기