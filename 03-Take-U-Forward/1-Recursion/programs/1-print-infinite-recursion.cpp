// print recursion function infinite times
// Without base condition
#include<bits/stdc++.h>
using namespace std;

void print()
{
    cout<<1<<endl;
    print();
}
int main()
{
    // #ifdef ONLINE_JUDGE
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "r", stdout);
    // #endif
    print();
    return 0;
}
