import java.io.*; 
import java.util.*; 

public class Main {

	// 
	public static long[] P(int n) {
		long dp[] = new long[n+1]; 
		dp[1] = 1; dp[2] = 1; dp[3] =1; 
		// 1 1 1
		// 2 2 3
		// 4 5 7
		// 9 12 16 
		for(int i=4;i<=100;i++) {
			if(i%3==1) {dp[i] = dp[i-3]+dp[i-2];}
			else if(i%3==2) {dp[i] = dp[i-3]+dp[i-2];}
			else {dp[i] = dp[i-2]+dp[i-3];}
		}
		return dp; 
	}
	
	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		long[] dp = P(100);
		for(int i=0;i<N;i++) {
			int n = Integer.parseInt(br.readLine()); 
			sb.append(dp[n]).append("\n");
		}
		
		br.close();
		System.out.println(sb.toString());
	}

}
