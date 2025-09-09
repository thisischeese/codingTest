import java.io.*;
import java.util.*;

public class Main {

    public static int k;
    public static char[] arr;
    public static boolean[] v;
    public static String min = "";
    public static String max = "";
    public static ArrayList<String> answer = new ArrayList<>();

    public static void bt(int cnt, String currentNum) {
        if (cnt == k + 1) {
            answer.add(currentNum);
            return;
        }

        for (int i = 0; i <= 9; i++) {
            if (!v[i]) { 
                if (cnt == 0 || check(Character.getNumericValue(currentNum.charAt(cnt - 1)), i, arr[cnt - 1])) {
                    v[i] = true;
                    bt(cnt + 1, currentNum + i);
                    v[i] = false;
                }
            }
        }
    }

    public static boolean check(int a, int b, char op) {
        if (op == '<') {
            return a < b;
        } else {
            return a > b;
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        k = Integer.parseInt(br.readLine());
        arr = new char[k];
        v = new boolean[10];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            arr[i] = st.nextToken().charAt(0);
        }

        bt(0, "");

        System.out.println(answer.get(answer.size() - 1));
        System.out.println(answer.get(0));
        
        br.close();
    }
}