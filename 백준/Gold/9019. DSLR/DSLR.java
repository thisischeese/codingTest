import java.io.*; 
import java.util.*; 

public class Main {
	
	public static class Num{
		int val;
		String cmd;
		Num(int val, String cmd){
			this.val = val;
			this.cmd = cmd; 
		}
	}
	
	public static int D(int A) {
		return 2*A%10000;
	}
	
	public static int S(int A) {
		if(A==0) {return 9999;}
		else {return A-1;}
	}
	
	public static int L(int A) {
		int[] d = sepNum(A);
		return d[1]*1000+d[2]*100+d[3]*10+d[0];
	}
	
	public static int R(int A) {
		int[] d = sepNum(A);
		return d[3]*1000+d[0]*100+d[1]*10+d[2];
	}
	
	public static String BFS(int A,int B) {
		
		boolean[] v = new boolean[10001]; 
		v[A] = true; 
		
		Queue<Num> q = new ArrayDeque<>();
		q.offer(new Num(A,""));
		
		while(!q.isEmpty()) {
			Num curr = q.poll();
			if(curr.val == B) {return curr.cmd;}
			
			int dnum = D(curr.val);
			if(!v[dnum]) {v[dnum]= true;q.offer(new Num(dnum,curr.cmd+"D"));}
			
			int snum = S(curr.val);
			if(!v[snum]) {v[snum]= true;q.offer(new Num(snum,curr.cmd+"S"));}
			
			int lnum = L(curr.val);
			if(!v[lnum]) {v[lnum]= true;q.offer(new Num(lnum,curr.cmd+"L"));}
			
			int rnum = R(curr.val);
			if(!v[rnum]) {v[rnum]= true;q.offer(new Num(rnum,curr.cmd+"R"));}

		}
		
		return "";
	}
	
	public static int[] sepNum(int A) {
		
		
		int d1 = A/1000;
		int d2 = (A-d1*1000)/100;
		int d3 = (A-d1*1000-d2*100)/10;
		int d4 = (A-d1*1000-d2*100-d3*10);
		int[] answer = {d1,d2,d3,d4};
		
		return answer;
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder(); 
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine()); 
		
		for(int i=0;i<T;i++) {
			st = new StringTokenizer(br.readLine()); 
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			
			String answer = BFS(A,B); 
			
			sb.append(answer).append("\n");
		}

		br.close();
		System.out.println(sb.toString());
	}

}

