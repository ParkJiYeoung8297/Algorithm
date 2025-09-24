import sys

T=int(input())


def binary_search(i,B):
    low, high=0,len(B)-1
    result=0
    while low<=high:
        mid=(low+high)//2
        if B[mid]<i:
            result=mid+1
            low=mid+1
        else:
            high=mid-1
    return result

for i in range(T):
    result=0
    N,M=map(int,sys.stdin.readline().split())
    A=list(map(int,sys.stdin.readline().split()))
    B=list(map(int,sys.stdin.readline().split()))

    B.sort()    # B는 정렬

    for i in A:
        result = result+ binary_search(i, B)

    print(result)
