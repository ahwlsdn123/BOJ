#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;
struct info
{
    int a,b,c;
};


int parent[2001];

int find(int v) {
    if (parent[v] != v) return parent[v] = find(parent[v]);
    return v;
}

void uni(int u, int v) {
    u = find(u);
    v = find(v);
    if (u > v) parent[u] = v;
    else parent[v] = u;
}

bool sameParent(int u, int v) {
    return find(u) == find(v);
}

bool comp(info a, info b) {
    return a.c < b.c;
}

int main() {
    int n,m,s;
    cin >> n >> m >> s;

    vector<info> edges;
    edges.resize(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].a >> edges[i].b >> edges[i].c;
    }

    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }

    int result = 0;
    int cnt = 0;
    sort(edges.begin(), edges.end(), comp);
    for (int i = 0; i < m; i++) {
        if (!sameParent(edges[i].a, edges[i].b)) {
            uni(edges[i].a, edges[i].b);
            result += edges[i].c;
            if (++cnt == n-1) {
                break;
            }
        }
    }
    string str;
    cin >> str;
    if (cnt == n-1)
        cout << result << endl;
    else
        cout << -1 << endl;
    return 0;
}