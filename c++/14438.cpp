#include <iostream>
#include <algorithm>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
#define INF 1000000001
typedef long long ll;

using namespace std;

int n,m;
int arr[100001];
int seg_tree[400004];

int min(int a, int b) {
    if (a < b) return a;
    else return b;
}

void init(int s, int e, int x) {
    if (s == e) {
        seg_tree[x] = arr[s];
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    seg_tree[x] = min(seg_tree[2*x],seg_tree[2*x+1]);
}

void update(int s, int e, int x, int t, int v) {
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

int findMin(int s, int e, int x, int l, int r) {
    if (r < s || e < l) return INF;
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    return min(findMin(s,mid,2*x,l,r),findMin(mid+1,e,2*x+1,l,r));
}

int main() {
    FASTIO
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    init(1,n,1);
    cin >> m;
    for (int i = 0; i < m; i++) {
        int a,b,c;
        cin >> a >> b >> c;
        if (a == 1) {
            update(1,n,1,b,c);
        } else {
            cout << findMin(1,n,1,b,c) << endl;
        }
    }
    return 0;
}