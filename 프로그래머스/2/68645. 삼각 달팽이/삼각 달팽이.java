// 직각삼각형으로 풀기
// 아래, 오른쪽,왼쪽 위로 움직임
import java.util.*;
class Solution {
    public static int[] dx ={0 , 1, -1};
    public static int[] dy ={1, 0, -1};
    public static int idx=0;
    public static int nx = 0;
    public static int ny =0;
    
    public int[] solution(int n) {
        int start = 1;
        int end = (n+1)*n/2;
        
        int[][] matrix = new int[n][n];
        int[] answer = new int[end];
        
        while(start<=end){
            if (isInRange(n) && matrix[ny][nx]==0){
                matrix[ny][nx]=start;
                start++;
            }
            else{
                ny-=dy[idx];
                nx-=dx[idx];
                idx=(idx+1)%3;
            } 
            ny+=dy[idx];
            nx+=dx[idx];
        }
        
        int number = 0;
        for (int y = 0; y<n; y++ ){
            for (int x=0; x<n; x++){
                if (matrix[y][x]==0){
                    break;
                }
                answer[number]=matrix[y][x];
                number++;
            }
        }
        return answer;
    }
    
    public boolean isInRange(int n){
        if (nx<0 || ny<0 || nx>=n || ny>=n){
            return false;
        }
        return true;
    }
}