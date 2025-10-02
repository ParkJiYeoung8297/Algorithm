# 아이디어 : 음수인 상태를 이용. 값이 음수라면 다시 원점 안가고 추가로 배달할 수 있음
# 순서는 뒤에서 앞으로
# 거리는 값이 양수가 되어 원점을 찍어야할 때 갱신
# (와..이걸 어떻게 생각하냐.. 출처 : https://oh2279.tistory.com/147)
def solution(cap, n, deliveries, pickups):
    distance=0
    deliveries=deliveries[::-1]
    pickups=pickups[::-1]
    
    have_to_del=0
    have_to_pick=0
    
    for i in range(n):
        have_to_del+=deliveries[i]
        have_to_pick+=pickups[i]
        
        while have_to_del>0 or have_to_pick>0:
            have_to_del-=cap
            have_to_pick-=cap
            distance+=(n-i)*2
    return distance