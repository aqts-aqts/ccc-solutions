#include <iostream>
using namespace std;

int main() {
    int people;
    cin >> people;

    int bids[people];
    string names[people];
    for (int i = 0; i < people; i++) {
        cin >> names[i];
        cin >> bids[i];
    }

    int highestBid = bids[0];
    string highestBidName = names[0];
    for (int i = 0; i < sizeof(bids) / sizeof(bids[0]); i++) {
        if (bids[i] > highestBid) {
            highestBid = bids[i];
            highestBidName = names[i];
        }
    }

    cout << highestBidName;
}