import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int n = 0;
        for (int[] command : commands){
            int i = command[0]-1;
            int j = command[1]-1;
            int k = command[2]-1;
            ArrayList<Integer> newList = new ArrayList<>();
            
            for (int x = i; x<j+1; x++){
                newList.add(array[x]);
            }
            Collections.sort(newList);
            answer[n]=newList.get(k);
            n++;
        }
        return answer;
    }
}