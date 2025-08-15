import java.io.*;
import java.util.*;

public class Main {

	public static void bt(int cnt, int curr, int N, int M, int[] temp,StringBuilder sb) {
		if(cnt==M) {
			for(int t:temp) {sb.append(t).append(" ");} 
			sb.append("\n");
			return;
			}
		for(int i=curr;i<=N;i++) {
			temp[cnt] = i; 
			bt(cnt+1,i,N,M,temp,sb); 
		}
		
	}
	
	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine()); 
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken()); 
		int[] temp = new int[M]; 
		bt(0,1,N,M,temp,sb); 
		
		System.out.println(sb.toString());
		br.close();
	}

}
