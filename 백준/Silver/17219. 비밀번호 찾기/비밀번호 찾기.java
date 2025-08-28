import java.io.*; 
import java.util.*; 

public class Main {

	public static int N,M; 
	public static Map<String,String> hashMap;
	public static StringBuilder sb = new StringBuilder(); 
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st; 
		
		st = new StringTokenizer(br.readLine()); 
		N = Integer.parseInt(st.nextToken()); 
		M = Integer.parseInt(st.nextToken()); 
		hashMap = new HashMap<>(); 
		
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine()); 
			hashMap.put(st.nextToken(),st.nextToken()); // 사이트 : 비밀번호 
		}
		for(int i=0;i<M;i++) {
			String k = br.readLine();
			sb.append(hashMap.get(k)).append("\n");
		}
		
		br.close();
		System.out.println(sb.toString());
	}

}
