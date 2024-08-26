#include <iostream>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

using namespace std;

int n,q;
ll seg_tree[4000000] = {0};

void update(int s,int e,int x,int t,int v) {
    if (e < t || t < s) return;
    if (s == e) {
        seg_tree[x] += v;
        return;
    }
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t,v);
    update(mid+1,e,2*x+1,t,v);
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1];
}

ll findSum(int s,int e,int x,int l,int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    return findSum(s,mid,2*x,l,r)+findSum(mid+1,e,2*x+1,l,r);
}

int main() {
    FASTIO

    cin >> n >> q;
    for (int i = 0; i < q; i++) {
        int a,b,c;
        cin >> a >> b >> c;
        if (a == 1) {
            update(1,n,1,b,c);
        } else {
            cout << findSum(1,n,1,b,c) << endl;
        }
    }
}