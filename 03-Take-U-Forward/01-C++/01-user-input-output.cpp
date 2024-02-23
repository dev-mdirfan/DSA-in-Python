// There are many header files in C++ which are used for different purposes. Some of the header files are:
#include <iostream> // Header file for input output functions
#include <string>   // Header file for string functions
#include <math.h>   // Header file for mathematical functions
#include <vector>   // Header file for vector functions
#include <algorithm> // Header file for sorting and searching functions
#include <map>       // Header file for map functions
#include <set>       // Header file for set functions
#include <queue>     // Header file for queue functions
#include <stack>     // Header file for stack functions
#include <deque>     // Header file for deque functions
#include <list>      // Header file for list functions
#include <iterator>  // Header file for iterator functions
#include <bitset>    // Header file for bitset functions
#include <utility>   // Header file for pair and other utility functions
#include <functional> // Header file for functional functions
#include <numeric>    // Header file for numeric functions
#include <limits>     // Header file for limits functions

#include <bits/stdc++.h> // This header file includes all the standard libraries

int output()
{
    std::cout << "Hello World" << std::endl; // std::cout is used to print the output to the console
    std::cout << "Welcome to C++"
              << "\n"; // "\n" is more faster than std::endl
    std::cout << "This is a new line" << std::endl;
    return 0;
}

int input()
{
    std::string name;
    std::cout << "Enter your name: ";
    std::cin >> name; // std::cin is used to take input from the user
    std::cout << "Hello " << name << std::endl;
    return 0;
}

using namespace std; // This line is used to avoid writing std:: before every cout and cin statement
int main()
{
    input();
    output();

    int x, y;
    cin >> x >> y; // Taking two inputs at the same time
    cout << "Value of x is: " << x << "and y is: " << y << endl;
    return 0;
}

/*
Enter your name: Irfan
Hello Irfan
Hello World
Welcome to C++
This is a new line
34
Value of x is: 34
*/

