from collections import defaultdict
def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    S1=defaultdict(int)
    S2=defaultdict(int)
    
    # 두 문자씩 자르기
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            S1[str1[i]+str1[i+1]]+=1
    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            S2[str2[i]+str2[i+1]]+=1
    
    S1_set=set(S1.keys())
    S2_set=set(S2.keys())
    
    int_total=0
    uni_total=0
    
    for k in S1_set.intersection(S2_set):
        int_total+=min(S1[k],S2[k])
        
    for k in S1_set.union(S2_set):
        uni_total+=max(S1[k],S2[k])
    
        
    return int((int_total/uni_total)*65536) if uni_total!=0 else 65536