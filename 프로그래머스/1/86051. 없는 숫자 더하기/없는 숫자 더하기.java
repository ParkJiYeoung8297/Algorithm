import java.util.List;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] numbers) {
        int answer = -1;
        List<Integer> nums=Arrays.stream(numbers)
                            .boxed()
                            .sorted()
                            .collect(Collectors.toList());
        
        // System.out.println(nums.toString());
        for (int i=0;i<10;i++){
            if (!nums.contains(i)){
                answer+=i;
            }
        }
        
        if (answer!=-1){
            answer+=1;
        }
        return answer;
    }
}