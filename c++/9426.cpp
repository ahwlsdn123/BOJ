#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;
#define MAX_TEMP 65535

int n,k;
queue<int> q;
vector<int> seg_tree;

void update(int s,int e,int x,int t,int v) {
    if (e < t || t < s) return;
    if (s == e) {
        seg_tree[x] += v;
        return;
    }
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t,v);
    update(mid+1,e,2*x+1,t,v);
    seg_tree[x] = seg_tree[2*x] + seg_tree[2*x+1];
}

int search(int s,int e,int x,int ord) {
    if (s == e) return s;
    int mid = (s+e) >> 1;
    if (seg_tree[2*x] >= ord) return search(s,mid,2*x,ord);
    else return search(mid+1,e,2*x+1,ord-seg_tree[2*x]);
}

int main() {
    FASTIO
    cin >> n >> k;
    seg_tree.assign(4*MAX_TEMP,0);
    for (int i = 0; i < k; i++) {
        int t; cin >> t;
        q.push(t);
        update(0,MAX_TEMP,1,t,1);
    }
    ll ans = 0;
    for (int i = 0; i < n-k; i++) {
        ans += search(0,MAX_TEMP,1,(k+1)/2);
        int t; cin >> t;
        update(0,MAX_TEMP,1,q.front(),-1);
        q.pop();
        q.push(t);
        update(0,MAX_TEMP,1,t,1);
    }
    ans += search(0,MAX_TEMP,1,(k+1)/2);
    cout << ans << endl;
    return 0;
}