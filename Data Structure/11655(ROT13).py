import sys 
import string
from collections import deque

A=deque(sys.stdin.readline().strip('\n'))
B=deque()

alpha=list(string.ascii_lowercase)

for i in range(len(A)):
    a=A.popleft()
   
    if a.isalpha()!=True:  #숫자, 공백은 그대로
        B.append(a)
    else:
        if a.lower()==a: #소문자
            a_index=alpha.index(a)+13 #13글자 뒤로
            if a_index>=26:  
                a_index=a_index-26
                a=alpha[a_index]
            else:
                a=alpha[a_index]
            B.append(a)
        else:  #대문자
            a_index=alpha.index(a.lower())+13 #13글자 뒤로
            if a_index>=26:  
                a_index=a_index-26
                a=alpha[a_index]
            else:
                a=alpha[a_index]
            B.append(a.upper())
print("".join(map(str,B)))