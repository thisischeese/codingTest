import java.io.*;
import java.util.*;

public class Main {

	public static int len1, len2;
	public static String s1,s2;
	public static int[][] dp; 
	
    public static void solution() {
        
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                
                // 현재 비교하는 문자가 서로 같다면
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    // 왼쪽 대각선 위 값에 +1
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } 
                // 다르다면
                else {
                    // 왼쪽 값과 위쪽 값 중 더 큰 값을 선택
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
    }
	
    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s1 = br.readLine();
        s2 = br.readLine();
        
        len1 = s1.length();
        len2 = s2.length();
        
        // 1 base
        dp = new int[len1 + 1][len2 + 1];
        
        solution();
        
        br.close();
        System.out.println(dp[len1][len2]);
    }
    

}
