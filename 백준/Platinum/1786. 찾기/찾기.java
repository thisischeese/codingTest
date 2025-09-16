import java.io.*;
import java.util.*;

public class Main {

    public static int[] makeTable(String p) {
        int pl = p.length();
        int[] pi = new int[pl];
        
        for (int i = 1, j = 0; i < pl; i++) {
            while (j > 0 && p.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (p.charAt(i) == p.charAt(j)) {
                pi[i] = ++j;
            }
        }
        return pi;
    }

    public static List<Integer> search(String t, String p) {
        List<Integer> result = new ArrayList<>();
        if (p.length() > t.length()) {
            return result;
        }

        int[] pi = makeTable(p);
        int tl = t.length();
        int pl = p.length();

        for (int i = 0, j = 0; i < tl; i++) {
            while (j > 0 && t.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }

            if (t.charAt(i) == p.charAt(j)) {
                if (j == pl - 1) {
                    // 패턴 일치! 1-based 시작 위치를 리스트에 추가
                    result.add(i - pl + 2);
                    // 다음 일치 탐색을 위해 pi 배열 값으로 j 이동
                    j = pi[j];
                } else {
                    j++;
                }
            }
        }
        
        return result;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String T = br.readLine();
        String P = br.readLine();

        List<Integer> result = search(T, P);

        System.out.println(result.size());

        StringBuilder sb = new StringBuilder();
        for (int pos : result) {
            sb.append(pos).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}