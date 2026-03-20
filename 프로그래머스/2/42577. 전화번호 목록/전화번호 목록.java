// [그리디..인가?]
// String은 contains 보다 String_변수명.startsWith("sss")이 더 빠르다.
// 길이가 짧은 거 기준으로 정렬하고 찾으려고 했는데, 사전식 정렬하는게 나음. 바로 뒤랑만 비교하면 된다.
// 참고 - 길이 정렬:Arrays.sort(phone_book,Comparator.comparingInt(String::length));

import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for (int i=0;i<phone_book.length-1;i++) {
            if (phone_book[i+1].startsWith(phone_book[i])){
                return false;
            }
        }
        return true;
    }
}