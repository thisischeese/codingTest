import java.io.*; 
import java.util.*; 

public class Main {
	
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int [] arr= new int[N];
		for(int i=0;i<N;i++) {arr[i] = Integer.parseInt(st.nextToken());}

		int [] left = new int[N];
		int [] right = new int[N];
		int[] num = new int[N];
		Stack<Integer> stack = new Stack<>();
		
		// 왼쪽 
		for(int i=0;i<N;i++) {
			// 더 작은 것이 없을 때까지 뽑는다 
			while(!stack.isEmpty() && arr[stack.peek()]<=arr[i]) {stack.pop();}
	
			left[i] = stack.size();
			if(!stack.isEmpty()) {num[i] = stack.peek()+1;}
			stack.add(i);
		}
		
		stack.clear();;
		// 오른쪽 
		for(int i=N-1;i>=0;i--) {
			// 더 작은 것이 없을 때까지 뽑는다 
			while(!stack.isEmpty() && arr[stack.peek()]<=arr[i]) {stack.pop();}

			right[i] = stack.size();
			if(!stack.isEmpty()) {
				if(num[i]==0) {num[i] = stack.peek()+1;}
				else if(stack.peek()-i<i-num[i]+1) {num[i]= stack.peek()+1;}
			}
			stack.add(i);		
			}
		
		for(int i=0;i<N;i++) {
			sb.append(left[i]+right[i]).append(" ");
			if(num[i]!=0) {sb.append(num[i]).append("\n");}
			else {sb.append("\n");}
		}
		
		br.close();
		System.out.println(sb.toString());
	}

}
