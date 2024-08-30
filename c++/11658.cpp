#include <bits/stdc++.h>
#define FastIO ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
using namespace std;

int N, M;
int save[1025][1025];
vector<vector<long long>> tree;

void init_y(int node, int left, int right, int xnode, int idx) {
    if (left == right) {
        tree[xnode][node] = save[idx][left];
        return;
    }

    init_y(node * 2, left, (left + right) / 2, xnode, idx);
    init_y(node * 2 + 1, (left + right) / 2 + 1, right, xnode, idx);

    tree[xnode][node] = tree[xnode][node * 2] + tree[xnode][node * 2 + 1];
}

void init_x(int node, int left, int right) {
    if (left == right) {
        init_y(1, 1, N, node, left);
        return;
    }

    init_x(node * 2, left, (left + right) / 2);
    init_x(node * 2 + 1, (left + right) / 2 + 1, right);

    for (int i = 1; i < tree[node].size(); i++) {
        tree[node][i] = tree[node * 2][i] + tree[node * 2 + 1][i];
    }
}

void update_y(int node, int left, int right, int y, int xnode, int val) {
    if (left > y || right < y) return;
    if (left == right) {
        tree[xnode][node] = val;
        for (int i = xnode >> 1; i >= 1; i >>= 1) {
            tree[i][node] = tree[i * 2][node] + tree[i * 2 + 1][node];
        }
        return;
    }

    update_y(node * 2, left, (left + right) / 2, y, xnode, val);
    update_y(node * 2 + 1, (left + right) / 2 + 1, right, y, xnode, val);

    tree[xnode][node] = tree[xnode][node * 2] + tree[xnode][node * 2 + 1];
    for (int i = xnode >> 1; i >= 1; i >>= 1) {
        tree[i][node] = tree[i * 2][node] + tree[i * 2 + 1][node];
    }
}

void update_x(int node, int left, int right, int x, int y, int val) {
    if (left > x || right < x) return;
    if (left == right) {
        update_y(1, 1, N, y, node, val);
        return;
    }

    update_x(node * 2, left, (left + right) / 2, x, y, val);
    update_x(node * 2 + 1, (left + right) / 2 + 1, right, x, y, val);
}

long long query_y(int node, int left, int right, int y1, int y2, int xnode) {
    if (right < y1 || left > y2) return 0;
    if (y1 <= left && right <= y2) {
        return tree[xnode][node];
    }

    long long l = query_y(node * 2, left, (left + right) / 2, y1, y2, xnode);
    long long r = query_y(node * 2 + 1, (left + right) / 2 + 1, right, y1, y2, xnode);

    return l + r;
}

long long query_x(int node, int left, int right, int x1, int x2, int y1, int y2) {
    if (x1 > right || x2 < left) return 0;
    else if (x1 <= left && right <= x2) return query_y(1, 1, N, y1, y2, node);

    long long l = query_x(node * 2, left, (left + right) / 2, x1, x2, y1, y2);
    long long r = query_x(node * 2 + 1, (left + right) / 2 + 1, right, x1, x2, y1, y2);

    return l + r;
}

int main() {
    FastIO

    cin >> N >> M;
    int tree_depth = (int)ceil(log2(N));
    int tree_size = (1 << (tree_depth + 1));
    tree = vector(tree_size, vector<long long>(tree_size));

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> save[i][j];
        }
    }

    init_x(1, 1, N);

    for (int i = 0; i < M; i++) {
        int order;
        cin >> order;

        if (order) {
            int x1, x2, y1, y2;
            cin >> x1 >> x2 >> y1 >> y2;

            cout << query_x(1, 1, N, x1, y1, x2, y2) << '\n';
        }
        else {
            int x, y, c;
            cin >> x >> y >> c;

            update_x(1, 1, N, x, y, c);
        }
    }

    return 0;
}