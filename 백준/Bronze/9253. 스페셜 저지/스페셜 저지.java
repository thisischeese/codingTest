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

    public static boolean search(String t, String p) {
        if (p.length() > t.length()) {
            return false;
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
                    return true;
                } else {
                    j++;
                }
            }
        }
        
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String sa = br.readLine();
        String sb = br.readLine();
        String ans = br.readLine();

        boolean isA = search(sa, ans);
        boolean isB = search(sb, ans);

        if (isA && isB) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}