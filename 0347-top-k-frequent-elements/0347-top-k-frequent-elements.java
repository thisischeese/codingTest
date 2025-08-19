class Solution {
        public class Node{
        int k,v;
        public Node(int k, int v){
            this.k = k;
            this.v = v;
        }

    }
    public int[] topKFrequent(int[] nums, int k) {	        int[] answer = new int[k];
	        List<Node> arr = new ArrayList<>(); 
	        HashMap<Integer,Integer> hashmap = new HashMap<>();
	
	        for(int n:nums){
	            if(!hashmap.containsKey(n)){
	                hashmap.put(n,1);
	            }
	            else{
	                int cnt = hashmap.get(n);
	                hashmap.replace(n,cnt+1);
	            }
	        }
	
	        hashmap.forEach((key,value)->{
	            arr.add(new Node(key,value));
	            //System.out.println(key+" "+value);
	        });
	
	        Collections.sort(arr, new Comparator<Node>() {
	            @Override
	            public int compare(Node n1, Node n2) {
	                // v값을 기준으로 내림차순 정렬
	                // n2가 더 크면 양수를 리턴하여 n2를 앞으로 보냄
	                return n2.v - n1.v;
	            }
	        });
	        //for(int i=0;i<arr.size();i++) {System.out.println(arr.get(i).k+" "+arr.get(i).v);}
	        for(int i=0;i<k;i++){
	            answer[i] = arr.get(i).k;
	        }
	        
	        
	        
	        return answer; 
    }
}