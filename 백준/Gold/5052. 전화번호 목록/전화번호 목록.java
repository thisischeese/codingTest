import java.io.*;
import java.util.*;

public class Main {

	public static int t; 
	public static String[] nums;
	public static StringBuilder sb = new StringBuilder();
	public static String solution() {
        // 1. 전화번호 목록을 사전순으로 정렬한다.
        Arrays.sort(nums);
        
        // 2. 인접한 번호끼리 접두어 관계인지 확인한다.
        // 마지막 번호는 비교 대상이 없으므로 n-1까지만 반복한다.
        for (int i = 0; i < nums.length - 1; i++) {
            // 다음 번호가 현재 번호로 시작하는지(접두어인지) 확인한다.
            if (nums[i+1].startsWith(nums[i])) {
                // 접두어인 경우가 하나라도 있으면 일관성이 없으므로 "NO"를 반환한다.
                return "NO";
            }
        }
        
        // 반복문이 끝날 때까지 접두어 관계를 찾지 못했다면 일관성이 있는 것이다.
        return "YES";
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            nums = new String[n];
            for (int i = 0; i < n; i++) {
                nums[i] = br.readLine();
            }

            sb.append(solution()).append("\n");
        }
        System.out.print(sb.toString());
        br.close();
    }

    
}

