#define ll long long int
#define pb push_back
#define mk make_pair
#define MOD 1000000007
#define f(i, a, b) for (int i = a; i < b; ++i)
#define rf(i, a, b) for (int i = a; i >= b; --i)
#define fi(n, a)                \
    vector<ll> a(n);            \
    for (int i = 0; i < n; ++i) \
        cin >> a[i];

// #include<iostream>
#include <bits/stdc++.h>
using namespace std;

void solve()
{

    string a, b;
    cin >> a >> b;

    if (a == b){
        cout << "YES" << endl;
        return;
    }
        

   

    bool flag = false;
    f(i, 0 , a.size()-1){
        if(a[i] == '0' && b[i] == '0' && a[i+1] == '1' && b[i+1] == '1') flag = true;
    }

    if (flag)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}

int main()
{

    int t;
    cin >> t;

    while (t--)
    {
        solve();
    }

    return 0;
}