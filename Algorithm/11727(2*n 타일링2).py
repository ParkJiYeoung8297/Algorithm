n=int(input())

if n==1:
    print(1)
elif n==2:
    print(3)

else:
    f1=1
    f2=3

    for i in range(n-2):
        f3=2*f1+f2

        f1=f2
        f2=f3

    print(f3%10007)
