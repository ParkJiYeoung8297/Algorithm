import sys
import string

#데이터 읽기
data=list(sys.stdin.readline().strip())

result=[-1]*26
alpha={}
count=0
a=list(string.ascii_lowercase)
readout=[]

for i in a:    #{"a":0,"b":1 ...} 이렇게 저장
    alpha[i]=count
    count=count+1

for i in range(len(data)):  #읽은 data로 result값 갱신
    if data[i] not in readout:  #처음 등장한 위치니까 처음 등장했을때만 갱신해줌
        result[alpha[data[i]]]=i
    readout.append(data[i])  

result_print=" ".join(map(str,result))  #출력에 맞는 형식으로 바꿈
print(result_print)