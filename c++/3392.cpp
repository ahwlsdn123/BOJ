#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define endl '\n'
#define MAX_LEAF 30000

class Info {
public:
    int x,y1,y2;
    bool left;
    Info() {}
    Info(int x,int y1,int y2,bool left) {
        this->x = x;
        this->y1 = y1;
        this->y2 = y2;
        this->left = left;
    }
    bool operator < (const Info & b) const {
        return this->x < b.x;
    }
};

vector<Info> vec;
pair<int,int> seg_tree[4*MAX_LEAF];

void update(int s,int e,int x,int l,int r,int v) {
    if (e < l || r < s) return;

    if (l <= s && e <= r) {
        seg_tree[x].second += v;
    } else {
        int mid = (s+e) >> 1;
        update(s,mid,2*x,l,r,v);
        update(mid+1,e,2*x+1,l,r,v);
    }

    if (!seg_tree[x].second) {
        if (s != e) seg_tree[x].first = seg_tree[2*x].first + seg_tree[2*x+1].first;
        else seg_tree[x].first = 0;
    } else {
        seg_tree[x].first = e-s+1;
    }
}

int main() {
    FASTIO
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        int x1,y1,x2,y2; cin >> x1 >> y1 >> x2 >> y2;
        vec.push_back(Info(x1,y1,y2,true));
        vec.push_back(Info(x2,y1,y2,false));
    }
    sort(vec.begin(),vec.end());

    int ans = 0;
    for (int i = 0; i < vec.size(); i++) {
        if (i) ans += (vec[i].x - vec[i-1].x) * seg_tree[1].first;
        int value = vec[i].left ? 1 : -1;
        update(0,MAX_LEAF-1,1,vec[i].y1,vec[i].y2-1,value);
    }
    cout << ans << endl;
}