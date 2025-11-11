def solution(a):
    answer = 0
    
    # 왼쪽에서 최소이거나, 오른쪽에서 최소이면 산다.
    # 반대쪽에 더 작은 값 있더라도, 그게 나머지 다 터트리고 찬스로 그 작은 거 잡으면 되니까.
    
    min_left=[0]*len(a)
    min_right=[0]*len(a)
    
    min_value=float("inf")
    for i in range(len(a)):
        min_value=min(min_value,a[i])
        min_left[i]=min_value
        
    min_value=float("inf")
    for i in range(len(a)-1,-1,-1):
        min_value=min(min_value,a[i])
        min_right[i]=min_value
    
    
    for i in range(len(a)):
        if min_right[i]==a[i] or min_left[i]==a[i]:
            answer+=1
    
        
    return answer