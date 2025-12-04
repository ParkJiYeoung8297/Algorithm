# dist 가 큰 사람순으로 들어가는게 유리 
# 시작점은 weak 점들 중 하나, (방향은 크게 중요하지 않음)
# 이 문제는 순열로 풀어야함 (대신 범위를 줄여서)
from itertools import permutations
def solution(n, weak, dist):
    length=len(weak)
    weak = weak + [w + n for w in weak]  # 원형 탐색을 위해 리스트 연장
    dist.sort(reverse=True)
    answer=len(dist)+1

    for start in range(length):
        for friends in permutations(dist):
            count=1
            # 첫번째
            position=weak[start]+friends[count-1]
            for idx in range(start,start+length):
                if weak[idx]>position:
                    # 사람 추가
                    count+=1
                    if count>len(friends):
                        break
                    position=weak[idx]+friends[count-1]

            
            answer=min(answer,count)
            
    if answer>len(dist):
        return -1
    else:
        return answer