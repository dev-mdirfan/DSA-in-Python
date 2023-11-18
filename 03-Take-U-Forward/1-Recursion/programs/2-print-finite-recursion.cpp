// print recursion function finite times
// With base condition
#include<bits/stdc++.h>
using namespace std;

int count = 0;
void print()
{
    if (count == 3)
        return ;
    cout<<count<<endl;
    count++;
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
