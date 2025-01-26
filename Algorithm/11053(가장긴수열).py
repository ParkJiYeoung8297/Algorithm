import sys

N = int(input())  # 입력 크기
A = list(map(int, sys.stdin.readline().split()))  # 배열 입력

dp = [1] * N  # DP 배열 초기화: 각 원소가 자신만 포함할 경우 길이 1

# DP 계산
for i in range(N):
    for j in range(i):  # 이전 요소 탐색
        if A[j] < A[i]:  # 증가하는 경우
            dp[i] = max(dp[i], dp[j] + 1)

# 최장 길이 출력
print(max(dp))
