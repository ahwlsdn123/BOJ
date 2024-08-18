#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define endl '\n'
typedef long long ll;
int parent[10001];

int find(int v) {
    if (parent[v] != v) return parent[v] = find(parent[v]);
    return v;
}

void uni(int u, int v) {
    u = find(u);
    v = find(v);
    if (u > v) {
        parent[u] = v;
    } else {
        parent[v] = u;
    }
}

bool sameParent(int u, int v) {
    u = find(u);
    v = find(v);
    if (u == v) return true;
    else return false;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);

    int v,e;
    cin >> v >> e;
    int result = 0;
    vector<pair<int,pair<int,int>>>vec;
    
    for (int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        vec.push_back({c,{a,b}});
    }
    sort(vec.begin(), vec.end());
    for (int i = 1; i <= v; i++) parent[i] = i;
    for (int i = 0; i < vec.size(); i++) {
        if (!sameParent(vec[i].second.first, vec[i].second.second)) {
            uni(vec[i].second.first, vec[i].second.second);
            result += vec[i].first;
        }
    }
    cout << result << endl;
    return 0;
}