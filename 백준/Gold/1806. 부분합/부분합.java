import java.io.*;
import java.util.*;

public class Main_1806 {

    public static int N;
    public static int M; 
    public static int[] seq;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken()); 

        seq = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {seq[i] = Integer.parseInt(st.nextToken());}

        int start = 0;
        int end = 0;
        long sum = 0;
        int minLength = Integer.MAX_VALUE;

        while (true) {
            // 누적합>=M -> start 오른쪽으로 (새로운 수를 탐색하기 위해 윈도우 축소)
            if (sum >= M) {
                minLength = Math.min(minLength, end - start);
                sum -= seq[start++];
            }
            // end가 배열 벗어나기 전에 종료 
            else if (end == N) {
                break;
            }
            // 누적합 <M -> end를 오른쪽으로 (확장)
            else {
                sum += seq[end++];
            }
        }

        if (minLength == Integer.MAX_VALUE) {System.out.println(0);} 
        else {System.out.println(minLength);}

        br.close();
    }
}
