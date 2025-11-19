import heapq
def solution(operations):
    answer = []
    heap=[]
    for op in operations:
        A=op.split(" ")
        if A[0]=="I":
            heapq.heappush(heap,int(A[1]))
        elif A[0]=="D" and heap:
            if A[1]=="1":
                value=max(heap)
                heap.remove(value)
            elif A[1]=="-1":
                heapq.heappop(heap)
    return [max(heap),heapq.heappop(heap)] if heap else [0,0]