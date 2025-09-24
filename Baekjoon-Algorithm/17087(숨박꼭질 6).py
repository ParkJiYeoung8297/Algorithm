import sys

def Euclidean(a,b):
    if b>a:
        a,b=b,a

    r=1 # remainder
    d1=a  # dividened
    d2=b  # divider

    while (1):
        if r==0:
            break
        r=d1%d2
        d1=d2
        d2=r
    return d1

A=sys.stdin.readline().split()

N=int(A[0]) # 동생 수
S=int(A[1]) # 수빈이 위치

B=sys.stdin.readline().split()

# D는 수빈과 동생 위치차이의 최대 공약수

for i in range(N):
    if S<int(B[i]):
        B[i]=int(B[i])-S
    elif S>int(B[i]):
        B[i]=S-int(B[i])
    else:
        B[i]=1

if N==1:
    D=B[0]
elif N==2:
    D=Euclidean(B[0],B[1])
else:
    D=Euclidean(B[0],B[1])
    for i in range(2,N):
        D=Euclidean(D,B[i])

print(D)