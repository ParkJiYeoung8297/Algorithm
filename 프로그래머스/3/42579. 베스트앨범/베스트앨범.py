from collections import defaultdict
def solution(genres, plays):
    answer = []
    count=defaultdict(int)
    music=defaultdict(list)
    
    for i in range(len(genres)):
        music[genres[i]].append((plays[i],-i)) # play는 큰거, i는 작은거가 우선순위
        count[genres[i]]+=plays[i]

    sorted_count=sorted(count.keys(),reverse=True,key=lambda x:count[x])
    
    for c in sorted_count:
        music[c].sort(reverse=True)
        if len(music[c])==1:
            answer.append(-music[c][0][1])
        elif len(music[c])>=2:
            answer.append(-music[c][0][1])
            answer.append(-music[c][1][1])
        
    return answer