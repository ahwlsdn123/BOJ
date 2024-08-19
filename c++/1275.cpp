#include <iostream>
#include <vector>
#include <algorithm>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

using namespace std;

int arr[100001];
ll seg_tree[400004];

void init(int s, int e, int x) {
    if (s == e) {seg_tree[x] = arr[s]; return;}
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1];
}

void update(int s, int e, int x, int t, int v) {
    if (t < s || e < t) return;
    if (s == e) {seg_tree[x] = v; return;}
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t,v);
    update(mid+1,e,2*x+1,t,v);
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

    int n,q;
    cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    init(1,n,1);
    for (int i = 0; i < q; i++) {
        int l,r,t,v;
        cin >> l >> r >> t >> v;
        if (l > r) {
            int tmp = l;
            l = r;
            r = tmp;
        }
        cout << findSum(1,n,1,l,r) << endl;
        update(1,n,1,t,v);
    }
    return 0;
}