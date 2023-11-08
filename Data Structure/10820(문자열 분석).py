import sys
import string
import re

Alpha=list(string.ascii_uppercase)
alpha=list(string.ascii_lowercase)

while(1):
    data=list(sys.stdin.readline().strip("\n"))
    if not data: #더 읽을 라인이 없으면 종료
        break
    result_dic={"alpha":0,"Alpha":0,"number":0,"space":0}

    for i in data:
        if i in alpha:
            result_dic["alpha"]=result_dic["alpha"]+1
        elif i in Alpha:
            result_dic["Alpha"]=result_dic["Alpha"]+1
        elif i ==" ":
            result_dic["space"]=result_dic["space"]+1
        elif re.compile("[0-9]")!=None:   #여기서는 대소문자,공백,숫자로 input이 정해져있기 때문에 숫자인지 아닌지를 이렇게 할 수 있는거
            result_dic["number"]=result_dic["number"]+1

    result=" ".join(map(str,result_dic.values()))
    print(result)