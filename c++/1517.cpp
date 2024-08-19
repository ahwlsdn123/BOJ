#include <iostream>
#include <vector>
#include <algorithm>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

using namespace std;

ll seg_tree[2000001] = {0};

void update(int s, int e, int x, int t) {
    if (t < s || e < t) return;
    if (s == e) {seg_tree[x]++; return;}
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t);
    update(mid+1,e,2*x+1,t);
    seg_tree[x] = seg_tree[2*x] + seg_tree[2*x+1];
}

ll findSum(int s, int e, int x, int l, int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    return findSum(s,mid,2*x,l,r) + findSum(mid+1,e,2*x+1,l,r);
}

int main() {
    FASTIO
    int n;
    cin >> n;
    vector<pair<ll,int>> vec;
    vec.push_back({0,0});
    for (int i = 1; i <= n; i++) {
        ll tmp;
        cin >> tmp;
        vec.push_back({tmp,i});
    }
    sort(vec.begin(),vec.end());
    int index[n+1];
    for (int i = 1; i <= n; i++) {
        index[vec[i].second] = i;
    }

    ll answer = 0;
    for (int i = 1; i <= n; i++) {
        int ind = index[i];
        update(1,n,1,ind);
        if (ind < n)
            answer += findSum(1,n,1,ind+1,n);
    }
    cout << answer << endl;
    return 0;
}