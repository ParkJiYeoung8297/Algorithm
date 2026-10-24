// 최단 경로는 BFS
// BFS는 큐에 값을 넣자마자 방문처리해야함

import java.util.*;
class Solution {
    static int[] dx = {0, 0, 1, -1}; // 위, 아, 오, 왼
    static int[] dy = {-1, 1, 0, 0}; 
    static int mx;
    static int my;
    static int[][] visited;
        
    
    public int solution(int[][] maps) {
        my = maps.length;
        mx = maps[0].length;
        
        ArrayDeque<int[]> queue = new ArrayDeque<>();  
        queue.addLast(new int[]{0,0,0}); // 경로합, x, y
        maps[0][0]=0;
        
        while(!queue.isEmpty()){
            int[] result = queue.removeFirst();
            
            int x = result[1];
            int y = result[2];
            
            if (x==mx-1 && y==my-1){
                return result[0]+1;
            }
            
            for (int i=0; i<4; i++){
                int nx = dx[i] + x;
                int ny = dy[i] + y;
                
                if (nx<mx && ny<my && 0<=nx && 0<=ny && maps[ny][nx]==1){
                    queue.addLast(new int[]{result[0]+1,nx,ny});
                    maps[ny][nx] = 0; // 재방문 못하도록
                }
            }
            
        }
        
        return -1;
    }
}