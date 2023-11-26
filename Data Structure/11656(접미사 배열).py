import sys
from collections import deque
import string

alpha=string.ascii_lowercase
index_A=[]
A=list(sys.stdin.readline().strip('\n')) 

for i in A:
    index_A.append(alpha.index(i))   #알파벳이 몇번째 있는 문자인지 알아내기
print(index_A)

for i in range(len(A)):
    min_index=index_A.index(min(index_A))
    
    "".join(map(str,A[min_index:]))
    index_A[min_index]=999   #큰수를 가짜로 넣어서 min index 후보에서 제외되게 함


