import sys

N=int(input())
A=list(map(int,sys.stdin.readline().split()))
result=[-1]*N
stack=[]   # 인덱스


for i in range(N):
    while stack and A[stack[-1]]<A[i]:  # 1) stack에 값이 있음 2) A[i]가 A[stack[-1]]보다 큼(오큰수)
        result[stack.pop()]=A[i]

    stack.append(i)


print(" ".join(map(str,result)))