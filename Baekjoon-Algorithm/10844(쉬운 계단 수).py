N=int(input())

if N==1:
    print(9)
else:
    A=[1]*10 #0~9까지 나올 수 있는 개수를 A에 갱신
    A[0]=0
    B=[0]*10
    for i in range(N-1):     # 자리수 만큼 반복
        for j in range(10):  # 0~9까지 각 자리에 나오는 개수 갱신
            if j==0:
                B[0]=A[1]
            elif j==9:

                B[9]=A[8]

            else:
                B[j]=A[j-1]+A[j+1]

        A=B.copy()

    print(sum(B)%1000000000)