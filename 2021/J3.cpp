#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main() {
    bool direction;
    int step;
    int iterations = 0;
    vector<string> output;
    vector<int> outputNum;

    cin >> step;
    while (step != 99999) {
        int dir1 = floor(step / 10000);
        int dir2 = floor(step / 1000) - dir1 * 10;
        int dir = dir1 + dir2;

        if (dir % 2 == 0 && dir != 0) {
            direction = true;
        } else if (dir % 2 == 1) {
            direction = false;
        }

        if (direction) {
            output.push_back("right ");
            outputNum.push_back(step - floor(step / 1000) * 1000);
        } else {
            output.push_back("left ");
            outputNum.push_back(step - floor(step / 1000) * 1000);
        }

        cin >> step;
        iterations++;
    }

    for (int i = 0; i < iterations; i++) {
        cout << output[i];
        cout << outputNum[i] << endl;
    }
}