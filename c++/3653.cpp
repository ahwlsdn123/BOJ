#include <iostream>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

using namespace std;

int n,m;
int seg_tree[1000000];
int location[100001];

void init(int s,int e,int x) {
    if (s == e) {
        if (s <= m+1) {
            seg_tree[x] = 0;
        } else {
            seg_tree[x] = 1;
        }
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1];
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
    seg_tree[x] = seg_tree[2*x] + seg_tree[2*x+1];
}

int findSum(int s,int e,int x,int l,int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    return findSum(s,mid,2*x,l,r) + findSum(mid+1,e,2*x+1,l,r);
}

int main() {
    FASTIO
    int t;
    cin >> t;
    for (int j = 0; j < t; j++) {
        cin >> n >> m;
        for (int i = 1; i <= n; i++) {
            location[i] = 1+m+i;
        }
        init(1,1+m+n,1);
        int new_location = 1+m;
        for (int i = 0; i < m; i++) {
            int dvd;
            cin >> dvd;
            cout << findSum(1,1+m+n,1,1,location[dvd]-1) << ' ';
            update(1,1+m+n,1,location[dvd],0);
            location[dvd] = new_location--;
            update(1,1+m+n,1,location[dvd],1);
        }
        cout << endl;
    }
    return 0;
}