import java.util.*;
class Solution {
    public String solution(int n, int k, String[] cmd) {
        int pointer=k+1;
        Stack<Integer> deleted = new Stack<>();
        
        int[] up = new int[n+2];
        int[] down = new int[n+2];
        for (int i = 0; i<n+2; i++){
            up[i]=i-1;
            down[i]=i+1;
        }
        
        for (String c : cmd){
            if (c.startsWith("U")){
                String[] s = c.split(" ");
                int num = Integer.parseInt(s[1]);
                while(num>0){
                    pointer = up[pointer];
                    num--;
                }
                
            } else if(c.startsWith("D")){
                String[] s = c.split(" ");
                int num = Integer.parseInt(s[1]);
                while(num>0){
                    pointer = down[pointer];
                    num--;
                }
            } else if(c.startsWith("C")){
                deleted.push(pointer);
                up[down[pointer]]=up[pointer];
                down[up[pointer]]=down[pointer];
                pointer=n<down[pointer] ? up[pointer] : down[pointer];
                    
            } else if(c.startsWith("Z")){
                int restore = deleted.pop();
                up[down[restore]] = restore;
                down[up[restore]] = restore;
            } else{
                System.out.println("오류");
            }
        }
        
        char[] answer = new char[n];
        Arrays.fill(answer,'O');
        for (int i : deleted){
            answer[i-1]='X';
        }
        
        return new String(answer);
    }
}