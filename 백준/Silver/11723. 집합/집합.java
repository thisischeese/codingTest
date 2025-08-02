import java.io.*; 
import java.util.*; 

public class Main {
	static StringBuilder sb = new StringBuilder(); 

	public static void operation(HashSet<Integer> set,String oper,int target) {
		switch(oper) {
			case "add": 
				set.add(target);
				break; 
			case "check" : 
				if(set.contains(target)) {sb.append(1+"\n");}
				else {sb.append(0+"\n");}
				break; 
			case "remove" : 
				set.remove(target); 
				break; 
			case "toggle" : 
				if(set.contains(target)) {set.remove(target);}
				else {set.add(target); }
				break; 
		
		}
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		HashSet<Integer> set = new HashSet<>(); 
		
		int M = Integer.parseInt(br.readLine()); 
		for(int i=0;i<M;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine()); 
			String oper = st.nextToken(); 
			if(oper.equals("all")){
				for(int j=1;j<21;j++) {
					set.add(j);}
			}
			else if(oper.equals("empty")) {	
				set.clear();
			}
			else {
				int target = Integer.parseInt(st.nextToken()); 
				operation(set,oper,target);
			}
		}
		System.out.println(sb);
		br.close();
	}

}
