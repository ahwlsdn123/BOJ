#include <iostream>

using namespace std;
#define endl '\n'
typedef long long ll;

int a, b, c;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> a >> b >> c;
    ll tmp = a*b*c;
    int arr[10] = {0};
    while (tmp != 0) {
        arr[tmp%10]++;
        tmp /= 10;
    }
    for (int i = 0; i < 10; i++) {
        cout << arr[i] << endl;
    }
    return 0;
}