N=int(input())

if N==1:
     print(1)
elif N==2:
     print(1)
else:
     f1=1
     f2=1
     for i in range(N-2):
        f3=f1+f2
        f1=f2
        f2=f3

     print(f3)