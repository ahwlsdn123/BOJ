#include <iostream>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

using namespace std;
int n,m;
ll seg_tree[4000001] = {0};

ll sum(int s, int e, int x, int l, int r) {
    if (e < l || r < s) return 0;
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    return sum(s,mid,2*x,l,r) + sum(mid+1,e,2*x+1,l,r);
}

void modify(int s, int e, int x, int t, int v) {
    if (e < t || t < s) return;
    if (s == e) {seg_tree[x] = v; return;}
    int mid = (s+e) >> 1;
    modify(s,mid,2*x,t,v);
    modify(mid+1,e,2*x+1,t,v);
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1];
}

int main() {
    FASTIO
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a,b,c;
        cin >> a >> b >> c;
        if (a==0) {
            if (b > c) {
                int tmp = b;
                b = c;
                c = tmp;
            }
            cout << sum(1,n,1,b,c) << endl;
        } else {
            modify(1,n,1,b,c);
        }
    }
    return 0;
}