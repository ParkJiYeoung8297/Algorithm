// 배열 최대값 구하기: Arrays.stream(배열_이름).max().getAsInt();
// 리스트를 배열로 바꾸기 : 리스트_이름.stream().mapToInt(Integer::intValue).toArray()
// IntStream.range(0, student.length).filter(i -> student[i] == maxScore).map(i -> i + 1).toArray(); 으로 줄여서 사용할 수도 있음
import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] student = new int[4];
        
        for (int i=0;i<answers.length;i++){
            student[1]=student[1]+calculateOne(i, answers[i]);
            student[2]=student[2]+calculateTwo(i, answers[i]);
            student[3]=student[3]+calculateThree(i, answers[i]);
        }
        int maxScore = Arrays.stream(student).max().getAsInt();
        List<Integer> cand = new ArrayList<>();
        for (int i =1;i<4;i++){
            if (student[i]==maxScore){
                cand.add(i);
            }
        }
        
        return cand.stream().mapToInt(Integer::intValue).toArray();
    }
    
    private int calculateOne(int i, int answer){
        int[] one = {1, 2, 3, 4, 5};
        if(one[i%5]==answer){
            return 1;
        }
        return 0;
    }
    
    private int calculateTwo(int i, int answer){
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        if(two[i%8]==answer){
            return 1;
        }
        return 0;
        
    }
    
    private int calculateThree(int i, int answer){
        int[] three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        if(three[i%10]==answer){
            return 1;
        }
        return 0;
    }
}