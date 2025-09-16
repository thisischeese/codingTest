import java.io.*;
import java.util.*;

public class Main {

    public static List<Long> list;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        list = new ArrayList<>();

        // N이 1022보다 크면 감소하는 수는 절대 나올 수 없음
        if (N > 1022) {
            System.out.println(-1);
            return;
        }
        // 발생 가능한 모든 감소하는 수 리스트에 추가 
        for (int i = 0; i < 10; i++) {
            getNum(i);
        }

        Collections.sort(list);

        // N번째 값 출력
        System.out.println(list.get(N));
    }

    public static void getNum(long num) {
        list.add(num); 
        long last = num % 10;
        
        // 마지막 자릿수보다 작은 수 뒤에 붙여 새로운 수를 만들기..
        for (int i = 0; i < last; i++) {
            long newNum = (num * 10) + i;
            getNum(newNum);
        }
    }
}