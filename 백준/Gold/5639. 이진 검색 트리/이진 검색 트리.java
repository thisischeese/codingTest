import java.io.*; 
import java.util.*; 

public class Main {
	
	public static int key,h,prevIdx; 
	public static int[] tree; 
	public static List<Integer> arr; 
	public static StringBuilder sb = new StringBuilder();
	
	// 후위 순회 : 왼 -> 오 -> 루트 
	public static void postOrder(int start,int end) {
		if(start>end) {return;}
		// 부분 트리의 루트 
		int root = arr.get(start);
		int rRoot = end+1; 
		// 현재 루트를 기준으로 오른쪽 서브트리 시작점을 찾기 : 현재 루트의 값보다 최초로 큰 값이 시작점
		for(int i=start;i<=end;i++) {
			if(arr.get(i)>root) {
				rRoot = i; break; 
			}
		}
		
		// 왼쪽 서브 트리 방문 
		postOrder(start+1, rRoot-1);
		// 오른쪽 서브 트리 방문 
		postOrder(rRoot, end);
		// 루트 노드 출력 
		sb.append(root).append("\n"); 
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st; 
		String line; 
		
		arr = new ArrayList<>();
		// 전위 순회 : 루트 -> 왼 -> 오 
		while((line = br.readLine())!=null && !line.isEmpty()) {
			key = Integer.parseInt(line); 
			arr.add(key); 
		}
		
		br.close();

		postOrder(0,arr.size()-1);// start end  
		System.out.println(sb.toString());
	}

}

// 전위 순회 결과 입력 -> 트리 구성 
// 트리 -> 후위 순회 결과 출력 

/*
50
30
24
5
28
45
98
52
60

5
28
24
45
30
60
52
98
50
 */
