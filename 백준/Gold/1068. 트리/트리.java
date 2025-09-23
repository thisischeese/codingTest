import java.io.*; 
import java.util.*; 


public class Main {

	public static int N,p,target,cnt,answer,root; 
	public static Set<Integer>[] tree; 
	public static StringBuilder sb = new StringBuilder(); 

	public static void cntChildren(int curr) {
		if(tree[curr].size()==0) {cnt++; return;}
		for(int c : tree[curr]) {
			cntChildren(c);
		}
	}
	// 루트부터 타고 내려가다가 
	// target과 같은 노드를 자식으로 만나면 지우고 return 
	public static void remove(int curr) {
		if(tree[curr].contains(target)) {tree[curr].remove(target); return;}
		
		for(int c : tree[curr]) {
			remove(c);
		}
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st; 
		
		N = Integer.parseInt(br.readLine()); 

		tree = new HashSet[N];
		for(int i=0;i<N;i++) {tree[i] = new HashSet<Integer>(); }
	
		st = new StringTokenizer(br.readLine()); 
		for(int i=0;i<N;i++) {
			p = Integer.parseInt(st.nextToken()); 
			if(p==-1) {root = i; continue;}
			tree[p].add(i); 
		}
		target = Integer.parseInt(br.readLine());
		br.close();
		
		// target의 자식부터 타고 가면서 지우기 

		// root== target -> 
		if(root==target) {answer=0;}
		else {
			if(target!=N) {
				// 자식 지우기 
				remove(root); 
			}
			cnt = 0; 
			cntChildren(root); 
			answer = cnt; 
		}

		
		sb.append(answer); 

		System.out.println(sb.toString());
	}

}


// 전체 자식 개수 구하기 
// target이 가지는 자식 개수 구하기 
// 전체 자식 개수 - target 자식 개수 