import heapq
def solution(operations):
    answer = []
    queue=[]


    for oper in operations:
        op=oper.split(" ")
        if op[0]=="I":
            heapq.heappush(queue,int(op[1]))
        if queue:
            if op[0]=="D" and op[1]=="-1":
                heapq.heappop(queue)
            if op[0]=="D" and op[1]=="1":
                queue.remove(max(queue))

    # 마지막 정렬 필요 (heap은 최솟갑을 빠르게 찾는거지, 정렬이 되어있는게 아님)
    queue.sort()
    if len(queue)==0:
        answer=[0,0]
    elif len(queue)==1:
        answer=[queue[0],queue[0]]
    elif len(queue)>=2:
        answer=[queue[-1],queue[0]]
    return answer