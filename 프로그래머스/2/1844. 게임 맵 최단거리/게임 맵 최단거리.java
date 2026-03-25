// 가장 빠른 길은 BFS로 구하기 
// 상하좌우 움직이는 건 dx, dy 사용
// Integer[]에다가 {x, y, cost}를 저장하고, Deque에 넣어서 풀었음 (근데 객체를 만들어서 하는거 추천)
// 방문처리는 stack에 넣어줄 때 한다. 
import java.util.*;
class Solution {
    public static final int[] dx={1,-1,0,0};
    public static final int[] dy={0,0,1,-1};
    
    public int solution(int[][] maps) {
        Integer[] start ={0,0,1};  // x, y, cost
        return bfs(start,maps);
    }
    
    private int bfs(Integer[] position, int[][] maps){
        Deque<Integer[]> stack = new ArrayDeque<>();
        stack.add(position);
        
        while(!stack.isEmpty()){
            Integer[] now = stack.poll();
            
            if (now[0]==maps[0].length-1 && now[1]==maps.length-1){
                return now[2];
            }
            
            for (int i=0;i<4;i++){
                Integer new_x=now[0]+dx[i];
                Integer new_y=now[1]+dy[i];
                Integer[] newPosition = {new_x,new_y,now[2]+1};

                if (0<=new_x && new_x<=maps[0].length-1 && 0<=new_y && new_y<=maps.length-1 && maps[new_y][new_x]==1){
                    stack.add(newPosition);
                    maps[new_y][new_x]=0;
                }
            }
        }
        return -1;
    }
}