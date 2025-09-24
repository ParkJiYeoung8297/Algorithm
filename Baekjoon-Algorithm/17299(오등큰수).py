import sys
from collections import Counter

N=int(input())
A=list(map(int,sys.stdin.readline().split()))
result=[-1]*N # 결과
stack=[] #인덱스

# 개수 구하기
F = Counter(A)  # A의 각 원소의 빈도 계산

# 개수 비교
for i in range(N):
    while stack and F[A[stack[-1]]]<F[A[i]]:
        result[stack.pop()]=A[i]

    stack.append(i)

print(" ".join(map(str,result)))