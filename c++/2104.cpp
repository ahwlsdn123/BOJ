#include <iostream>
#include <vector>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;
#define INF 1000001

using namespace std;

int n;
int arr[100001] = {0};
vector<pair<ll,int>> seg_tree;

void init(int s,int e,int x) {
    if (s == e) {
        seg_tree[x] = {arr[s],s};
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    seg_tree[x].first = seg_tree[2*x].first + seg_tree[2*x+1].first;
    seg_tree[x].second = (arr[seg_tree[2*x].second] < arr[seg_tree[2*x+1].second]) ? seg_tree[2*x].second : seg_tree[2*x+1].second;
}

pair<ll,int> findPair(int s,int e,int x,int l,int r) {
    if (r < s || e < l) return {0,0};
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    pair<ll,int> p1 = findPair(s,mid,2*x,l,r);
    pair<ll,int> p2 = findPair(mid+1,e,2*x+1,l,r);
    return {p1.first+p2.first, (arr[p1.second] < arr[p2.second]) ? p1.second : p2.second};
}

ll max3(ll a,ll b,ll c) {
    ll tmp = (a > b) ? a : b;
    return (tmp > c) ? tmp : c;
}

ll dnc(int l,int r) {
    pair<ll,int> p = findPair(1,n,1,l,r);
    ll v1 = p.first * arr[p.second];
    ll v2 = (l <= p.second-1) ? dnc(l,p.second-1) : 0;
    ll v3 = (p.second+1 <= r) ? dnc(p.second+1,r) : 0;
    return max3(v1,v2,v3);
}

int main() {
    FASTIO
    
    cin >> n;
    arr[0] = INF;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    seg_tree.assign(4*n,{0,0});
    init(1,n,1);
    cout << dnc(1,n) << endl;
    return 0;
}