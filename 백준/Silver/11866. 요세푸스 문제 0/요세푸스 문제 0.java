import java.io.*; 
import java.util.*; 

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringBuilder sb = new StringBuilder(); 
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		List<Integer> arr = new ArrayList<>();
		int cnt = 1;
		
		Queue<Integer> queue = new ArrayDeque<>(); 
		for(int i=1;i<=N;i++) {queue.add(i);}

		while(!queue.isEmpty()) {
			if(cnt==K) {arr.add(queue.poll()); cnt = 1;continue;}
			cnt++; 
			int temp = queue.poll();
			queue.add(temp);
		}
		sb.append("<");
		for(int i=0;i<N-1;i++) {sb.append(arr.get(i)).append(", ");}
		sb.append(arr.get(N-1)).append(">");
		br.close();
		System.out.println(sb.toString());
	}

}
