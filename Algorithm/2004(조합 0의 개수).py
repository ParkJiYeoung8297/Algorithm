import sys

def count_factorial_factors(n, p):
    """n!에서 소인수 p의 개수를 계산"""
    count = 0
    power = p
    while n >= power:
        count += n // power
        power *= p
    return count

# 입력 처리
x = sys.stdin.readline().split()
a = int(x[0])
b = int(x[1])

# 조합식에서 5와 2의 개수 계산
factor_5 = count_factorial_factors(a, 5) - count_factorial_factors(a - b, 5) - count_factorial_factors(b, 5)
factor_2 = count_factorial_factors(a, 2) - count_factorial_factors(a - b, 2) - count_factorial_factors(b, 2)

# 끝자리 0의 개수는 5와 2의 최소값
print(min(factor_5, factor_2))
