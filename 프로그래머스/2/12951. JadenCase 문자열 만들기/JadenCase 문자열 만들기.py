def solution(s):
    answer = ''
    s=s.lower()
    S=list(s)
    # 첫문자이거나 이전에 공백이면 대문자
    # 조건 : 알파벳
    if S[0].isalpha():
        S[0]=S[0].upper()
        
    for i in range(1,len(S)):
        if S[i-1]==" " and S[i].isalpha():
            S[i]=S[i].upper()
    return "".join(S)