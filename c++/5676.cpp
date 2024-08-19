#include <iostream>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

using namespace std;

int arr[100001] = {0};
int seg_tree[400004] = {0};

void init(int s,int e,int x) {
    if (s == e) {
        seg_tree[x] = arr[s];
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    seg_tree[x] = seg_tree[2*x]*seg_tree[2*x+1];
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
    seg_tree[x] = seg_tree[2*x]*seg_tree[2*x+1];
}

int findProduct(int s,int e,int x,int l,int r) {
    if (r < s || e < l) return 1;
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    return findProduct(s,mid,2*x,l,r) * findProduct(mid+1,e,2*x+1,l,r);
}

int main() {
    FASTIO
    int n,k;
    while (cin >> n >> k) {
        for (int i = 1; i <= n; i++) {
            int value;
            cin >> value;
            if (value < 0) {
                arr[i] = -1;
            } else if (value == 0) {
                arr[i] = 0;
            } else {
                arr[i] = 1;
            }
        }
        init(1,n,1);
        for (int i = 0; i < k; i++) {
            char c;
            cin >> c;
            if (c == 'C') {
                int a,b;
                cin >> a >> b;
                b = (b > 0) ? 1 : (b == 0) ? 0 : -1;
                update(1,n,1,a,b);
            } else {
                int l,r;
                cin >> l >> r;
                int result = findProduct(1,n,1,l,r);
                char ch = (result > 0) ? '+' : (result == 0) ? '0' : '-';
                cout << ch;
            }
        }
        cout << endl;
    }
    return 0;
}