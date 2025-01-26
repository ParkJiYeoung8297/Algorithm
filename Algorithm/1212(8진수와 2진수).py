import sys

a=sys.stdin.readline().strip('\n')
if a=='0':
    print('0')
else:
    A=list(a)

    for i in range(len(A)):
        if A[i]=='4':
            A[i]='100'
        elif A[i]=='2':
            A[i]='010'
        elif A[i]=='1':
            A[i]='001'
        elif A[i]=='7':
            A[i]='111'
        elif A[i]=='6':
            A[i]=='110'
        elif A[i]=='5':
            A[i]='101'
        elif A[i]=='3':
            A[i]='011'
        elif A[i]=='0':
            A[i]='000'

    # 문자열로 출력하며, 앞의 0 제거
    print(''.join(A).lstrip('0'))