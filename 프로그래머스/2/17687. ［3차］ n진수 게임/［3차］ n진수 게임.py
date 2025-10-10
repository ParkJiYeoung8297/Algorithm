def radixChange(number,n):
    if number==0:
        return "0"
    answer=[]
    while (number!=0):
        answer.append(str(number%n))
        number=number//n
    return answer[::-1]

def radixTenChange(number,n,dict_n):
    if number==0:
        return "0"
    answer=[]
    while number:
        if number%n>=10:
            answer.append(dict_n[number%n])
        else:
            answer.append(str(number%n))
        number=number//n
    return answer[::-1]

def solution(n, t, m, p):
    answer = ''
    dict_n={10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    result=[]
    number=0
    while (1):
        if len(result)>=m*(t-1)+p:
            break
        if number<10:
            result+=radixChange(number,n)
        else:
            result+=radixTenChange(number,n,dict_n)
        number+=1
    
    answer="".join([result[idx*m+p-1] for idx in range(t)])
 
    return answer