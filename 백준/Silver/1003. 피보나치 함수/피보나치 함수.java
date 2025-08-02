import java.io.*;
import java.util.*; 

public class Main {
	static StringBuilder sb = new StringBuilder(); 
	static int[] dp_0 = new int[41];
	static int[] dp_1 = new int[41];
	

	// 각 숫자마다 0이 필요한 횟수, 1이 필요한 횟수를 기록하는 DP
	public static void fib_dp(int N) {
		for(int i =2;i<N+1;i++) {
			dp_0[i] = dp_0[i-1] + dp_0[i-2];
			dp_1[i] = dp_1[i-1] + dp_1[i-2];}
		
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		int T = Integer.parseInt(br.readLine()); 
		// dp 테이블 초기화 
		dp_0[0] = 1; dp_0[1] = 0; 
		dp_1[0] = 0; dp_1[1] = 1; 
		fib_dp(40); 
		
		for(int t = 0; t<T; t++) {
			int N = Integer.parseInt(br.readLine()); 
			sb.append(dp_0[N]+" ").append(dp_1[N]+"\n");
		}
		System.out.println(sb.toString());
		br.close();
	}

}
