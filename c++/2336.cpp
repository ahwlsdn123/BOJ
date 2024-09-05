#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

int n;
vector<pair<int,pair<int,int>>> ranks;
vector<int> seg_tree;

bool comp(pair<int,pair<int,int>> p1, pair<int,pair<int,int>> p2) {
    return p1.first < p2.first;
}

int min(int a,int b) {
    return (a < b) ? a : b;
}

void update(int s,int e,int x,int t,int v) {
    if (e < t || t < s) return;
    if (s == e) {
        seg_tree[x] = v;
        return;
    }
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t,v);
    update(mid+1,e,2*x+1,t,v);
    seg_tree[x] = min(seg_tree[2*x],seg_tree[2*x+1]);
}

int search(int s,int e,int x,int l,int r) {
    if (r < s || e < l) return n+1;
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    return min(search(s,mid,2*x,l,r),search(mid+1,e,2*x+1,l,r));
}

int main() {
    FASTIO
    cin >> n;
    ranks.assign(n+1,{0,{0,0}});
    for (int i = 1; i <= n; i++) {
        int tmp; cin >> tmp;
        ranks[tmp].first = i;
    }
    for (int i = 1; i <= n; i++) {
        int tmp; cin >> tmp;
        ranks[tmp].second.first = i;
    }
    for (int i = 1; i <= n; i++) {
        int tmp; cin >> tmp;
        ranks[tmp].second.second = i;
    }
    sort(ranks.begin(),ranks.end(),comp);
    seg_tree.assign(4*n,n+1);
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        update(1,n,1,ranks[i].second.first,ranks[i].second.second);
        if (ranks[i].second.first == 1 || search(1,n,1,1,ranks[i].second.first-1) > ranks[i].second.second) {
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}