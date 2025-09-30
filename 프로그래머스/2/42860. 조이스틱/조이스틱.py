# 프로그래머스 책 참고하기 (어렵다..)
def solution(name):
    answer=0
    min_move=len(name)-1
    size=len(name)
    
    
    for i in range(len(name)):
        # 세로 고려 (해당 숫자로 위 아래 누르기) → ascii 로 고쳐서 간격 계산
        # 후자의 경우는 커서 이동 1번 필요하니까 +1
        answer+=min(ord(name[i])-ord("A"),ord("Z")-ord(name[i])+1) 
        
        # A 지날때까지
        next_idx=i+1
        while next_idx<size and name[next_idx]=="A":
            next_idx+=1
        
        # 가로 고려
        # 그냥 전진, 오른쪽 가다가 뒤돌아서 가는거, 왼쪽 가다가 뒤돌아서 가는거
        min_move=min(min_move,i*2+(size-next_idx), (size-next_idx)*2+i)
    answer+=min_move
    return answer