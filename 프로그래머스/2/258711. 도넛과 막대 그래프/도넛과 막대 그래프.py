from collections import defaultdict
def solution(edges):
    answer = []
    # 들어오는 간선과 나가는 간선의 수로 판단하기
    in_get=defaultdict(int)
    out_get=defaultdict(int)
    
    nodes=set([u for u,v in edges]+[v for u,v in edges])
    
    for u,v in edges:
        out_get[u]+=1
        in_get[v]+=1
        
    generated_node=[node for node in nodes if in_get[node]==0 and out_get[node]>=2][0]
    
    # 생성된 정점과 간선 삭제

    total=out_get[generated_node]
    in_get=defaultdict(int)
    out_get=defaultdict(int)
    
    nodes.remove(generated_node)
    removes_edges=[[u,v] for u,v in edges if u!=generated_node]
    
    for u,v in removes_edges:
        out_get[u]+=1
        in_get[v]+=1

    # 막대 (size=1인경우는 1번, size>=2인 경우는 2번 count 되니까 추가 계산 필요)
    barCount=sum([1 for node in nodes if in_get[node]==0 or out_get[node]==0])
    barCount+=sum([1 for node in nodes if in_get[node]==0 and out_get[node]==0])
    barCount=barCount//2
    
    # 8자
    eightCount=sum([1 for node in nodes if in_get[node]==2 and out_get[node]==2])
    
    #도넛
    
    donutCount=total-barCount-eightCount
    
    
    return [generated_node,donutCount,barCount,eightCount]