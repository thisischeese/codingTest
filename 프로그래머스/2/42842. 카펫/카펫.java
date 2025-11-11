class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        // 가로>= 세로 
        // 2*w + 2*(h-2) = brown 
        // w+h = brown/2 +2  
        // (h-2)*(w-2) = yellow 
        // w* h = brown + yellow 
        for(int w=brown/2+2;w>=brown/4+1;w--){
            if(w*(brown/2+2-w)==(brown+yellow)){
                answer[0] = w; 
                answer[1] = brown/2+2-w;
                break;
            }
        }
        return answer;
    }
}