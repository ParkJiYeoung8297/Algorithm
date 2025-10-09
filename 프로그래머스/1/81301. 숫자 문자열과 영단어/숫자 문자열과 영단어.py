def solution(s):
    dict_s={"zero":0, "one":1,"two":2,"three":3,"four":4,"five":5,"six":6,
            "seven":7,"eight":8,"nine":9}
    for k in dict_s.keys():
        while (1):
            if s.find(k)!=-1:
                s=s.replace(k,str(dict_s[k]))
            else:
                break

    return int(s)