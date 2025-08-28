import java.io.*; 
import java.util.*; 

public class Main {

	public static int N; 
	public static int[][] arr; 
	public static StringBuilder sb = new StringBuilder();
	
	// Z 방향으로 진행 
	// 사각형 검사 -> 만약 모두 0 or 1이다 || 만약 사각형 크기가 1이다 -> ㅊsb append 
	// 	        -> 아니다 -> 분할정복 진행(재귀를 타고 들어가는 순간 위의 조건에 해당하지 않는다면 여는 괄호를 입력-> depth가 같으면 추가하지 x / 같은 depth에서 탐색 마치고 빠져나올 때 닫는 괄호 추가) 
	// 
	// 
	public static int check(int r,int c, int length) {
		int flag = arr[r][c]; 
		for(int i=r;i<r+length;i++) {
			for(int j=c;j<c+length;j++) {
				if(flag!=arr[i][j]) {return -1;}
			}
		}
		return flag; 
	}
	
	public static void dc(int r,int c, int length) {
		int flag = check(r,c,length);
		if(flag==-1) {
			// 분할정복 진행 
			sb.append("(");
			dc(r,c,length/2); // 좌상
			dc(r,c+length/2,length/2); // 우상
			dc(r+length/2,c,length/2); // 좌하
			dc(r+length/2,c+length/2,length/2);// 우하 
			sb.append(")"); 
		}
		else {
			sb.append(flag); 
		}
		
	}
	
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		
		N = Integer.parseInt(br.readLine()); 
		arr = new int[N][N]; 
		
		for(int i=0;i<N;i++) {
			String s = br.readLine(); 
			for(int j=0;j<N;j++) {
				arr[i][j] = s.charAt(j)-'0'; 
			}
		}
		

		dc(0, 0, N);
		br.close();
		System.out.println(sb.toString());
	}

}
