import java.io.*; 
import java.util.*; 

public class Main {

	public static void bt(int cnt, int curr, int N, int M, int[] temp, List<int[]>seq) {
		if(cnt==M) {seq.add(temp.clone());return;}
		for(int i=curr+1;i<=N;i++) {
			temp[cnt] = i;
			bt(cnt+1,i,N,M,temp,seq);
		}
	}
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine()); 

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken()); 
		List<int[]> seq = new ArrayList<>();
		int[] temp = new int[M]; 
		
		bt(0,0,N,M,temp,seq);
		for(int i=0;i<seq.size();i++) {
			for(int j =0;j<M;j++) {
				System.out.print(seq.get(i)[j]+" ");
			}
			System.out.println();
		}
		
		br.close();
		
	}

}
