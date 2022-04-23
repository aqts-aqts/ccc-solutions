#include <iostream>
using namespace std;

int main() {
    int temp;
    cin >> temp;
    
    int pressure = 5 * temp - 400;
    cout << pressure << endl;
    if (temp > 100) {
        cout << "-1";
    } else if (temp == 100) {
        cout << "0";
    } else {
        cout << "1";
    }
}