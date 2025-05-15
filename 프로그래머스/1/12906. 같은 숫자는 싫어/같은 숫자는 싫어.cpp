#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    int prev = arr[0];
    vector<int> answer = {prev};
    
    for(int i=1;i<arr.size();i++){
        int curr = arr[i];
        if (prev != curr){
            answer.push_back(curr);
        }
        prev = curr;
    }
    

    return answer;
}