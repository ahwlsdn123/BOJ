#include <iostream>
#include <vector>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;
#define INF 1000000001

using namespace std;


int n,m;
int arr[100001];
vector<pair<int,int>> seg_tree;

bool comp(pair<int,int> x, pair<int,int> y) {
    return x.first < y.first || (x.first == y.first && x.second < y.second);
}

void init(int s,int e,int x) {
    if (s == e) {
        seg_tree[x] = {arr[s],s};
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    if (comp(seg_tree[2*x],seg_tree[2*x+1])) {
        seg_tree[x] = seg_tree[2*x];
    } else {
        seg_tree[x] = seg_tree[2*x+1];
    }
}

void update(int s,int e,int x,int t,int v) {
    if (e < t || t < s) return;
    if (s == e) {
        seg_tree[x].first = v;
        return;
    }
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t,v);
    update(mid+1,e,2*x+1,t,v);
    if (comp(seg_tree[2*x],seg_tree[2*x+1])) {
        seg_tree[x] = seg_tree[2*x];
    } else {
        seg_tree[x] = seg_tree[2*x+1];
    }
}

pair<int,int> findMinNode(int s,int e,int x,int l,int r) {
    if (r < s || e < l) return {INF,0};
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    pair<int,int> n1 = findMinNode(s,mid,2*x,l,r);
    pair<int,int> n2 = findMinNode(mid+1,e,2*x+1,l,r);
    return comp(n1,n2) ? n1: n2;
}

int main() {
    FASTIO
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    seg_tree.assign(4*n,{0,0});
    init(1,n,1);
    cin >> m;
    for (int i = 0; i < m; i++) {
        int q;
        cin >> q;
        if (q == 1) {
            int t,v;
            cin >> t >> v;
            update(1,n,1,t,v);
        } else {
            pair<int,int> result = findMinNode(1,n,1,1,n);
            cout << result.second << endl;
        }
    }
    return 0;
}