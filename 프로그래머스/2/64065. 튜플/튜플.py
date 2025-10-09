def solution(s):
    answer = []
    dict_s={}
    S=[tuple(i.split(",")) for i in s[2:-2].split("},{")]
    S.sort(key=lambda x:len(x))
    for i in S:
        for j in i:
            if j not in dict_s:
                answer.append(j)
                dict_s[j]=1
    return list(map(int,answer))