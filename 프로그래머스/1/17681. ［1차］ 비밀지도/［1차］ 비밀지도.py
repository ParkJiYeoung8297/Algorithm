
def solution(n, arr1, arr2):
    answer = []

    # 변환
    for i in range(len(arr1)):
        bin_a=bin(arr1[i])[2:]
        bin_b=bin(arr2[i])[2:]
        
        if len(bin_a)!=n:
            bin_a="0"*(n-len(bin_a))+bin_a
            
        if len(bin_b)!=n:
            bin_b="0"*(n-len(bin_b))+bin_b
            
        temp=[]
        for i in range(len(bin_a)):
            if bin_a[i]=="0" and bin_b[i]=="0":
                temp.append(" ")
            else:
                temp.append("#")    
        answer.append("".join(temp))
        
    return answer