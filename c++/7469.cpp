#include <iostream>
#include <vector>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

using namespace std;

int n,m;
vector<int> arr;
vector<int> seg_tree[4*100000];

void init(int s, int e, int x) {
    if (s == e) {
        seg_tree[x].push_back(arr[s]);
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    int i = 0, j = 0;
    while (i < seg_tree[2*x].size() && j < seg_tree[2*x+1].size()) {
        if (seg_tree[2*x][i] < seg_tree[2*x+1][j]) {
            seg_tree[x].push_back(seg_tree[2*x][i++]);
        } else {
            seg_tree[x].push_back(seg_tree[2*x+1][j++]);
        }
    }
    if (i == seg_tree[2*x].size()) {
        while (j < seg_tree[2*x+1].size()) {
            seg_tree[x].push_back(seg_tree[2*x+1][j++]);
        }
    }
    if (j == seg_tree[2*x+1].size()) {
        while ( i < seg_tree[2*x].size()) {
            seg_tree[x].push_back(seg_tree[2*x][i++]);
        }
    }
}

int query(int s, int e, int x, int l, int r, int v) {
    if (e < l || r < s) return 0;
    if (l <= s && e <= r) {
        int cnt = lower_bound(seg_tree[x].begin(),seg_tree[x].end(),v) - seg_tree[x].begin();
        return cnt;
    }
    int mid = (s+e) >> 1;
    return query(s,mid,2*x,l,r,v) + query(mid+1,e,2*x+1,l,r,v);
}

int main() {
    FASTIO
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        int tmp; cin >> tmp;
        arr.push_back(tmp);
    }
    init(0,n-1,1);
    for (int i = 0; i < m; i++) {
        int a,b,c; cin >> a >> b >> c;
        int l = -1e9;
        int r = 1e9;
        int mid;
        int ans = -1e9;
        while (l <= r)
        {
            mid = (l+r) >> 1;
            int q = query(1,n,1,a,b,mid);
            if (q < c) {
                ans = mid;
                l = mid+1;
            } else {
                r = mid-1;
            }
        }
        cout << ans << endl;
    }
    return 0;
}