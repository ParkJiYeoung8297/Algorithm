from collections import defaultdict
def solution(str1, str2):
    answer = 0
    dict_one=defaultdict(int)
    dict_two=defaultdict(int)
    for i in range(len(str1)-1):
        string=(str1[i]+str1[i+1]).lower()
        if string.isalpha():
            dict_one[string]+=1
    for i in range(len(str2)-1):
        string=(str2[i]+str2[i+1]).lower()
        if (string).isalpha():
            dict_two[string]+=1
    
    set_one=set(dict_one.keys())
    set_two=set(dict_two.keys())
    
    inter=set_one.intersection(set_two)
    un=set_one.union(set_two)
    
    up=0
    down=0
    for s in inter:
        up+=min(dict_one[s],dict_two[s])
    for s in un:
        down+=max(dict_one[s],dict_two[s])
  
    return int((up/down)*65536) if down!=0 else 65536