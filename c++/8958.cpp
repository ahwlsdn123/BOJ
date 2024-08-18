#include <iostream>
#include <string>

using namespace std;
#define endl '\n'
typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    int t;
    string s;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> s;
        int sum, cnt;
        sum = cnt = 0;
        for (int j = 0; j < s.length(); j++) {
            if (s[j] == 'O') cnt++;
            else cnt = 0;
            sum += cnt;
        }
        cout << sum << endl;
    }
}