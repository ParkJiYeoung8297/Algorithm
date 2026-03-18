// [배열 문제]
// sum(arr1[i][]의 행 * arr2[][j]의 열) 한 것이 return[i][j] 값
// 곱할 수 있는 배열 이란 a*b b*c → a*c

import java.util.*;
class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];
        
        for (int i=0;i<arr1.length;i++){
            for (int j=0;j<arr2[0].length;j++){
                int total = 0;
                for (int idx=0;idx<arr2.length;idx++){
                    total+=arr1[i][idx]*arr2[idx][j];
                }
                answer[i][j]=total;
            }
            
        }
        return answer;
    }
}