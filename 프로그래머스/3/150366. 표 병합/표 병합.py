# union find를 이용해서 merge와 unmerge 구현하기
# 루트들의 값만 저장해서 update 성능 높히기

from collections import defaultdict
def solution(commands):
    answer = []

    parent={(r,c):(r,c) for r in range(51) for c in range(51)}
    group=defaultdict(set)
    word={} # 루트의 값
    for r in range(51):
        for c in range(51):
            group[(r,c)].add((r,c))

    def find_parent(x):
        if parent[x]!=x:
            parent[x]=find_parent(parent[x])
        return parent[x]
    
    def union(x1,x2):
        parent1=find_parent(x1)
        parent2=find_parent(x2)
        
        if parent1==parent2: # 부모 좌표가 같으면 이미 병합된 상태
            return
        
        parent[parent2]=parent1 # r1,c1 값이 우선 순위이므로 parent1을 parent2의 부모로 함
        group[parent1]=group[parent1].union(group[parent2])
        group[parent2].clear()
        
        val = "EMPTY"
        if parent1 in word:
            val = word[parent1]
        elif parent2 in word:
            val = word[parent2]

        # 모두 EMPTY일 때는 word에 key를 만들지 말아야 한다!
        if val != "EMPTY":
            word[parent1] = val

        if parent2 in word:
            del word[parent2]
        
    for command in commands:
        C=command.split(" ")
        if C[0]=="UPDATE":
            if len(C)==4:
                r,c,value1=int(C[1]), int(C[2]), C[3]
                root=find_parent((r,c))
                if root not in word:
                    word[root]=""
                word[root]=value1

            elif len(C)==3:
                value1,value2=C[1],C[2]
                for key in word.keys():
                    if word[key]==value1:
                        word[key]=value2

        elif C[0]=="MERGE":
            r1,c1,r2,c2=int(C[1]), int(C[2]), int(C[3]), int(C[4])
            union((r1,c1),(r2,c2))
                
        elif C[0]=="UNMERGE":
            r,c=int(C[1]), int(C[2])
            root=find_parent((r,c))
            val="EMPTY"
            if root in word: # 단어 삭제
                val=word[root]

            # 그룹 전체 해제
            for cell in list(group[root]):
                parent[cell] = cell
                group[cell] = {cell}
                if cell in word:
                    del word[cell]
            
            if val!="EMPTY":
                word[(r,c)]=val

        elif C[0]=="PRINT":
            r,c=int(C[1]), int(C[2])
            value="EMPTY"
            root=find_parent((r,c))
            if root in word:
                value=word[root]
            answer.append(value) 
            
    return answer