import java.io.*; 
import java.util.*; 

/*
비행기 입력은 G로 주어지는데 1 ~ G에 모두 들어갈 수 있음을 의미함
=> 그렇다면 1에 가까운 게이트일수록 비행기가 들어가려고 하는 확률이 높을 것으로 G부터 거꾸로 탐색을 해야 한다. 
==> 원래대로라면 G에 들어간 경우, G-1에 들어간 경우, ... 1에 들어간 경우를 모두 재귀 완탐으로 구현이 가능하긴 할 것임 
===> 그러나 시간복잡도가 매우 높을 것임 : Union find를 사용해서 비어있는 노드를 찾는데에 소요되는 시간을 줄인다 
=====> 맨 끝부터 채우는 그리디한 선택을 할 것 
*/

public class Main {

	public static int G,P,answer; 
	public static int[] nodes; 
	public static StringBuilder sb = new StringBuilder(); 
	
	// 부모 노드 업데이트 
	// 자식 노드를 방문했는데 자식이 부모를 가지고 있다면 
	// 비행기를 넣기 위해 자기 자신의 부모를 방문함 
	// 그렇기에 현재 게이트에 비행기가 이미 들어왔다면 
	// 바로 자기 앞의 노드를 확인하고 자기 앞 노드의 부모를 자기 노드로 가져야 함 
	// a<b인 상황만 가정하고 구현 
	public static void union(int a, int b) {
		int pa = find(a); 
		int pb = find(b);
		if(pa!=pb) {nodes[pb] = pa; }
	}
	
	// 부모 노드 찾기 
	public static int find(int idx) {
		// 자기자신 부모 노드가 
		if(nodes[idx]==idx) {return idx;}
		
		// 경로 압축 
		return nodes[idx] = find(nodes[idx]);
	}
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		G = Integer.parseInt(br.readLine()); // gates cnt
		P = Integer.parseInt(br.readLine()); //planes cnt
		answer = 0; 
		nodes = new int[G+1];
		for(int i=1;i<=G;i++) {
			nodes[i] = i; // 모든 노드 자기 자신이 부모 노드이도록 설정ㅎ기 
		}
		/*
		System.out.println(answer);
		for(int j=0;j<=G;j++) {
			System.out.print(nodes[j]+" ");
		}
		*/
		//System.out.println();
		for(int i=1;i<=P;i++) {
			int g = Integer.parseInt(br.readLine()); 
			// 들어오는 즉시 도킹할 게이트 찾기 find
			int pg = find(g); // O(1) 
			// 게이트 찾지 못했다면 break -> 부모 노드를 찾았는데 부모 노드가 0으로 나온다? 그러면 nreak 
			if(pg==0) {break;}
			// 게이트 찾았다면 부모 노드를 업데이트해 방문하지 않도록 처리하기 union
			
			union(pg-1,pg); // O()
			
			answer++; 
			/*
			System.out.println(answer);
			for(int j=0;j<=G;j++) {
				System.out.print(nodes[j]+" ");
			}
			System.out.println();
			*/
		}
		
		sb.append(answer); 
		br.close();
		System.out.println(sb.toString());
		
	}

}


