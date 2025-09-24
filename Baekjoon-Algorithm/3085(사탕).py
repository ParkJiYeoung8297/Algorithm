import sys

N=int(input())
A=[]
for i in range(N):
    A.append(list(sys.stdin.readline().strip('\n')))

# N*N에서 가장 많이 먹을 수 있는 사탕 개수 구하기
def count_candy(A,N):
    result=1

    # 행
    for i in range(N):
        count = 1
        for j in range(1, N):
            if A[i][j] == A[i][j - 1]:  # 이전 값과 같으면 count+1
                count += 1
            else:
                result = max(result, count)  # 새로운 색이 나오면 최대값 갱신
                count = 1  # 연속이 끊겼으므로 count 초기화
        result = max(result, count)  

    # 열
    for j in range(N):
        count = 1
        for i in range(1, N):
            if A[i][j] == A[i - 1][j]:  # 이전 값과 같으면 count+1
                count += 1
            else:
                result = max(result, count)  # 새로운 색이 나오면 최대값 갱신
                count = 1  # 연속이 끊겼으므로 count 초기화
        result = max(result, count)

    return result


# 직접 옆으로 교체 , 밑으로 교체 경우의 수 모두 구하기 (완전 탐색)
counts=0
result=0
for i in range(N):
    for j in range(N-1):
        B = [row[:] for row in A]
        B[i][j],B[i][j+1]=B[i][j+1],B[i][j] # 옆으로 교체
        counts=count_candy(B,N)   # 개수 세기
        if result<counts:
            result=counts

for i in range(N-1):
    for j in range(N):
        B = [row[:] for row in A]
        B[i][j],B[i+1][j]=B[i+1][j],B[i][j] # 밑으로 교체
        counts=count_candy(B,N)   # 개수 세기
        if result<counts:
            result=counts

print(result)