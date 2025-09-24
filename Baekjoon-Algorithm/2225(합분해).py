import sys

N,k=sys.stdin.readline().split()

result=0
#for i in range(N):






# N%k==0 값*2+1 , 값*2
if N%k==0:
    result=result*2+1
else:
    result=result*2

print(result)