#include <iostream>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
#define MAX 1000000001
typedef long long ll;

using namespace std;

ll arr[100001];
ll seg_tree[400004];

ll min(ll a, ll b) { if (a < b) return a; else return b; }

void init(int s, int e, int x) {
    if (s == e) {
        seg_tree[x] = arr[s];
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    seg_tree[x] = min(seg_tree[2*x], seg_tree[2*x+1]);
}

ll findMin(int s, int e, int x, int l, int r) {
    if (e < l or r < s) {
        return MAX;
    }
    if (l <= s && e <= r) {
        return seg_tree[x];
    }
    int mid = (s+e) >> 1;
    return min(findMin(s,mid,2*x,l,r),findMin(mid+1,e,2*x+1,l,r));
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);

    int n,m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    init(1,n,1);
    for (int i = 0; i < m; i++) {
        int l,r;
        cin >> l >> r;
        cout << findMin(1,n,1,l,r) << endl;
    }
    return 0;
}