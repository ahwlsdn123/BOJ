#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

int n,m;
vector<int> arr;
vector<int> seg_tree[400000];

void init(int s,int e,int x) {
    if (s == e) {
        seg_tree[x].push_back(arr[s]);
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    vector<int> v1 = seg_tree[2*x];
    vector<int> v2 = seg_tree[2*x+1];
    int i = 0, j = 0;
    while (i < v1.size() && j < v2.size()) {
        if (v1[i] < v2[j]) {
            seg_tree[x].push_back(v1[i++]);
        } else {
            seg_tree[x].push_back(v2[j++]);
        }
    }
    while (i < v1.size()) {
        seg_tree[x].push_back(v1[i++]);
    }
    while (j < v2.size()) {
        seg_tree[x].push_back(v2[j++]);
    }
}

int search(int s,int e,int x,int l,int r,int v) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg_tree[x].end() - upper_bound(seg_tree[x].begin(),seg_tree[x].end(),v);
    int mid = (s+e) >> 1;
    return search(s,mid,2*x,l,r,v) + search(mid+1,e,2*x+1,l,r,v);
}

int main() {
    FASTIO
    cin >> n;
    arr.push_back(0);
    for (int i = 1; i <= n; i++) {
        int tmp; cin >> tmp;
        arr.push_back(tmp);
    }
    init(1,n,1);
    cin >> m;
    int last_ans = 0;
    for (int i = 0; i < m; i++) {
        int a,b,c; cin >> a >> b >> c;
        a ^= last_ans;
        b ^= last_ans;
        c ^= last_ans;
        last_ans = search(1,n,1,a,b,c);
        cout << last_ans << endl;
    }
    return 0;
}