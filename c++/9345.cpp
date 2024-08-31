#include <iostream>
using namespace std;

#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

int t,n,k;
int arr[100000] = {0};
pair<int,int> seg_tree[400000];

void init(int s,int e,int x) {
    if (s == e) {
        seg_tree[x] = {s,e};
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    seg_tree[x] = {seg_tree[2*x].first, seg_tree[2*x+1].second};
}

int min(int a,int b) {
    return (a < b) ? a : b;
}

int max(int a,int b) {
    return (a > b) ? a : b;
}

void update(int s,int e,int x,int t,int v) {
    if (e < t || t < s) return;
    if (s == e) {
        seg_tree[x] = {v,v};
        return;
    }
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t,v);
    update(mid+1,e,2*x+1,t,v);
    seg_tree[x] = {min(seg_tree[2*x].first,seg_tree[2*x+1].first),max(seg_tree[2*x].second,seg_tree[2*x+1].second)};
}

pair<int,int> search(int s,int e,int x,int l,int r) {
    if (r < s || e < l) return {n+1,-1};
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    pair<int,int> p1 = search(s,mid,2*x,l,r);
    pair<int,int> p2 = search(mid+1,e,2*x+1,l,r);
    return {min(p1.first,p2.first),max(p1.second,p2.second)};
}

int main() {
    FASTIO
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n >> k;
        for (int j = 0; j < n; j++) {
            arr[j] = j;
        }
        init(0,n-1,1);
        for (int j = 0; j < k; j++) {
            int q,a,b; cin >> q >> a >> b;
            if (q == 0) {
                update(0,n-1,1,a,arr[b]);
                update(0,n-1,1,b,arr[a]);
                int tmp = arr[a];
                arr[a] = arr[b];
                arr[b] = tmp;
            } else {
                pair<int,int> p = search(0,n-1,1,a,b);
                if (p.first == a && p.second == b) cout << "YES\n";
                else cout << "NO\n";
            }
        }
    }
    return 0;
}