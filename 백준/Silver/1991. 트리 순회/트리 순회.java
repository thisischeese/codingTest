import java.io.*; 
import java.util.*; 

public class Main {

	public static int N,h; 
	public static Node[] tree; 
	public static StringBuilder sb = new StringBuilder(); 
	
	public static class Node{
		int idx; 
		int lc;
		int rc; 
		Node(int idx,int lc, int rc){
			this.idx = idx; 
			this.lc = lc; 
			this.rc = rc; 
		}
	}
	// 전위 순회 : 루트 -> 왼쪽 -> 오른쪽 
	public static void pre(Node curr) {
		
		// 루트 노드 추가 
		sb.append((char)(curr.idx+65)); 
		// 방문 처리된 노드라면 sb에 append 후 리턴 
		if(curr.lc!=-1) {pre(tree[curr.lc]);}
		if(curr.rc!=-1){pre(tree[curr.rc]); }

		return; 
	}
	// 중위 순회 : 왼쪽 -> 루트 -> 오른쪽 
	public static void in(Node curr) {
		
		if(curr.lc!=-1) {in(tree[curr.lc]);}
		sb.append((char)(curr.idx+65)); 
		if(curr.rc!=-1) {in(tree[curr.rc]);} 
	}
	
	public static void post(Node curr) {

		if(curr.lc!=-1) {post(tree[curr.lc]);}
		if(curr.rc!=-1) {post(tree[curr.rc]);} 
		sb.append((char)(curr.idx+65)); 

		return; 
	}
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st; 
		N = Integer.parseInt(br.readLine()); 
		
		// 0 인덱스는 A 노드 
		tree = new Node[26]; 
		
		// 트리 만들기 
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine()); 
			int p = st.nextToken().charAt(0)-'A';
			int lc = st.nextToken().charAt(0)-'A';
			int rc = st.nextToken().charAt(0)-'A';
			//System.out.println("p:"+p);
			//System.out.println("lc:"+lc);
			//System.out.println("rc:"+rc);
			tree[p] = new Node(p,lc==-19?-1:lc,rc==-19?-1:rc);
			
		}
		
		// 전위 순회  
		pre(tree[0]); sb.append("\n");
		// 중위 순회 
		in(tree[0]); sb.append("\n");
		// 후위 순회 
		post(tree[0]); sb.append("\n");
		
		br.close();
		System.out.println(sb.toString());
		
	}

}
