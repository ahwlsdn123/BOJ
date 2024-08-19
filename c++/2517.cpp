#include <iostream>
#include <vector>
#include <algorithm>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
typedef long long ll;

using namespace std;

struct runner
{
    int ability, id;
};

int n;
vector<runner> v;
int seg_tree[2000001] = {0};

bool comp(runner a, runner b) {
    return a.ability > b.ability;
}

void update(int s, int e, int x, int t) {
    if (e < t || t < s) return;
    if (s == e) {
        seg_tree[x]++;
        return;
    }
    int mid = (s+e) >> 1;
    update(s,mid,2*x,t);
    update(mid+1,e,2*x+1,t);
    seg_tree[x] = seg_tree[2*x]+seg_tree[2*x+1];
}

int findSum(int s, int e, int x, int l, int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg_tree[x];
    int mid = (s+e) >> 1;
    return findSum(s,mid,2*x,l,r) + findSum(mid+1,e,2*x+1,l,r);
}

int main() {
    FASTIO

    cin >> n;
    v.assign(n+1,{1000000001,0});
    for (int i = 1; i <= n; i++) {
        cin >> v[i].ability;
        v[i].id = i;
    }
    sort(v.begin(),v.end(),comp);
    int answer[n+1];
    for (int i = 1; i <= n; i++) {
        update(1,n,1,v[i].id);
        if (v[i].id > 1)
            answer[v[i].id] = 1+findSum(1,n,1,1,v[i].id-1);
        else
            answer[v[i].id] = 1;
    }
    for (int i = 1; i <= n; i++) {
        cout << answer[i] << endl;
    }
}