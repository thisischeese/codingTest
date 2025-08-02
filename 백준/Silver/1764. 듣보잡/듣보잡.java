import java.io.*; 
import java.util.*; 

public class Main {
	
	public static void main (String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder(); 

		int N = Integer.parseInt(st.nextToken()); 
		int M = Integer.parseInt(st.nextToken()); 
		LinkedHashSet<String> hs1 = new LinkedHashSet(); 
		LinkedHashSet<String> hs2 = new LinkedHashSet(); 
 
		for(int i=0;i<N;i++) {
			hs1.add(br.readLine());
		}
		for(int i=0;i<M;i++) {
			hs2.add(br.readLine()); 
		}
		hs1.retainAll(hs2);
		List<String> temp = new ArrayList<>(hs1); 
		Collections.sort(temp);
		sb.append(temp.size()+"\n"); // 사이즈 
		for(String s: temp) {
			sb.append(s+"\n");	
		}	
		System.out.println(sb.toString());
		br.close();
	}

}
