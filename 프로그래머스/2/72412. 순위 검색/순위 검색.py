# 가장 간단하게는 조건들을 dict 키값으로 해서 점수를 저장한다. 
# 이때, - 를 고려해서 미리 만들어두는게 좋다. 
# (등록할때는 가짓수가 얼마 안되니, 등록할 떄 만들기, 질의에서 만들면 너무 반복임)
# 미리 점수 정렬하고 이진 탐색 이용해서 빠르게 찾기
import bisect

def solution(info, query):
    answer = []
    dict_i={}
    for i in info:
        elements=list(i.split(" "))
        score=int(elements.pop())
        
        
        # 미리 - 고려해서 만들어두기
        for l in [elements[0],"-"]:  
            for j in [elements[1],"-"]:
                for e in [elements[2],"-"]:
                    for f in [elements[3],"-"]:
                        key=" ".join([l,j,e,f])
                        if key not in dict_i:
                            dict_i[key]=[]
                        dict_i[key].append(score)
    for i in dict_i:
        dict_i[i]=sorted(dict_i[i])
        
    # 질의 진행
    for q in query:
        count=0
        elements=list(q.split(" and "))
        elements[3], target=elements[3].split(" ")
        target=int(target)
        
        option=" ".join(elements)
        if option in dict_i:
            # 이진 탐색하여 인원 수 더하기
            idx = bisect.bisect_left(dict_i[option], target)
            count += len(dict_i[option])-idx
            answer.append(count)
        else:
            answer.append(0)

            
    return answer
