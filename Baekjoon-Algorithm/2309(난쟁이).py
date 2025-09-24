# import sys

# A=[]
# for _ in range(9):
#     A.append(int(sys.stdin.readline()))

# A.sort()

# value=sum(A)-100  # 가짜 난쟁이 둘을 더하면 value 값이 된다.

# for i in range(len(A)):
#     if len(A)==7: #답 찾으면 len(A)=7임
#         break
#     for j in range(i,len(A)):
#         if value==A[i]+A[j]:
#             a=A[j]         #A[i] remove하고 나면 A[j] 값이 달라지니까 미리 저장해두기
#             A.remove(A[i])
#             A.remove(a)    
#             break
            



# for i in range(7):
#     print(A[i])

# 파이썬 조합 라이브러리 사용 답안
import sys
from itertools import combinations

A=[]
for _ in range(9):
    A.append(int(sys.stdin.readline()))

combination_list=list(combinations(A,7))

for i in range(len(combination_list)):
    if sum(combination_list[i])==100:
        A=list(combination_list[i])
        break

A.sort()
for i in range(7):
    print(A[i])