import java.io.*; 
import java.util.*; 


public class Main {

	private static int N,r,c;
	private static StringBuilder sb = new StringBuilder(); 
	
	
	private static void findV(int sr, int sc,int er, int ec, int cnt) {
		if(er-sr==1) {
			cnt += (r-sr)*2 + (c-sc);
			sb.append(cnt).append("\n");
			return;}
		int dist = (1+er-sr)/2; 
		int[] nr = {sr,sr,sr+dist,sr+dist};
		int[] nc = {sc,sc+dist,sc,sc+dist}; 
		
		
		for(int i=0;i<4;i++) {
			if(nr[i]<=r && r<=nr[i]+dist-1 && nc[i]<=c && c<=nc[i]+dist-1) {
				findV(nr[i], nc[i],nr[i]+dist-1,nc[i]+dist-1,cnt);}
			cnt += dist*dist;

				
			
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c =  Integer.parseInt(st.nextToken());
		
		findV(0,0,(int)Math.pow(2, N)-1,(int)Math.pow(2, N)-1,0);
	
		br.close();
		System.out.println(sb.toString());
	}

}
