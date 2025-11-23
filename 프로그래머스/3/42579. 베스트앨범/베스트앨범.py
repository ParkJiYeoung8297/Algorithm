from collections import defaultdict
def solution(genres, plays):
    answer = []
    G=defaultdict(list)
    count=defaultdict(int)
    for idx,value in enumerate(plays):
        count[genres[idx]]+=value
        G[genres[idx]].append((-value,idx))
    genre=sorted(count.keys(), key=lambda x:count[x],reverse=True)
    
    for g in genre:
        if len(G[g])==1:
            answer.append(G[g][0][1])
            continue
        G[g].sort()
        answer.append(G[g][0][1])
        answer.append(G[g][1][1])

        
    return answer