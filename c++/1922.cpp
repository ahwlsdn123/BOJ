#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define endl '\n'

int parent[1001];

int find(int v) {
    if (parent[v] != v)
        return parent[v] = find(parent[v]);
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
    if (u != v) return false;
    else return true;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);

    int n,m;
    cin >> n >> m;

    vector<pair<int,pair<int,int>>> edges;
    for (int i = 0; i < m; i++) {
        int a,b,c;
        cin >> a >> b >> c;
        edges.push_back({c,{a,b}});
    }
    sort(edges.begin(),edges.end());

    int result = 0;
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }
    for (int i = 0; i < m; i++) {
        if (!sameParent(edges[i].second.first,edges[i].second.second)) {
            uni(edges[i].second.first,edges[i].second.second);
            result += edges[i].first;
        }
    }
    cout << result << endl;
    return 0;
}