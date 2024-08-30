#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

int n;
vector<int> arr;

pair<vector<int>,ll> init(int s, int e, int x) {
    if (s == e) {
        return {{arr[s]},0};
    }
    int mid = (s+e) >> 1;
    pair<vector<int>,ll> p1 = init(s,mid,2*x);
    pair<vector<int>,ll> p2 = init(mid+1,e,2*x+1);
    pair<vector<int>,ll> p = {vector<int>(),p1.second+p2.second};
    int i = 0, j = 0;
    while (i < p1.first.size() && j < p2.first.size()) {
        if (p1.first[i] <= p2.first[j]) {
            p.first.push_back(p1.first[i++]);
        } else {
            p.first.push_back(p2.first[j++]);
            p.second += p1.first.size() - i;
        }
    }
    if (i == p1.first.size()) {
        while (j < p2.first.size()) {
            p.first.push_back(p2.first[j++]);
        }
    }
    if (j == p2.first.size()) {
        while (i < p1.first.size()) {
            p.first.push_back(p1.first[i++]);
        }
    }
    return p;
}

int main() {
    FASTIO
    cin >> n;
    for (int i = 0; i < n; i++) {
        int tmp; cin >> tmp; arr.push_back(tmp);
    }
    cout << init(0,n-1,1).second << endl;

    return 0;
}