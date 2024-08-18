#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define MAX 100001
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;
struct INFO {
    int U, V, T;
};

int N, M;
vector<INFO> Edge;
int Parent[MAX];
int D = 1;

void init() {
    for (int i = 0; i < MAX; i++) {
        Parent[i] = i;
    }
}

void input() {
    cin >> N >> M;
    Edge.resize(M);
    for (int i = 0; i < M; i++) {
        cin >> Edge[i].U >> Edge[i].V >> Edge[i].T;
    }
}

int find_Parent(int X) {
    if (Parent[X] == X) {
        return X;
    }
    return Parent[X] = find_Parent(Parent[X]);
}

void union_Group(int X, int Y) {
    int PX = find_Parent(X);
    int PY = find_Parent(Y);
    if (PX < PY) {
        Parent[PY] = PX;
    }
    else {
        Parent[PX] = PY;
    }
}

bool Comp(INFO A, INFO B) {
    return (A.T < B.T);
}

void settings() {
    sort(Edge.begin(), Edge.end(), Comp);
    for (int i = 0; i < M; i++) {
        int U = Edge[i].U;
        int V = Edge[i].V;
        int T = Edge[i].T;
        if (T != D) {
            break;
        }
        if (find_Parent(U) != find_Parent(V)) {
            union_Group(U, V);
            D++;
        }
    }
}

void find_Answer() {
    cout << D << "\n";
}

int main() {
    FASTIO
    init();
    input();
    settings();
    find_Answer();

    return 0;
}