import java.io.*; 
import java.util.*; 

public class Main {

	public static void track(int curr, int cnt,int N, int M, boolean[] v, List<int[]> seq, int[] temp) {
		if(cnt==M) {seq.add(temp.clone());return;}
		//System.out.println("curr : "+curr+""+Arrays.toString(temp));

		for(int i=1;i<=N;i++) {
			if(v[i]) {continue;}
			temp[cnt] = i; 
			v[i] = true; 
			track(i,cnt+1,N,M,v,seq,temp); 
			v[i] = false; 
		}
		
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		//StringBuilder sb = new StringBuilder(); 
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		List<int[]> seq = new ArrayList<>();
		boolean[]v = new boolean[N+1]; v[0] = true; // 0부터 N까지 visited 체크 
		int[] temp = new int[M];
		
		track(0,0,N,M,v,seq, temp); 
		
		for(int i =0;i<seq.size();i++) {
			for(int j =0;j<M;j++) {
				System.out.print(seq.get(i)[j]+" ");
			}
			System.out.println();
		}
		
		br.close();
	}

}
