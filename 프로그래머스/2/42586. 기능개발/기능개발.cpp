#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> periods;
    
    // 각 작업의 완료까지 필요한 일수 계산
    for(int i = 0; i < progresses.size(); i++) {
        int remain = 100 - progresses[i];
        int days = (remain + speeds[i] - 1) / speeds[i];  // 올림 처리
        periods.push_back(days);
    }

    // 배포 단위 계산
    int curr_deploy_day = periods[0];
    int count = 1;

    for (int i = 1; i < periods.size(); i++) {
        if (periods[i] <= curr_deploy_day) {
            // 이전 배포일에 같이 배포 가능
            count++;
        } else {
            // 새 배포 시작
            answer.push_back(count);
            curr_deploy_day = periods[i];
            count = 1;
        }
    }

    // 마지막 배포 처리
    answer.push_back(count);

    return answer;
}
