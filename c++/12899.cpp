#include <iostream>
using namespace std;

typedef long long ll;
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
#define MAX_VAL 2000000

int n;
int seg_tree[4*MAX_VAL] = {0};

void update(int s,int e,int x,int t) {
    if (e < t || t < s) return;
    if (s == e) {
        seg_tree[x]++;
        return;
    }
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t);
    update(mid+1,e,2*x+1,t);
    seg_tree[x] = seg_tree[2*x] + seg_tree[2*x+1];
}

int query(int s,int e,int x,int ord) {
    if (s == e) {
        seg_tree[x]--;
        return s;
    }
    int mid = (s+e) >> 1;
    int _ret;
    if (seg_tree[2*x] >= ord) {
        _ret = query(s,mid,2*x,ord);
    } else {
        _ret = query(mid+1,e,2*x+1,ord-seg_tree[2*x]);
    }
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1];
    return _ret;
}

int main() {
    FASTIO
    cin >> n;
    for (int i = 0; i < n; i++) {
        int t,x; cin >> t >> x;
        if (t == 1) {
            update(1,MAX_VAL,1,x);
        } else {
            cout << query(1,MAX_VAL,1,x) << endl;
        }
    }
    return 0;
}