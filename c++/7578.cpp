#include <iostream>
#include <vector>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

using namespace std;

int location[500001] = {0};
vector<pair<int,int>> machines;
ll seg_tree[2000001] = {0};

void update(int s, int e, int x, int t) {
    if (e < t || t < s) return;
    if (s == e) {
        seg_tree[x]++;
        return;
    }
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t);
    update(mid+1,e,2*x+1,t);
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1];
}

ll findSum(int s, int e, int x, int l, int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    return findSum(s,mid,2*x,l,r)+findSum(mid+1,e,2*x+1,l,r);
}

int main() {
    FASTIO
    machines.assign(1000001,{0,0});

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int num;
        cin >> num;
        machines[num].first = i;
    }
    for (int i = 1; i <= n; i++) {
        int num;
        cin >> num;
        machines[num].second = i;
    }

    for (int i = 0; i <= 1000000; i++) {
        if (machines[i].first != 0) {
            location[machines[i].first] = machines[i].second;
        }
    }

    ll answer = 0;
    for (int i = 1; i <= n; i++) {
        int ind = location[i];
        update(1,n,1,ind);
        if (ind < n)
            answer += findSum(1,n,1,ind+1,n);
    }
    cout << answer << endl;
    return 0;
}