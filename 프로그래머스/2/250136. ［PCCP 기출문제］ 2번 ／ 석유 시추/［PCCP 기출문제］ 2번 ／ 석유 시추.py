from collections import deque

def solution(land):
    answer =[0]*len(land[0])
    visited=[[0]*len(land[0]) for _ in range(len(land))]
    
    # 땅 사이즈 구하기
    def getLandSize(y,x):
        total=1
        queue=deque()
        queue.append((y,x))
        visited[y][x]=1
        x_dict={x:0} # 이 석유가 지나는 열 번호를 모두 구함
        directions=[(-1,0),(0,-1),(0,1),(1,0)] # y,x


        while queue:
            curr_y,curr_x=queue.pop()
            for d in directions:
                new_y,new_x=curr_y+d[0],curr_x+d[1]
                if new_y>=0 and new_x>=0 and new_y<len(land) and new_x<len(land[0]) and land[new_y][new_x]==1 and visited[new_y][new_x]==0:
                    total+=1
                    if new_x not in x_dict:
                        x_dict[new_x]=0
                    visited[new_y][new_x]=1
                    queue.append((new_y,new_x))
        return total, x_dict
    
    # 탐색
    for x in range(len(land[0])):
        for y in range(len(land)):
            if land[y][x]==1 and visited[y][x]==0:
                size, dict_x=getLandSize(y,x)
                for i in dict_x.keys():
                    answer[i]+=size
   
    return max(answer)