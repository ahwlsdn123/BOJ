#include <iostream>
#include <vector>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

using namespace std;

int n,m;
int arr[100001] = {0};
vector<int> seg_tree[400000];

void init(int s,int e,int x) {
    if (s == e) {
        seg_tree[x].push_back(arr[s]);
        return;
    }
    int mid = (s+e) >> 1;
    init(s,mid,2*x);
    init(mid+1,e,2*x+1);
    int i = 0;
    int j = 0;
    while (i < mid-s+1 && j < e-mid) {
        if (seg_tree[2*x][i] < seg_tree[2*x+1][j]) {
            seg_tree[x].push_back(seg_tree[2*x][i++]);
        } else {
            seg_tree[x].push_back(seg_tree[2*x+1][j++]);
        }
    }
    while (i < mid-s+1) {
        seg_tree[x].push_back(seg_tree[2*x][i++]);
    }
    while (j < e-mid) {
        seg_tree[x].push_back(seg_tree[2*x+1][j++]);
    }
}

int bs(int x,int l,int r,int k) {
    if (l == r) return l;
    int mid = (l+r) >> 1;
    if (seg_tree[x][mid] <= k) {
        return bs(x,mid+1,r,k);
    } else {
        return bs(x,l,mid,k);
    }
}

int search(int x,int k) { // seg_tree 중에서 k보다 큰 원소의 개수
    int len = seg_tree[x].size();
    int idx = (seg_tree[x][len-1] > k) ? bs(x,0,len-1,k) : len;
    return len-idx;
}

int query(int s,int e,int x,int l,int r,int k) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) {
        return search(x,k);
    }
    int mid = (s+e) >> 1;
    return query(s,mid,2*x,l,r,k) + query(mid+1,e,2*x+1,l,r,k);
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
        int l,r,k;
        cin >> l >> r >> k;
        cout << query(1,n,1,l,r,k) << endl;
    }
    return 0;
}