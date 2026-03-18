// [dfs + 백트래킹]
// dfs로 경우의 수 찾아보기
// 선택하거나 안하거나 둘 중 하나다.

import java.util.*;
class Solution {
    private boolean[] check;
    private int answer=0;
    
    public int solution(int k, int[][] dungeons) {
        check = new boolean[dungeons.length];
        dfs(0,dungeons,k);
        return answer;
    }
    
    private void dfs(int count, int[][] dungeons , int energy){
        for (int i=0;i<dungeons.length;i++){
            if (!check[i] && dungeons[i][0]<=energy){
                check[i]=true;
                dfs(count+1,dungeons,energy-dungeons[i][1]);
                check[i]=false;
            }
        }
        answer=Math.max(answer,count);
    }
}