import java.io.*; 
import java.util.*; 

// DP 풀이 
// 1번부터 i번 직원까지 칭찬 받은 정도를 기록하는 DP 배열 
// 자신의 창찬 값 = 자신이 직속 상사에게 받은 칭찬 + 직속 상사가 연쇄적으로 받은 칭찬 
// dp[i] += dp[i-1]

public class Main {

	public static int n,m;
	public static int[] arr, dp; 
	public static StringBuilder sb = new StringBuilder(); 
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st = new StringTokenizer(br.readLine()); 
		
		n = Integer.parseInt(st.nextToken()); 
		m = Integer.parseInt(st.nextToken()); 
		arr = new int[n+1]; // 회사 직원별 직속 상사 번호 기록하는 배열  -> 0번은 취급 x 
		dp = new int[n+1]; 
		st = new StringTokenizer(br.readLine()); 
		for(int i=1;i<=n;i++) {
			arr[i] = Integer.parseInt(st.nextToken()); 
			if(i==1) {arr[i]+=1;}
		}
		
		for(int i=0;i<m;i++) {
			st = new StringTokenizer(br.readLine()); 
			int idx = Integer.parseInt(st.nextToken()); 
			int w = Integer.parseInt(st.nextToken()); 
			dp[idx] += w; 
		}
		/*
		for(int i=1;i<=n;i++) {
			sb.append(dp[i]).append(" ");}
		*/
		for(int i=1;i<=n;i++) {
			dp[i] += dp[arr[i]]; 
		}
		
		
		for(int i=1;i<=n;i++) {
			sb.append(dp[i]).append(" ");}
		
		br.close();
		System.out.println(sb.toString());
	}

}
