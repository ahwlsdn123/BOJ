#include <iostream>
using namespace std;

typedef long long ll;
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
#define MOD 1000000007
#define MAX_LOC 200000

ll n;
pair<ll,ll> seg_tree[4*MAX_LOC] = {{0,0}};

void update(ll s,ll e,ll x,ll loc) {
    if (e < loc || loc < s) return;
    if (s == e) {
        seg_tree[x].first += loc;
        seg_tree[x].second++;
        return;
    }
    ll mid = (s+e) >> 1;
    update(s,mid,2*x,loc);
    update(mid+1,e,2*x+1,loc);
    seg_tree[x].first = seg_tree[2*x].first + seg_tree[2*x+1].first;
    seg_tree[x].second = seg_tree[2*x].second + seg_tree[2*x+1].second;
}

pair<ll,ll> query(ll s,ll e,ll x,ll l,ll r) {
    if (r < s || e < l) return {0,0};
    if (l <= s && e <= r) return seg_tree[x];
    ll mid = (s+e) >> 1;
    pair<ll,ll> p1 = query(s,mid,2*x,l,r);
    pair<ll,ll> p2 = query(mid+1,e,2*x+1,l,r);
    return {p1.first+p2.first, p1.second+p2.second};
}

int main() {
    FASTIO
    cin >> n;
    ll loc; cin >> loc;
    update(0,MAX_LOC,1,loc);
    ll ans = 1;
    for (ll i = 1; i < n; i++) {
        cin >> loc;
        update(0,MAX_LOC,1,loc);
        pair<ll,ll> p1,p2;
        if (loc == 0) p1 = {0,0};
        else p1 = query(0,MAX_LOC,1,0,loc-1);
        if (loc == MAX_LOC) p2 = {0,0};
        else p2 = query(0,MAX_LOC,1,loc+1,MAX_LOC);
        ans *= (p2.first + loc*(p1.second-p2.second) - p1.first) % MOD;
        ans %= MOD;
    }
    cout << ans << endl;
}