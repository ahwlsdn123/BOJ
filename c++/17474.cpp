#include <iostream>
#include <algorithm>
 
using namespace std;
#define endl '\n'
typedef long long ll;
 
 
struct Node{
    ll max, cnt, max2, sum;
};
 
int N, M;
int a[1010101];
Node seg[4040404];
 
 
Node merge(Node l, Node r){
    if (l.max == r.max) return {l.max, l.cnt + r.cnt, max(l.max2, r.max2), l.sum + r.sum};
    if (l.max < r.max) return {r.max, r.cnt, max(l.max, r.max2), l.sum + r.sum};
    return {l.max, l.cnt, max(l.max2, r.max), l.sum + r.sum};
}
 
Node init(int x, int s, int e){
    if (s == e) return seg[x] = {a[s], 1, -1, a[s]};
    int m = (s + e) / 2;
    return seg[x] = merge(init(x * 2, s, m), init(x * 2 + 1, m + 1, e));
}
 
void lazyProp(int x, int s, int e){
    if (s == e) return;
 
    for (int i = x * 2; i <= x * 2 + 1; i++){
        if (seg[x].max < seg[i].max){
            seg[i].sum -= (seg[i].max-seg[x].max) * seg[i].cnt;
            seg[i].max = seg[x].max;
        }
    }
}
 
void update(int x, int s, int e, int l, int r, int k){
    lazyProp(x, s, e);
    if (r < s || e < l || seg[x].max <= k) return;
    if (l <= s && e <= r && seg[x].max2 < k){
        seg[x].sum -= (seg[x].max-k) * seg[x].cnt;
        seg[x].max = k;
        lazyProp(x, s, e);
        return;
    }
 
    int m = (s + e) / 2;
    update(x * 2, s, m, l, r, k);
    update(x * 2 + 1, m + 1, e, l, r, k);
 
    seg[x] = merge(seg[x * 2], seg[x * 2 + 1]);
}
 
ll getMax(int x, int s, int e, int l, int r){
    lazyProp(x, s, e);
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg[x].max;
 
    int m = (s + e) / 2;
    return max(getMax(x * 2, s, m, l, r), getMax(x * 2 + 1, m + 1, e, l, r));
}
 
ll getSum(int x, int s, int e, int l, int r){
    lazyProp(x, s, e);
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg[x].sum;
 
    int m = (s + e) / 2;
    return getSum(x * 2, s, m, l, r) + getSum(x * 2 + 1, m + 1, e, l, r);
}
 
 
int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> N;
    for (int i = 1; i <= N; i++){
        cin >> a[i];
    }
    init(1, 1, N);
    cin >> M;
    for (int qr = 0; qr < M; qr++){
        int Q, i, j, k;
        cin >> Q >> i >> j;
        if (Q == 1){
            cin >> k;
            update(1, 1, N, i, j, k);
        }
        else if (Q == 2){
            cout << getMax(1, 1, N, i, j) << endl;
        }
        else{
            cout << getSum(1, 1, N, i, j) << endl;
        }
    }
    return 0;
}