#include <iostream>
#include <vector>
using namespace std;

#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

int n,k;
vector<int> seg_tree;

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

int get_number_and_remove(int s,int e,int x,int idx) {
    seg_tree[x]--;
    if (s == e) return s;
    int mid = (s+e) >> 1;
    if (seg_tree[2*x] >= idx) {
        return get_number_and_remove(s,mid,2*x,idx);
    } else {
        return get_number_and_remove(mid+1,e,2*x+1,idx-seg_tree[2*x]);
    }
}

int main() {
    FASTIO

    cin >> n >> k;
    seg_tree.assign(4*n,0);
    init(1,n,1);
    int idx = 1;
    cout << '<';
    while (seg_tree[1]) {
        idx = ((idx + (k-2)) % seg_tree[1]) + 1;
        cout << get_number_and_remove(1,n,1,idx);
        if (seg_tree[1]) cout << ", ";
    }
    cout << ">\n";
    return 0;
}