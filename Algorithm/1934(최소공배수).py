import sys

n=int(input())
for i in range(n):

    a=sys.stdin.readline().split()
    A=int(a[0])
    B=int(a[1])
    target=0

    if (A<B):
        for i in range(1,A+1):
            if (A%i==0 and B%i==0):
                target=i
        print(target*int(A/target)*int(B/target)) #최소공배수
        

    else:
        for i in range(1,B+1):
            if (A%i==0 and B%i==0):
                target=i
        print(target*int(A/target)*int(B/target)) #최소공배수

