#include <iostream>
#include <queue>
using namespace std;

typedef long long ll;
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
#define MAX_LIGHT 1000000

int n,m;
queue<int> q;
int seg_tree[4*MAX_LIGHT] = {0};

int max(int a,int b) {
    return (a>b) ? a : b;
}

void update(int s,int e,int x,int t,int v) {
    if (e < t || t < s) return;
    if (s == e) {
        seg_tree[x] += v;
        return;
    }
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t,v);
    update(mid+1,e,2*x+1,t,v);
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1];
}

int query(int s,int e,int x,int ord) {
    if (s == e) return s;
    int mid = (s+e) >> 1;
    if (seg_tree[2*x] >= ord) return query(s,mid,2*x,ord);
    else return query(mid+1,e,2*x+1,ord-seg_tree[2*x]);
}

int main() {
    FASTIO
    cin >> n >> m;
    m = 2*m-1;
    for (int i = 0; i < m; i++) {
        int light; cin >> light;
        q.push(light);
        update(1,MAX_LIGHT,1,light,1);
    }
    cout << query(1,MAX_LIGHT,1,m) << ' ';
    for (int i = 0; i < n-m; i++) {
        int light; cin >> light;
        update(1,MAX_LIGHT,1,q.front(),-1);
        q.pop();
        q.push(light);
        update(1,MAX_LIGHT,1,light,1);
        cout << query(1,MAX_LIGHT,1,m) << ' ';
    }
    cout << endl;
    return 0;
}