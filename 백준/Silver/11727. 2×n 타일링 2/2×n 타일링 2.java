import java.io.*; 
import java.util.*; 

public class Main {

	public static int N; 
	public static int[] dp; 
	public static StringBuilder sb = new StringBuilder(); 
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		N = Integer.parseInt(br.readLine()); 
		
		
		dp = new int[N+1]; 
		dp[1] = 1;
		if(N>=2) {
			dp[2] = 3;
			if(N>=3) {
				for(int i=3;i<N+1;i++) {
					dp[i] = (dp[i-1] + dp[i-2]*2)%10007; 
				}
			}
		}
		sb.append(dp[N]);
		br.close();
		System.out.println(sb.toString());
		

	}

}
