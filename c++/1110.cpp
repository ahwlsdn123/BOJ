#include <iostream>

using namespace std;
#define endl '\n'

int n;

int main() {
    cin >> n;
    int tmp = n;
    int cnt = 0;
    do
    {
        cnt++;
        int a = tmp/10;
        int b = tmp%10;
        tmp = 10*b + (a+b)%10;
    } while (tmp != n);
    cout << cnt << endl;
}