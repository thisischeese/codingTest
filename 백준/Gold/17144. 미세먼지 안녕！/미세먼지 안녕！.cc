#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
using namespace std;

int r, c, t;
int arr[50][50];
int temp[50][50];
int air_x1 = -1, air_x2 = -1;

int dx[4] = {-1, 1, 0, 0}; 
int dy[4] = {0, 0, -1, 1};

void spread() {
    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            temp[i][j] = 0;

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (arr[i][j] > 0) {
                int amount = arr[i][j] / 5;
                int cnt = 0;
                for (int d = 0; d < 4; ++d) {
                    int ni = i + dx[d], nj = j + dy[d];
                    if (ni >= 0 && ni < r && nj >= 0 && nj < c && arr[ni][nj] != -1) {
                        temp[ni][nj] += amount;
                        cnt++;
                    }
                }
                temp[i][j] += arr[i][j] - amount * cnt;
            }
        }
    }

    temp[air_x1][0] = temp[air_x2][0] = -1;

    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            arr[i][j] = temp[i][j];
}

void operate_air() {
    for (int i = air_x1 - 1; i > 0; --i)
        arr[i][0] = arr[i - 1][0];
    for (int j = 0; j < c - 1; ++j)
        arr[0][j] = arr[0][j + 1];
    for (int i = 0; i < air_x1; ++i)
        arr[i][c - 1] = arr[i + 1][c - 1];
    for (int j = c - 1; j > 1; --j)
        arr[air_x1][j] = arr[air_x1][j - 1];
    arr[air_x1][1] = 0;

    for (int i = air_x2 + 1; i < r - 1; ++i)
        arr[i][0] = arr[i + 1][0];
    for (int j = 0; j < c - 1; ++j)
        arr[r - 1][j] = arr[r - 1][j + 1];
    for (int i = r - 1; i > air_x2; --i)
        arr[i][c - 1] = arr[i - 1][c - 1];
    for (int j = c - 1; j > 1; --j)
        arr[air_x2][j] = arr[air_x2][j - 1];
    arr[air_x2][1] = 0;
}

int main() {
    cin >> r >> c >> t;

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == -1) {
                if (air_x1 == -1)
                    air_x1 = i;
                else
                    air_x2 = i;
            }
        }
    }

    while (t--) {
        spread();
        operate_air();
    }

    int result = 0;
    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            if (arr[i][j] > 0)
                result += arr[i][j];

    cout << result << endl;
    return 0;
}
