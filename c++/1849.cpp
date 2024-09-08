#include <iostream>
using namespace std;

typedef long long ll;
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
#define MAX_N 100000

int seg_tree[4*MAX_N];
int ans[MAX_N] = {0};

void init(int s,int e,int x) {
    if (s == e) {
        seg_tree[x] = 1;
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    seg_tree[x] = seg_tree[2*x] + seg_tree[2*x+1];
}

int query(int s,int e,int x,int ord) {
    seg_tree[x]--;
    if (s == e) return s;
    int mid = (s+e) >> 1;
    if (seg_tree[2*x] >= ord) return query(s,mid,2*x,ord);
    else return query(mid+1,e,2*x+1,ord-seg_tree[2*x]);
}

int main() {
    FASTIO
    int n; cin >> n;
    init(1,n,1);
    for (int i = 1; i <= n; i++) {
        int ord; cin >> ord;
        int tmp = query(1,n,1,ord+1);
        ans[tmp] = i;
    }
    for (int i = 1; i <= n; i++) {
        cout << ans[i] << endl;
    }
}