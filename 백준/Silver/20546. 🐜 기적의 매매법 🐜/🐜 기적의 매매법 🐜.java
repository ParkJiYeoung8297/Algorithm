import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int money = Integer.parseInt(br.readLine());

        List<Integer> prices = Arrays.stream(br.readLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        int i = getBnpPrice(prices, prices.size(), money);
        int j = getAllSellPrice(prices, prices.size(), money);
//        System.out.println(i);
//        System.out.println(j);
        if(i>j){
            System.out.println( "BNP");
        }
        else if (i<j){
            System.out.println("TIMING");
        }
        else{
            System.out.println("SAMESAME");
        }

    }

    // 마지막 날 주식의 개수가 중요
    public static int getBnpPrice(List<Integer> timing, int days, int money) {
        int stock = 0;
        for (int i = 0; i < days; i++) {
            int buy = money / timing.get(i);
            stock += buy;
            money -= buy * timing.get(i);
        }
        return stock * timing.get(timing.size()-1)+money;
    }

    public static int getAllSellPrice(List<Integer> timing, int days, int money) {
        int stock = 0;
        int upRates = 0;
        int downRates = 0;

        for (int i = 1; i < days; i++) {
//            System.out.printf("%d  %d  %d  \n", i, money, stock);
            if (timing.get(i) > timing.get(i - 1)) {
                upRates++;
                downRates = 0;
            }

            if (timing.get(i) < timing.get(i - 1)) {
                downRates++;
                upRates = 0;
            }

            if (downRates >= 3) {
                int buy = money / timing.get(i);
                stock += buy;
                money -= buy * timing.get(i);
            }

            if (upRates >= 3) {
                money += stock * timing.get(i);
                stock = 0;
            }

        }
        return stock * timing.get(timing.size()-1) + money;
    }


}